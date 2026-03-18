"""
Generate Figure 1: Choropleth of construction-era asbestos risk across Fukuoka Prefecture.

Downloads Fukuoka municipality boundaries from 国土数値情報 (MLIT N03 dataset),
aggregates district-level risk scores to municipality level (weighted by n_buildings),
and produces a publication-quality choropleth map.

Requirements:
    pip install geopandas matplotlib numpy

Output:
    figure1_risk_choropleth.png  (300 dpi, ~8x9 inches)
"""

import io
import json
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path

import geopandas as gpd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "asbestos_risk_districts.json"
OUTPUT_FILE = HERE / "figure1_risk_choropleth.png"
CACHE_DIR = HERE / "_cache"
CACHE_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------------
# N03 boundary data (MLIT 国土数値情報, Fukuoka Prefecture = code 40)
# ---------------------------------------------------------------------------
N03_URL = (
    "https://nlftp.mlit.go.jp/ksj/gml/data/N03/N03-2024/"
    "N03-20240101_40_GML.zip"
)
N03_CACHE = CACHE_DIR / "N03_fukuoka.gpkg"

# ---------------------------------------------------------------------------
# Risk palette — 5-level sequential, print-safe
# ---------------------------------------------------------------------------
RISK_COLORS = {
    "very_high":   "#d73027",  # RdYlBu vivid red
    "high":        "#fc8d59",  # RdYlBu orange
    "elevated":    "#fee090",  # RdYlBu pale yellow
    "low_moderate":"#91bfdb",  # RdYlBu mid blue
    "low":         "#e0f3f8",  # RdYlBu very pale blue
    "no_data":     "#e8e8e8",  # light grey
}
RISK_ORDER = ["very_high", "high", "elevated", "low_moderate", "low"]
RISK_LABELS = {
    "very_high":   "Very High  (score ≥ 75)",
    "high":        "High  (55–74)",
    "elevated":    "Elevated  (35–54)",
    "low_moderate":"Low-Moderate  (15–34)",
    "low":         "Low  (< 15)",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def score_to_level(score: float) -> str:
    if score >= 75: return "very_high"
    if score >= 55: return "high"
    if score >= 35: return "elevated"
    if score >= 15: return "low_moderate"
    return "low"


def load_districts() -> list:
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)["districts"]


def aggregate_to_municipality(districts: list) -> dict:
    """Max district risk score per municipality (JIS 5-digit code).

    Using max rather than weighted mean so that municipalities containing
    even one very-high-risk district show as very_high. Weighted mean dilutes
    the signal when newer buildings coexist with pre-1975 stock.
    """
    acc = defaultdict(lambda: {"max_score": 0.0, "n": 0, "name": ""})
    for d in districts:
        code = d["municipality_code"]
        n    = d["n_buildings"]
        score = d["risk_score"]
        if score > acc[code]["max_score"]:
            acc[code]["max_score"] = score
        acc[code]["n"]    += n
        acc[code]["name"]  = d["municipality"]
    return {
        code: {
            "max_score":    v["max_score"],
            "n_buildings":  v["n"],
            "risk_level":   score_to_level(v["max_score"]),
            "municipality": v["name"],
        }
        for code, v in acc.items()
    }


def get_boundaries() -> gpd.GeoDataFrame:
    if N03_CACHE.exists():
        print("Using cached boundary data.")
        return gpd.read_file(N03_CACHE)

    print("Downloading Fukuoka boundary data from 国土数値情報 …")
    req = urllib.request.Request(
        N03_URL,
        headers={"User-Agent": "Mozilla/5.0 (academic research use)"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        zip_bytes = resp.read()

    # Shapefiles are multi-file — extract entire ZIP to a temp dir on disk
    import tempfile, shutil
    tmp_dir = Path(tempfile.mkdtemp())
    try:
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            zf.extractall(tmp_dir)

        shp_files = list(tmp_dir.rglob("*.shp"))
        if not shp_files:
            raise RuntimeError(f"No .shp found after extraction. Contents: {list(tmp_dir.rglob('*'))}")
        target = shp_files[0]
        print(f"Reading: {target.name}")
        gdf = gpd.read_file(target)
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

    gdf.to_file(N03_CACHE, driver="GPKG")
    print(f"Cached to {N03_CACHE}")
    return gdf


# ---------------------------------------------------------------------------
# Figure
# ---------------------------------------------------------------------------
def make_figure(gdf: gpd.GeoDataFrame, muni_scores: dict) -> None:
    # N03 column names: N03_001 prefecture, N03_004 city/ward, N03_005 JIS code
    # Dissolve to municipality level (N03_005 is the unique code per municipality)
    code_col = "N03_007"
    if code_col not in gdf.columns:
        print(f"Columns available: {list(gdf.columns)}")
        raise KeyError(f"Expected column '{code_col}' not found in boundary data.")

    gdf_muni = gdf.dissolve(by=code_col, as_index=False)
    gdf_muni = gdf_muni.to_crs(epsg=6674)  # JGD2011 / Japan Plane Rectangular IX — appropriate for Fukuoka

    # Join risk data
    gdf_muni["risk_level"]  = gdf_muni[code_col].map(
        lambda c: muni_scores.get(c, {}).get("risk_level", "no_data")
    )
    gdf_muni["max_score"]   = gdf_muni[code_col].map(
        lambda c: muni_scores.get(c, {}).get("max_score", np.nan)
    )
    gdf_muni["face_color"]  = gdf_muni["risk_level"].map(
        lambda r: RISK_COLORS.get(r, RISK_COLORS["no_data"])
    )

    scored   = gdf_muni[gdf_muni["risk_level"] != "no_data"]
    unscored = gdf_muni[gdf_muni["risk_level"] == "no_data"]

    n_scored   = len(scored)
    n_unscored = len(unscored)
    print(f"Municipalities scored: {n_scored}  |  no data: {n_unscored}")

    # Compute zoom bounds from scored wards + padding
    bounds  = scored.total_bounds          # minx, miny, maxx, maxy
    x_pad   = (bounds[2] - bounds[0]) * 0.12
    y_pad   = (bounds[3] - bounds[1]) * 0.12
    x0, y0  = bounds[0] - x_pad, bounds[1] - y_pad
    x1, y1  = bounds[2] + x_pad, bounds[3] + y_pad

    # ---- Plot ---------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7.0, 7.0))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)

    # Unscored municipalities (context, lighter)
    if not unscored.empty:
        unscored.plot(ax=ax, color="#e8e8e8", edgecolor="#bbbbbb", linewidth=0.35)

    # Scored wards
    for level in RISK_ORDER:
        subset = scored[scored["risk_level"] == level]
        if not subset.empty:
            subset.plot(ax=ax, color=RISK_COLORS[level],
                        edgecolor="#333333", linewidth=0.8)

    # Ward name labels
    ward_labels = {
        "40131": "Higashi",
        "40132": "Hakata",
        "40133": "Chuo",
        "40134": "Minami",
        "40135": "Nishi",
        "40136": "Jonan",
        "40137": "Sawara",
    }
    for _, row in scored.iterrows():
        code    = row[code_col]
        label   = ward_labels.get(code, "")
        centroid = row.geometry.centroid
        if x0 < centroid.x < x1 and y0 < centroid.y < y1:
            ax.text(
                centroid.x, centroid.y, label,
                ha="center", va="center",
                fontsize=6.5, color="#111111",
                fontweight="bold",
            )

    # ---- Legend -------------------------------------------------------------
    legend_patches = [
        mpatches.Patch(facecolor=RISK_COLORS[lvl], edgecolor="#333333",
                       linewidth=0.5, label=RISK_LABELS[lvl])
        for lvl in RISK_ORDER
    ]
    ax.legend(
        handles=legend_patches,
        loc="lower left",
        fontsize=7.5,
        title="Construction-era asbestos risk",
        title_fontsize=8,
        framealpha=0.93,
        edgecolor="#888888",
        handlelength=1.4,
        handleheight=1.1,
        borderpad=0.75,
        labelspacing=0.45,
    )

    # ---- Source note (English only — no CJK glyphs in caption) --------------
    ax.text(
        0.5, -0.01,
        "Fig. 1  Construction-era asbestos risk by municipality, Fukuoka Prefecture (51 municipalities, 1,360 districts, 31,184 transactions).\n"
        "Colour shows the highest-scoring district within each municipality. District-level data available in the open dataset.\n"
        "Data: MLIT Real Estate Information Library, 2022-2024. DOI: 10.5281/zenodo.19087985",
        transform=ax.transAxes,
        ha="center", va="top",
        fontsize=6.5, color="#444444", linespacing=1.5,
    )

    plt.tight_layout(pad=0.3)
    plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight", facecolor="white")
    print(f"\nSaved: {OUTPUT_FILE}")
    plt.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    districts   = load_districts()
    muni_scores = aggregate_to_municipality(districts)
    print(f"Municipalities with data: {len(muni_scores)}")

    gdf = get_boundaries()
    print(f"Boundary polygons loaded: {len(gdf)}  |  CRS: {gdf.crs}")

    make_figure(gdf, muni_scores)


if __name__ == "__main__":
    main()

"""
Build asbestos risk overlay data from MLIT Fukuoka transactions.

Reads: aurora-finder/data/transactions/fukuoka_transactions_2024.csv
Writes: asbestos_risk_districts.json

Risk model:
  Pre-1975  → very_high (100 pts)
  1975–1989 → high (75 pts)
  1990–1999 → elevated (50 pts)
  2000–2005 → low_moderate (25 pts)
  Post-2006 → low (0 pts)

District score = weighted average across all buildings in district.
Districts with fewer than 3 data points are excluded.
"""

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

MLIT_CSV = Path(__file__).resolve().parent.parent.parent / "aurora-finder/data/transactions/fukuoka_transactions_2024.csv"
OUTPUT   = Path(__file__).resolve().parent / "asbestos_risk_districts.json"

MIN_BUILDINGS = 3  # minimum data points per district

def parse_year(s):
    m = re.search(r"(\d{4})", s)
    return int(m.group(1)) if m else None

def risk_points(year):
    if year < 1975: return 100
    if year < 1990: return 75
    if year < 2000: return 50
    if year < 2006: return 25
    return 0

def risk_label(score):
    if score >= 75: return "very_high"
    if score >= 55: return "high"
    if score >= 35: return "elevated"
    if score >= 15: return "low_moderate"
    return "low"

def main():
    if not MLIT_CSV.exists():
        print(f"ERROR: {MLIT_CSV} not found", file=sys.stderr)
        sys.exit(1)

    districts = defaultdict(lambda: {
        "years": [], "structures": defaultdict(int),
        "municipality": "", "district": "", "ward": "",
        "municipality_code": ""
    })

    with open(MLIT_CSV, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = parse_year(row.get("BuildingYear", ""))
            if not year:
                continue

            muni = row.get("Municipality", "").strip()
            dist = row.get("DistrictName", "").strip()
            ward = row.get("ward_name", "").strip()
            code = row.get("MunicipalityCode", "").strip()
            structure = row.get("Structure", "").strip()

            key = f"{code}_{dist}"
            d = districts[key]
            d["municipality"] = muni
            d["district"] = dist
            d["ward"] = ward
            d["municipality_code"] = code
            d["years"].append(year)
            if structure:
                d["structures"][structure] += 1

    results = []
    for key, d in districts.items():
        n = len(d["years"])
        if n < MIN_BUILDINGS:
            continue

        avg_year = sum(d["years"]) / n
        score = sum(risk_points(y) for y in d["years"]) / n

        # Structure breakdown
        structures = dict(d["structures"])
        dom_structure = max(structures, key=structures.get) if structures else "unknown"

        # Year band counts
        pre_1975 = sum(1 for y in d["years"] if y < 1975)
        y1975_89 = sum(1 for y in d["years"] if 1975 <= y < 1990)
        y1990_99 = sum(1 for y in d["years"] if 1990 <= y < 2000)
        y2000_05 = sum(1 for y in d["years"] if 2000 <= y < 2006)
        post_2006 = sum(1 for y in d["years"] if y >= 2006)

        results.append({
            "municipality": d["municipality"],
            "municipality_code": d["municipality_code"],
            "district": d["district"],
            "ward": d["ward"],
            "n_buildings": n,
            "avg_year_built": round(avg_year),
            "risk_score": round(score, 1),
            "risk_level": risk_label(score),
            "dominant_structure": dom_structure,
            "year_bands": {
                "pre_1975": pre_1975,
                "1975_1989": y1975_89,
                "1990_1999": y1990_99,
                "2000_2005": y2000_05,
                "post_2006": post_2006,
            },
            "structures": structures,
        })

    results.sort(key=lambda x: x["risk_score"], reverse=True)

    output = {
        "meta": {
            "source": "MLIT Real Estate Information Library (不動産情報ライブラリ)",
            "source_file": "fukuoka_transactions_2024.csv",
            "total_transactions": sum(r["n_buildings"] for r in results),
            "districts_scored": len(results),
            "min_buildings_threshold": MIN_BUILDINGS,
            "risk_model": {
                "pre_1975": "very_high (100 pts)",
                "1975_1989": "high (75 pts)",
                "1990_1999": "elevated (50 pts)",
                "2000_2005": "low_moderate (25 pts)",
                "post_2006": "low (0 pts)",
            },
            "score_thresholds": {
                "very_high": ">= 75",
                "high": ">= 55",
                "elevated": ">= 35",
                "low_moderate": ">= 15",
                "low": "< 15",
            },
            "generated_by": "build_asbestos_overlay.py",
        },
        "districts": results,
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Summary
    from collections import Counter
    levels = Counter(r["risk_level"] for r in results)
    print(f"Wrote {len(results)} districts to {OUTPUT}")
    print(f"Total buildings scored: {sum(r['n_buildings'] for r in results)}")
    for level in ["very_high", "high", "elevated", "low_moderate", "low"]:
        print(f"  {level}: {levels.get(level, 0)} districts")

if __name__ == "__main__":
    main()

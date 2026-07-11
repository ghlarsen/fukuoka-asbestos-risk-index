# Fukuoka Asbestos Risk Index

[![DOI](https://zenodo.org/badge/1185157267.svg)](https://doi.org/10.5281/zenodo.19087985)

**A Construction-Era Asbestos Risk Index for Residential Districts in Fukuoka Prefecture Using MLIT Transaction Data**

Sebastian Larsen, Yudane (yudane.com), Denmark

---

## Overview

This repository contains the complete data pipeline and derived dataset for a district-level asbestos risk index covering Fukuoka Prefecture, Japan. The methodology uses building construction year data from the MLIT Real Estate Information Library (不動産情報ライブラリ) to assign construction-era risk scores to 1,360 residential districts across all 51 municipalities of Fukuoka Prefecture.

The methodology paper is included in this repository (`asbestos-methodology-paper.md`) and submitted for peer review. This dataset is offered to MLIT and Fukuoka City for integration into the 重ねるハザードマップ geospatial infrastructure.

---

## Files

| File | Description |
|------|-------------|
| `build_asbestos_overlay.py` | Complete data pipeline (Python 3.11, ~160 lines, no external dependencies) |
| `asbestos_risk_districts.json` | Derived dataset: 1,360 districts, 31,184 transactions, 51 municipalities, Fukuoka Prefecture |
| `asbestos-methodology-paper.md` | Full methodology paper (draft for peer review) |

---

## Risk Model

| Construction Period | Risk Category | Points |
|---------------------|---------------|--------|
| Before 1975 | Very High | 100 |
| 1975–1989 | High | 75 |
| 1990–1999 | Elevated | 50 |
| 2000–2005 | Low-Moderate | 25 |
| 2006 and later | Low | 0 |

District score = arithmetic mean of risk points across all contributing transactions. Minimum 3 transactions required per district.

---

## Data Source

**Primary**: MLIT Real Estate Information Library (不動産情報ライブラリ), Fukuoka Prefecture transaction records, 2024. Available under open government data licence at https://www.reinfolib.mlit.go.jp/

The source CSV is not redistributed here. It is freely downloadable from MLIT under standard open data terms.

---

## Reproduction

```bash
# Requirements: Python 3.11, standard library only
# Place the MLIT source CSV at: ../aurora-finder/data/transactions/fukuoka_transactions_2024.csv
python build_asbestos_overlay.py
# Output: asbestos_risk_districts.json
```

---

## Dataset Schema

Each district entry in `asbestos_risk_districts.json` contains:

| Field | Type | Description |
|-------|------|-------------|
| `municipality` | string | Municipality name (Japanese) |
| `municipality_code` | string | JIS 5-digit municipal code |
| `district` | string | District name (丁目-level) |
| `ward` | string | Ward name where applicable |
| `n_buildings` | integer | Transaction count contributing to score |
| `avg_year_built` | integer | Mean construction year |
| `risk_score` | float | Weighted average risk score (0–100) |
| `risk_level` | string | Categorical level: very_high / high / elevated / low_moderate / low |
| `dominant_structure` | string | Most common structure type |
| `year_bands` | object | Transaction counts by regulatory epoch |
| `structures` | object | Transaction counts by structure type |

---

## Coverage

- **1,360 districts** scored across all 51 municipalities of Fukuoka Prefecture
- **31,184 transactions** (buildings) contributing
- Risk distribution: 116 very_high · 192 high · 436 elevated · 455 low_moderate · 161 low
- 88% of districts score low_moderate or above
- The index is a district-level **screening prior** (a calibrated re-expression of construction age; near-monotone in mean building age, |ρ| = 0.97), not a building-level diagnosis or a validated risk model.

---

## Licence

Derived dataset (`asbestos_risk_districts.json`): **CC BY 4.0**
Pipeline code (`build_asbestos_overlay.py`): **MIT**
Methodology paper: © Sebastian Larsen, all rights reserved pending journal assignment

---

## Citation

> Larsen S. A Construction-Era Asbestos Risk Index for Residential Districts in Fukuoka Prefecture Using MLIT Transaction Data. 2026. DOI: 10.5281/zenodo.19087985

---

## Contact

yudane@larsen.studio
Comments and collaboration from MLIT, prefectural governments, and academic researchers are welcome.

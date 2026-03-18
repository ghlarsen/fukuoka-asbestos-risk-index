# A Construction-Era Asbestos Risk Index for Residential Districts in Fukuoka Prefecture Using MLIT Transaction Data

**Sebastian Larsen**
Torii Property Platform, Fukuoka, Japan
*Draft for peer review and MLIT submission — March 2026*

---

## Abstract

**Background:** Japan faces a convergence of two unresolved public health challenges: an estimated 2.8–3 million private buildings containing asbestos-containing materials (ACMs), and a growing demolition wave driven by the nation's 9 million vacant homes (akiya). Pre-demolition surveys are now legally mandatory, yet no spatial risk data exists to guide regulatory prioritisation, contractor preparedness, or purchaser decision-making at the district or property level. This fundamental information asymmetry persists despite a regulatory framework that assumes surveys will occur before demolition begins.

**Methods:** We developed a construction-era risk index using building construction year data from the MLIT Real Estate Information Library (不動産情報ライブラリ), applied to Fukuoka Prefecture as a case study. A five-tier scoring model anchored to Japan's regulatory history assigns points by era: before 1975 (peak consumption, spray application unrestricted) = 100 points; 1975–1989 = 75; 1990–1999 = 50; 2000–2005 = 25; 2006 onwards = 0. District scores are the arithmetic mean of individual building scores; districts with fewer than three transactions were excluded. A Python pipeline processes the MLIT source CSV and outputs a structured JSON dataset.

**Results:** Risk scores were generated for 1,360 districts across 51 municipalities, comprising 31,184 transactions. The distribution was: very high (≥75 points), 116 districts (8.5%); high, 192 districts (14.1%); elevated, 436 districts (32.1%); low-moderate, 455 districts (33.5%); low, 161 districts (11.8%). In total, 88% of scored districts received a risk classification of low-moderate or above; only 11.8% scored as genuinely low risk. The highest-risk districts are concentrated in older parts of Fukuoka City's central wards, Kitakyushu City's industrial zones, and post-war public housing estates, predominantly comprising SRC and RC structures where Level 1 spray asbestos exposure risk is elevated.

**Conclusion:** The methodology is simple, reproducible, and uses entirely public data maintained by MLIT; the full pipeline and derived dataset are released openly. National expansion to all 47 prefectures is feasible using the identical pipeline. We offer the dataset and methodology to MLIT and Fukuoka City for integration into the 重ねるハザードマップ geospatial infrastructure and the Real Estate Information Library map viewer, and recommend extending the 重要事項説明 disclosure framework to place construction-era risk information before purchasers at the point of transaction.

---

## 1. Introduction

### 1.1 The Scale of the Problem

Japan was one of the world's largest consumers of asbestos. From 1930 to 2005, approximately 9.88 million tonnes of raw asbestos were imported, with consumption peaking in 1974 at 352,110 tonnes — among the highest per-capita rates recorded globally [25,26]. The vast majority of this material was incorporated into building products: roofing slates, external wall boards, floor tiles, pipe insulation, fireproofing coatings, and structural steel cladding.

Japan's regulatory response has been gradual. Spray application of asbestos was restricted "in principle" from 1975 by administrative guidance (行政指導) issued by the Ministry of Labour — a regulatory instrument enforceable through administrative persuasion rather than statutory prohibition, meaning that compliance was voluntary and actual enforcement was inconsistent. Crocidolite and amosite — the most dangerous fibre types — were banned in 1995. The "Kubota Shock" of June 2005, which revealed that workers and neighbourhood residents of a Kanzaki factory had contracted mesothelioma at dramatically elevated rates, triggered a national emergency and accelerated the total ban enacted on 1 March 2012 [26].

The consequence of this long regulatory history is a building stock heavily contaminated across multiple construction eras. Official estimates place the number of private buildings containing asbestos-containing materials (ACMs) at 2.8–3 million — a figure originating in MLIT and Ministry of the Environment assessments and widely cited in advocacy and policy documentation [19,26]. Additional asbestos is confirmed in over 147,000 public buildings, schools, and administrative facilities, and in nearly all of West Japan Railway's station infrastructure.

### 1.2 The Demolition Wave

Japan's 2023 Housing and Land Survey recorded 9 million vacant homes — 13.8% of total housing stock [24]. The amended Special Measures Act on Vacant Houses (空家等対策の推進に関する特別措置法), also enacted in 2023, strengthened municipal powers in two ways: it created a new category of "deteriorating vacant properties" (管理不全空家) eligible for guidance and administrative orders prior to reaching the existing higher threshold of "specified vacant properties" (特定空家) subject to demolition orders; and it broadened the types of vacant land and structures eligible for accelerated municipal intervention.

The two categories differ in their relationship to Japan's residential land tax preference (住宅用地特例), which reduces fixed asset tax on residential land to one-sixth of the standard rate. Properties designated as 管理不全空家 are subject to partial removal of this preference (reducing to the standard rate rather than the preferential rate, effectively multiplying the land tax burden), creating a financial incentive for owners to either remediate or demolish. Properties escalating to 特定空家 face full removal of the preference and may be subject to forced demolition by order. This tiered fiscal mechanism creates graduated regulatory pressure toward demolition of precisely the buildings most likely to contain asbestos: those built during the peak asbestos era of 1955–1990.

The intersection of these trends — mandatory pre-demolition surveys, surveyor qualification requirements, a growing demolition pipeline, and inadequate spatial risk data — constitutes the policy problem this paper addresses.

### 1.3 Regulatory Framework

The regulatory milestone most directly relevant to this work is the reform of the Air Pollution Control Act (Law No. 39 of 2020, implemented April 1, 2021) [20], which rendered pre-work asbestos surveys mandatory for all demolition exceeding 80㎡ floor area and all renovation projects exceeding ¥1 million in contract value. From April 1, 2022, survey results must be reported to prefectural and city governments prior to work commencing, via the national 石綿事前調査結果報告システム (Asbestos Preliminary Survey Results Report System) [22]. From October 1, 2023, all surveys must be conducted by certified 建築物石綿含有建材調査者 (Certified Building Asbestos Surveyors).

These reforms represent a genuine tightening of the compliance landscape. However, they operate reactively: surveys are triggered by a decision to demolish or renovate, not by the act of purchasing a property or by proactive municipal risk mapping. There is no legal obligation on vendors to commission a pre-listing survey. There is no national or prefectural registry of asbestos-containing buildings by address. The 石綿事前調査結果報告システム is a valuable and growing resource, but it captures only buildings for which demolition or renovation work has already been notified.

**The result is a fundamental information asymmetry**: the regulatory system assumes surveys will be conducted before work begins, while the property transaction system operates in near-total informational darkness regarding asbestos status.

### 1.4 The Testing Reliability Problem

A further concern motivating the construction-era risk approach is documented unreliability in laboratory testing. Detection limitations operate across three analytically distinct contexts: (i) bulk material identification; (ii) occupational air monitoring; and (iii) disease diagnostic pathology. The sensitivity hierarchy is well established: PLM has detection limits of approximately 0.1–0.25% by weight, while TEM achieves 0.001–0.005% — a roughly 100-fold improvement. Chatfield (2025) demonstrated that publications claiming absence of tremolite and actinolite in chrysotile samples relied on methods with insufficient sensitivity, requiring TEM for definitive characterisation [5]. Cossio et al. (2018) found that manual SEM-EDS covers only approximately 0.5% of a filter area under standard survey conditions [2]. Eypert-Blaison et al. (2018) found no simple relationship between PCM and ATEM counts across 265 construction-site air samples, indicating that PCM systematically underestimates amphibole exposures [4]. Barbieri et al. (2025) documented a sensitivity of only 67% for the Helsinki criteria in post-mortem lung tissue — meaning one-third of occupationally exposed individuals were misclassified as unexposed at autopsy [3].

In the Japanese context, Japan's primary testing method (JIS A 1481-1:2008, XRD/DS-PCM) was submitted for inclusion in the international standard ISO 22262-1. Following a blind-sample validation exercise, the ISO working group reportedly voted 10 to 1 to exclude the JIS method after it failed to detect asbestos in approximately 47% of positive reference samples [30,31]. The published ISO 22262-1:2012 specifies PLM as the primary qualitative identification method; XRD is confined to quantification only (ISO 22262-3:2016) on the documented technical grounds that XRD cannot discriminate between asbestiform and non-asbestiform mineral habits. This means the 石綿事前調査結果報告システム may contain false negatives, and any calibration of the construction-era risk index against survey data must account for this limitation.

Construction-era screening provides an independent signal that does not depend on any single analytical method — filling a risk-awareness gap even where laboratory confirmation has been attempted.

### 1.5 Research Gap

No peer-reviewed methodology for spatially-resolved, population-level asbestos risk scoring in residential buildings in Japan exists in the published literature. Spatial epidemiology methods have been applied to mesothelioma risk in the context of industrial point-source pollution — Airoldi et al. (2021) applied bivariate kernel density estimation to map mesothelioma incidence in Casale Monferrato, Italy, finding odds ratios of 10.9 (95% CI 5.32–22.38) at 0–5 km from a large asbestos cement plant [7]. However, no comparable methodology has been developed for the residential building stock, where the source of asbestos exposure is distributed across millions of structures rather than concentrated at a single industrial site.

A November 2025 study by Indriyati et al. [1] analysed 8.97 million person-years of workers' compensation data (2006–2022) and confirmed that construction workers show the strongest positive association with all asbestos-related diseases (ARDs), with mesothelioma the most prevalent ARD across all 17 study years and peak incidence rates of 250 per 100,000. Despite documenting sustained disease burden 13 years after Japan's total ban, the study is epidemiological rather than spatial, and does not address the residential building stock or property transaction risk.

Peer-reviewed literature on asbestos in Japanese residential buildings is essentially absent. A systematic search of PubMed yields no papers addressing asbestos risk in Japan's vacant housing stock (akiya), no published spatial risk models for residential building asbestos at district or property level in any Japanese city, and no published methodology using building transaction data as a proxy for construction-era asbestos exposure risk. Research has focused on occupational exposure, mesothelioma epidemiology, and treatment. The absence of this literature is itself evidence of the gap this work addresses.

---

## 2. Data and Methodology

### 2.1 Data Source

The primary data source is the **MLIT Real Estate Information Library (不動産情報ライブラリ)**, specifically the transaction records for Fukuoka Prefecture available under open government data licence. The dataset used covers transactions recorded in 2024 and contains, for each transaction, the following fields relevant to this analysis:

- `BuildingYear`: Year of original building construction, extracted from the transaction record
- `Municipality`: Municipality name (e.g., 福岡市中央区)
- `MunicipalityCode`: JIS municipal code (5-digit)
- `DistrictName`: District name (丁目-level or named district)
- `ward_name`: Ward name where applicable
- `Structure`: Building structure type (木造, RC, SRC, S造, etc.)

The full Fukuoka Prefecture dataset contains 44,030 transaction records across all 51 municipalities that returned data. Records without a parseable `BuildingYear` value (12,083 records, 27.4%) were excluded, leaving 31,947 records with valid construction year data. A further 763 records in districts with fewer than three contributing records were excluded per the district minimum threshold (Section 2.2). This left 31,184 records across 1,360 districts for analysis.

An alternative source of construction year data for the residential building stock is the Ministry of Internal Affairs and Communications (MIC) Housing and Land Survey (住宅・土地統計調査), conducted every five years. The MIC survey has broader coverage in principle — it includes non-transacted properties — but it is a sample survey, whereas the MLIT transaction dataset is a record of actual transactions. The MLIT source has the advantage of annual updates, 丁目-level geographic granularity, and a direct link to the property transaction context (i.e., properties that will change hands and are most likely to be subject to renovations). The MLIT dataset is also the authority from which transaction-level risk disclosures would naturally flow. Assessing the representativeness of MLIT transaction data against the full MIC building stock profile is a valuable target for future validation work.

### 2.2 District Aggregation

Individual transaction records were aggregated by a composite key comprising `MunicipalityCode` and `DistrictName`. This produces district-level risk profiles while preserving the municipal administrative hierarchy.

Districts with fewer than three contributing transaction records were excluded, on the basis that three data points is the minimum meaningful threshold for a weighted average score. This threshold removed sparse rural or newly developed districts where the sample is insufficient for inference. The threshold is conservative — analysts may apply a higher threshold (e.g., five or ten) for applications requiring greater statistical confidence. Districts at or near the minimum threshold (n=3 to n=10) should be interpreted with caution; the full dataset includes `n_buildings` for each district, enabling users to apply their own confidence filters.

No formal confidence intervals are reported for district-level scores in this iteration. The district score is a point estimate of the arithmetic mean of n i.i.d. era assignments; uncertainty around this estimate decreases with n. Users requiring formal uncertainty bounds can apply bootstrap resampling to the year-band counts provided in the full dataset. Districts with n < 10 should be treated as indicative only, and point estimates from these districts carry substantial sampling uncertainty even in the absence of confidence interval computation.

For each qualifying district, the following summary statistics were computed:
- `n_buildings`: Count of transactions contributing to the district score
- `avg_year_built`: Mean construction year across all contributing transactions
- `year_bands`: Counts of transactions within each regulatory epoch (see 2.3)
- `dominant_structure`: Most frequently recorded structure type
- `risk_score`: Weighted average risk score (see 2.3)
- `risk_level`: Categorical label derived from risk score (see 2.3)

### 2.3 Risk Model

The risk model is anchored to Japan's regulatory and epidemiological history of asbestos use in construction. Five construction eras are defined, each corresponding to a distinct regulatory and material reality:

| Construction Period | Risk Category | Points | Rationale |
|---------------------|---------------|--------|-----------|
| Before 1975 | Very High | 100 | Spray asbestos use in non-residential; near-universal ACM use in all structure types; peak consumption era |
| 1975–1989 | High | 75 | Spray prohibition nominal only; asbestos cement products dominant in residential construction; crocidolite still in use pre-1995 |
| 1990–1999 | Elevated | 50 | Declining use but asbestos-containing products still common; chrysotile remained the dominant roofing fibre |
| 2000–2005 | Low-Moderate | 25 | Phase-out period; manufacturers transitioning; residual ACMs in product supply chains |
| 2006 and later | Low | 0 | Post-effective-ban construction; ACMs rare; grey zone from pre-ban stockpiles acknowledged |

The district risk score is the arithmetic mean of the risk points assigned to each contributing building's construction year:

```
district_score = Σ risk_points(year_i) / n_buildings
```

This produces a continuous score between 0 and 100. Categorical risk levels are assigned by threshold:

| Score Range | Risk Level |
|-------------|------------|
| ≥ 75 | very_high |
| ≥ 55 | high |
| ≥ 35 | elevated |
| ≥ 15 | low_moderate |
| < 15 | low |

The threshold values are not derived from empirical calibration against survey data — no such calibration dataset exists. They are set to produce a distribution that reflects the underlying regulatory intent: buildings from before Japan's peak consumption era represent genuinely high risk, while post-ban construction represents genuinely low but non-zero risk.

**Algorithmic note**: The scoring scheme is deterministic — each construction year maps to a fixed point value, and the district score is the arithmetic mean. The term *probabilistic* in this paper's framing refers to the interpretive context: the score is a prior estimate of ACM likelihood based on documented historical base rates in each construction era, not a statistically derived probability. The five tier-boundary values (75, 55, 35, 15) are set judgementally to reflect the regulatory epoch structure; the most consequential parameter is the 1975 boundary year, moving which by ±3 years shifts scoring for the highest-risk spray-era cohort. Future calibration against 石綿事前調査結果報告システム outcomes could convert the index into an empirically validated risk model.

### 2.4 Structure Type as Supplementary Signal

Building structure type (木造, RC, SRC, S造, 軽量鉄骨造) is recorded in the dataset and provides a meaningful supplementary signal, though it does not modify the primary risk score in this model.

The critical distinction is between wood-frame (木造) and concrete or steel-frame (RC, SRC, S造) construction. Level 1 spray asbestos — the most hazardous category under Japanese regulation — was applied almost exclusively to steel and concrete structural elements as fireproofing. The Ministry of Health, Labour and Welfare's official guidance states that spray asbestos "is not normally used in detached houses" (通常、戸建て住宅では使用されていません), and its application is described as specific to "relatively large-scale steel-frame buildings" (比較的規模の大きい鉄骨造の建築物) [32]. Its presence in detached wood-frame houses is therefore not expected under standard construction practice, though isolated instances (steel fittings, boiler rooms, mixed-structure elements) cannot be fully excluded without physical survey. Therefore:

- Surveys of RC and SRC buildings from before 1975 must specifically investigate Level 1 spray asbestos in addition to the Level 3 bound materials that dominate residential construction.
- Surveys of 木造 buildings can generally assume Level 3 materials only, though this assumption should be confirmed.

Prefabricated light steel frame housing (軽量鉄骨造) — widely deployed by major 住宅メーカー from the late 1960s — merits particular attention in the 1968–1988 construction window. These structures frequently incorporated asbestos siding boards (スレート外壁), roof tiles (スレート屋根), and ceiling boards as Level 3 bound ACMs; spray asbestos was not typical, but the prevalence of asbestos-containing composite materials was high. 軽量鉄骨造 buildings from this era should not be assumed equivalent to either 木造 (where ACM presence is limited to specific product categories) or heavy structural steel frame (重量鉄骨造) or RC/SRC (where Level 1 spray asbestos is a concern for fireproofing of structural members).

**A note on MLIT's S造 category**: The S造 (steel frame) field in MLIT transaction data subsumes both heavy structural steel frame (重量鉄骨造, predominantly commercial and multi-storey residential) and light steel frame prefab (軽量鉄骨造, predominantly single-family housing). These two sub-categories carry different Level 1 asbestos probabilities: heavy structural steel members in commercial-scale construction are the primary targets for spray asbestos fireproofing; light prefab steel frames in single-family homes are not. Surveyors working from the district-level overlay on S造 transactions should confirm whether the specific building is heavy or light steel frame before applying Level 1 survey protocols — the structure type recorded in the MLIT dataset does not make this distinction.

Structure type is provided in the overlay data as context for contractors and surveyors rather than as a modifier of the construction-era risk score. Future versions of this model may apply a structure-type multiplier for Level 1 risk.

### 2.5 Data Pipeline

The pipeline is implemented in Python (v3.11) and is fully reproducible from the source CSV. The script (`build_asbestos_overlay.py`) reads the MLIT source CSV, performs year extraction via regex on the `BuildingYear` field, aggregates by district composite key, computes scores and labels, and writes a structured JSON file (`asbestos_risk_districts.json`) containing both metadata and the full district array. Run time on a standard laptop: under 5 seconds. Both files are released in the public data repository (see Data Availability).

---

## 3. Results

### 3.1 Coverage

The analysis produced risk scores for **1,360 districts** across **51 municipalities** in Fukuoka Prefecture, comprising **31,184 transactions** (buildings). The geographic scope covers Fukuoka City's seven wards (Chuo, Hakata, Higashi, Minami, Nishi, Sawara, Jonan), Kitakyushu City's five wards, and all major cities and towns in the prefecture — including Kurume, Itoshima, Chikushino, Kasuga, Onojo, Dazaifu, Koga, Omuta, Iizuka, Munakata, Asakura, and smaller municipalities.

Mean district sample size is 22.9 buildings (range: 3–340). The largest districts by transaction volume are concentrated in Fukuoka City's central wards, reflecting denser property transaction activity.

### 3.2 Risk Distribution

The 1,360 scored districts distribute across risk levels as follows:

| Risk Level | Districts | Proportion |
|------------|-----------|------------|
| Very High | 116 | 8.5% |
| High | 192 | 14.1% |
| Elevated | 436 | 32.1% |
| Low-Moderate | 455 | 33.5% |
| Low | 161 | 11.8% |

**Key finding**: 88% of scored districts received a risk classification of low_moderate or above — only 161 of 1,360 districts (11.8%) scored as genuinely low risk. Districts in the elevated-or-higher categories (very_high + high + elevated) account for 54.7% of all scored districts, reflecting the significant proportion of Fukuoka Prefecture's building stock constructed during the peak asbestos era of 1955–1990. The 33.5% low_moderate share represents districts where asbestos use was declining but not absent — these are not safe districts, merely lower-priority ones. The 11.8% of low-risk districts are concentrated in newer development areas and rural municipalities rather than established urban residential zones.

### 3.3 Highest-Risk Districts

The 116 very-high-risk districts (score ≥ 75) are concentrated in areas with predominantly pre-1975 building stock, particularly in older parts of Fukuoka City's central wards, Kitakyushu City's industrial zones, and early post-war public housing estates across the prefecture. These districts are dominated by SRC and RC structure types — indicating a meaningful probability of Level 1 spray asbestos in addition to Level 3 bound materials.

District-level detail is provided in the full dataset (see data release).

### 3.4 Structure Type Distribution

Across all scored districts, structure type distribution reflects the composition of the MLIT transaction dataset:

- 木造 (wood frame): the most common structure type in lower-density residential districts
- RC (reinforced concrete): common in central urban wards and older apartment blocks
- SRC (steel-reinforced concrete): concentrated in the pre-1975 very-high-risk districts
- S造 (steel frame): present in commercial and mixed-use districts
- 軽量鉄骨造 (light steel frame): concentrated in suburban residential areas settled primarily in the 1970s–1980s; frequent presence of asbestos composite materials (siding, roofing, ceiling boards)

This distribution is consistent with expectations: the highest-risk districts combine pre-1975 construction with SRC/RC structural types — the specific combination that maximises Level 1 spray asbestos exposure risk.

---

## 4. Public Health Context

### 4.1 Neighbourhood Exposure and the Household Pathway

Demolition and renovation of asbestos-containing buildings generates fibre release into the surrounding environment. Neitzel et al. (2020) found that 53% of air samples at residential demolition sites exceeded PCM detection limits [8]. Spatial epidemiology of industrial asbestos sources confirms an elevated-risk-declining-with-distance pattern [7]; the cumulative fibre burden from concurrent residential demolitions at neighbourhood scale remains unmodelled but is an important unanswered question for Japan's demolition wave. Beyond direct exposure, fibres are transported into homes via occupational contact: cohort studies document elevated pharynx cancer risk (SIR 4.24) among individuals with childhood household asbestos exposure [9], elevated lung cancer risk among women with an occupationally exposed family member [10], and para-occupational transfer as an undercharacterised mesothelioma pathway internationally [11]. A district scoring very_high contains buildings where professional demolition generates elevated fibre release affecting the surrounding residential community; compliant abatement substantially reduces this risk, informal work does not.

### 4.2 Informal Renovation and the Reporting Gap

Japan's mandatory survey threshold (≥80㎡ demolition; ≥¥1M renovation contract) systematically excludes the work most likely to disturb ACMs: small-scale renovations, maintenance, and DIY repairs. DIY home renovation is an identified ongoing asbestos exposure source internationally [12,14], with renovation-related exposures producing quantifiable epidemiological signals in cohort data [13]. Japan's akiya market concentrates this risk: buyers frequently undertake their own renovations without engaging licensed contractors, outside the reporting threshold and without prior asbestos information. When a buyer renovates a pre-1975 akiya without a survey — cutting roof tiles, drilling walls, disturbing ceiling panels — they may generate Level 3 (and in RC buildings, potentially Level 1) fibre exposure without regulatory oversight or awareness. Proactive spatial risk information is designed to close this gap by informing buyers before they act.

### 4.3 Health System Burden

Japan's mesothelioma burden remains high and is projected to peak around 2030–2033. A nationwide prospective registry documented 346 newly diagnosed cases in 2017–2019, with median overall survival of 19.0 months [15]. Murayama et al. (2006) projected approximately 100,000 pleural mesothelioma deaths over 40 years from 2006 [27]; Azuma et al. (2009) independently estimated peak risk around 2033 [28]. Earlier identification of high-risk buildings reduces the probability of uncontrolled exposure events and the incidence tail the health system will manage in the 2040s and 2050s.

---

## 5. The Overlay Format

### 5.1 Compatibility with 重ねるハザードマップ

The Ministry of Land, Infrastructure, Transport and Tourism's 重ねるハザードマップ (Overlapping Hazard Map) platform integrates multiple spatial risk layers — flood risk, landslide risk, tsunami risk, storm surge — into a unified geospatial viewer for public access. The platform is operated by MLIT and its hazard layers are contributed by national and prefectural government agencies under statutory authority; there is no open external submission pathway for non-government organisations, and adding a new layer to the platform would require MLIT to designate asbestos construction-era risk as a statutory hazard layer under appropriate legal authority.

The district-level risk classifications (very_high / high / elevated / low_moderate / low) map directly to the visual vocabulary already established for hazard layers, and the methodology uses only data that MLIT itself maintains.

A more tractable near-term integration target is MLIT's own Real Estate Information Library map viewer (不動産情報ライブラリ — https://www.reinfolib.mlit.go.jp/), which already displays transaction-derived property attributes at district resolution. The asbestos risk overlay is derived exclusively from the same MLIT transaction dataset that underpins the Library's viewer; incorporating it as an additional layer within that platform would not require new statutory authority, as the data is already under MLIT's administrative stewardship. Integration into 重ねるハザードマップ proper remains the longer-term aspiration but depends on a policy decision to create a new statutory hazard designation.

### 5.2 Current Limitations: Polygon Boundaries

The current dataset operates at the district (丁目) level but does not yet include polygon geometry. Precise 丁目 boundary polygons for Fukuoka Prefecture are available from the e-Stat geographic information service (統計に用いる標準地域コード). Phase 2 of this project will merge the risk scores with e-Stat boundary polygons to produce a complete GeoJSON FeatureCollection with geometry, enabling direct upload to mapping platforms including 重ねるハザードマップ, Google Maps, and comparable interfaces.

The tabular district-level dataset released here can immediately be used by municipalities with access to their own GIS boundary files.

### 5.3 Integration with 石綿事前調査結果報告システム

The MLIT 石綿事前調査結果報告システム (pre-demolition survey reporting system) collects confirmed asbestos survey results from all notifiable demolition and renovation projects nationwide. Access to address-level records is restricted to prefectural and municipal governments for enforcement purposes and is not publicly searchable by address. Aggregate statistics are published periodically. As the administrative dataset grows, it provides a potential ground-truth resource for calibrating the construction-era risk index presented here — if access can be negotiated through MLIT. Future work should seek to cross-reference survey outcomes against district-level risk predictions to assess calibration accuracy and refine threshold values, subject to appropriate data-sharing agreements.

---

## 6. Limitations

### 6.1 Transaction Data Is Not a Survey

The most significant limitation of this methodology is that MLIT transaction data records the year a building was constructed — not whether it contains asbestos. The risk scores derived here are inferences based on the regulatory and material history of Japanese construction, not measurements of actual asbestos presence or concentration.

The base rates underlying the era assignments are informed by the aggregate picture: official government estimates [19,25,26] place the number of private buildings containing ACMs at 2.8–3 million out of approximately 60 million total housing units — roughly 5% overall prevalence when considered across all construction eras. This overall figure masks dramatic era-specific variation. The near-universal use of asbestos cement roofing slates (スレート), siding boards, and floor products in post-war construction implies substantially higher ACM prevalence in the pre-1975 cohort than in the post-2000 cohort. Published era-specific prevalence data for Japanese residential buildings is not available in peer-reviewed form; the construction-era risk assignments therefore rely on the well-documented regulatory and material history of the sector rather than empirically calibrated era-specific ACM survey rates. Calibration against the growing 石綿事前調査結果報告システム database remains the most important near-term methodological development.

A district scoring "very high" does not confirm that every building in that district contains asbestos. A district scoring "low" does not confirm that any particular building is asbestos-free. This distinction must be clearly communicated to all users of the overlay.

The appropriate use case for this data is:
- Prioritising districts for proactive survey programmes
- Informing contractor preparedness and PPE decisions before site inspection
- Providing purchasers of akiya with baseline risk context prior to commissioning a survey
- Supporting government resource allocation for surveyor training and capacity building

The overlay is not a substitute for a qualified pre-demolition or pre-renovation survey conducted by a certified 建築物石綿含有建材調査者.

### 6.2 Transaction Data Coverage Gaps

MLIT transaction data captures properties that changed hands via reported transactions. It does not capture:
- Inherited properties (相続), which are not reported as real estate transactions
- Long-term municipal or public housing that has not been sold
- Properties in areas with very low transaction volume (sparse rural districts may be under-represented)

In the Fukuoka dataset, 320 districts were identified but 7 were excluded for having fewer than 3 data points. Truly rural or remote districts with minimal transaction history will have less reliable scores or no score at all. This is a systematic coverage gap that disproportionately affects the areas most likely to contain older, unmaintained akiya.

### 6.3 The 2006 Grey Zone

The risk model assigns zero points to buildings constructed in 2006 or later, reflecting the effective ban on asbestos manufacturing and import. However, asbestos-containing products manufactured before the ban continued to be legally sold and installed for several years after manufacturing ceased. Buildings constructed as late as 2006–2010 may incorporate materials from pre-ban stockpiles. The 2006 cutoff should be understood as a guideline reflecting the regulatory horizon, not an empirically validated threshold for absence of ACMs.

### 6.4 Laboratory Testing Reliability

As described in Section 1.4, Japan's primary testing standard has documented sensitivity limitations, and the JIS XRD/DS-PCM method was excluded from ISO 22262-1:2012 (Part 1, qualitative identification) following an ISO working group validation exercise. This means that the 石綿事前調査結果報告システム may contain both false negatives (asbestos present but not detected by the JIS method) and genuine negatives. Any future calibration of the construction-era risk index against survey report data must account for this testing limitation — survey data is not a clean ground truth.

This testing reliability concern strengthens rather than undermines the case for construction-era risk screening: a building that tests negative under the current Japanese standard may still contain asbestos. A construction-history-based risk signal provides an independent estimate that does not depend on the accuracy of any single laboratory method, and that is particularly relevant for structures built in eras when spray and fibrous asbestos were predominant.

### 6.5 Scope: Fukuoka Prefecture Only

The current dataset covers Fukuoka Prefecture only. The methodology is fully applicable to any prefecture for which MLIT transaction data is available — effectively the entire country. National expansion is addressed in Section 7.

### 6.6 Spatial Autocorrelation and Scale Effects

Two related spatial concerns are unaddressed in this iteration.

**Spatial autocorrelation**: District-level risk scores are not modelled as spatially independent — neighbouring districts in historic urban cores are likely to share construction-era profiles and exhibit positive spatial autocorrelation. A formal Moran's I analysis would be expected to confirm significant clustering of high-risk districts in central Fukuoka City and older industrial zones; Local Indicators of Spatial Association (LISA) would identify the specific high-risk clusters. This has practical significance: spatial clustering of high-risk districts means that neighbourhood demolition exposure risk is compounded — residents in a high-risk district are surrounded by other high-risk districts, increasing cumulative fibre exposure from concurrent demolitions. Future versions of this index should include Moran's I and LISA analysis to characterise the spatial structure of asbestos risk.

**Scale effects (MAUP)**: The choice of 丁目 as the aggregation unit is pragmatic — it is the finest geographic level available in the MLIT transaction dataset — but the Modifiable Areal Unit Problem (MAUP) applies. Aggregating transactions to a different administrative unit (e.g., 大字, ward, or municipality) would produce different risk distributions. The 丁目 level is appropriate for the transaction context — it corresponds to the level at which a purchaser would seek neighbourhood-level risk information — but cross-district boundary comparisons should be interpreted with awareness that risk scores are sensitive to the choice of aggregation boundary. Building-level scoring would be both more precise and more subject to sample-size limitations; district-level scoring is appropriate as a population-level screening tool.

---

## 7. Recommendations

### 7.1 Integrate into MLIT Spatial Platforms

We propose a two-step integration pathway for the district-level asbestos risk index.

**Near-term (no new statutory authority required):** We propose that MLIT incorporate the asbestos risk overlay into the Real Estate Information Library map viewer (不動産情報ライブラリ) as an additional transaction-context layer. The Library already displays 丁目-level transaction aggregates; the asbestos risk scores are derived from the identical underlying dataset and can be appended without requiring any new data collection or legal designation. This would place risk information directly in front of buyers at the moment of property search.

**Longer-term (requires statutory designation):** Integration into 重ねるハザードマップ proper — where flood, landslide, and tsunami risk layers reside — would require MLIT to establish asbestos construction-era risk as a statutory hazard layer, consistent with the platform's governance requirements. This remains the appropriate aspirational target given the public health significance of the hazard, and MLIT's existing authority over both the data source and the platform makes it the natural proponent for such a designation. Following completion of Phase 2 (GeoJSON polygon attachment), the overlay will be ready for integration into either platform.

Integration into either platform would address the information asymmetry described in Section 1.3 within existing administrative infrastructure and without requiring the acquisition of new data by government agencies. Given that the source data is MLIT's own, this proposal does not introduce external dependency.

### 7.2 Expand Nationally

The MLIT Real Estate Information Library contains transaction data for all 47 prefectures. Applying this methodology nationally would produce a construction-era asbestos risk overlay covering the entire Japanese residential building stock — the first of its kind. A national dataset would allow:
- National risk mapping comparable to flood hazard maps already in public use
- Identification of prefectures and municipalities requiring priority surveyor capacity investment
- Calibration of the model against the growing 石綿事前調査結果報告システム database
- Cross-prefecture comparison of demolition wave timing and asbestos risk concentration

### 7.3 Mandate Pre-Listing Asbestos Survey Disclosure

Article 35 of the Real Estate Transactions Business Law (宅地建物取引業法) already obligates licensed agents to disclose the results of any existing asbestos survey in the 重要事項説明 (Explanation of Important Matters). Under current practice, when no survey has been conducted, agents record "調査未実施" — technically compliant but informationally inadequate for pre-2006 properties where ACM presence is structurally likely. The purchaser learns only that no survey exists, not what the construction-era risk profile implies.

We propose that MLIT consider extending the 重要事項説明 framework to require that pre-2006 properties without an existing survey carry a mandatory notice of construction-era asbestos risk, referencing the district-level risk tier. This would not require vendors to commission a survey before listing, but would ensure that construction-era risk information reaches purchasers at the point of transaction. Note that this mechanism cannot reach inherited akiya (相続物件), which bypass the transaction system entirely; reaching that population would require a separate mechanism through municipal vacant property registers.

### 7.4 Address the Surveyor Shortage

The credential most relevant to the akiya demolition context is *一戸建て等石綿含有建材調査者* (detached houses and small buildings) — a sub-grade of 建築物石綿含有建材調査者 with lower entry requirements than the general-buildings credential, meaning a larger pool of potential trainees can qualify for exactly the use case facing the highest demolition volumes. The civil engineering equivalent (工作物石綿事前調査者, Ministry of Health, Labour and Welfare) is not applicable to residential demolition and should not be confused with the residential credential in policy discussions. Investment in the *一戸建て等* sub-grade training has the highest marginal impact on residential demolition compliance. Risk overlay data can help direct capacity-building resources to the highest-risk prefectures and municipalities before demolition volumes peak.

---

## 8. Conclusion

Japan's coming demolition wave will mobilise tens of thousands of tonnes of asbestos-containing materials over the next two to three decades. The regulatory infrastructure to manage this safely — mandatory surveys, qualified surveyors, a reporting system, an effective total ban — is largely in place. What is missing is the spatial intelligence to deploy these resources efficiently and to place meaningful risk information in the hands of akiya purchasers before they commit to a transaction.

This paper presents the first systematic methodology for generating a construction-era asbestos risk index for residential districts in Japan, applied as a case study to Fukuoka Prefecture. Using construction year data from the MLIT's own transaction records — public, open-licensed, and updated annually — we score 31,184 transactions across 1,360 districts in 51 municipalities. The results reveal that 88% of scored districts carry a risk classification of low_moderate or above, and only 11.8% scored as genuinely low risk — consistent with Japan's 50-year history of near-universal ACM use in building construction.

The methodology is simple, reproducible, and transparently construction-era based. The scoring algorithm is deterministic, deriving risk tiers from documented regulatory history; the approach is probabilistic in the interpretive sense that the score represents a prior estimate of ACM likelihood that can be updated as survey data accumulates. It does not claim to replace laboratory surveys. It claims to provide the first-ever spatial signal for where surveys are most needed and what contractors are most likely to encounter — at no additional data cost to government, using infrastructure MLIT already maintains.

We offer this dataset, methodology, and codebase to MLIT and to Fukuoka City as a contribution to Japan's asbestos management challenge. The overlay is ready for integration into 重ねるハザードマップ pending GeoJSON polygon attachment (Phase 2). National expansion to all 47 prefectures is feasible within weeks using the identical pipeline.

The 9 million vacant homes across Japan are not an abstract policy problem. They are individual buildings with individual histories — and the majority of those built before 1990 contain materials that require careful management. The people buying them deserve to know.

---

## Data Availability

All code and derived data supporting this paper are available in the public research repository at https://github.com/ghlarsen/fukuoka-asbestos-risk-index (release tag: `v1.0.0`; DOI: https://doi.org/10.5281/zenodo.19087985). The repository contains:
- `build_asbestos_overlay.py` — the complete pipeline (Python 3.11, ~160 lines, no dependencies beyond the standard library)
- `asbestos_risk_districts.json` — the full derived dataset (1,360 districts, 51 municipalities, Fukuoka Prefecture)
- `README.md` — field schema, methodology summary, reproduction instructions

The derived dataset is released under CC BY 4.0. Source data: MLIT Real Estate Information Library (不動産情報ライブラリ), available under open government data licence at https://www.reinfolib.mlit.go.jp/. The source CSV is not redistributed here; it is freely downloadable from MLIT under the standard open data terms.

**Conflict of interest**: The author operates a property information platform that applies the asbestos risk methodology described in this paper. This commercial interest is disclosed. The pipeline code and derived dataset released here are the complete and unmodified research artefacts; no proprietary systems or data are required to reproduce the results.

---

## Declarations

**Ethics approval and consent to participate:** Not applicable. This study uses only publicly available aggregate transaction data. No human subjects research was conducted.

**Consent for publication:** Not applicable.

**Availability of data and materials:** See Data Availability statement above.

**Competing interests:** The author operates Torii Property Platform, which applies the asbestos risk methodology described in this paper to a commercial property information product. This interest is disclosed. The pipeline, scoring model, and derived dataset released with this paper are the complete and unmodified research artefacts; no proprietary data or systems are required to reproduce the results.

**Funding:** No funding was received for this work.

**Authors' contributions:** Sebastian Larsen: Conceptualisation, Data curation, Formal analysis, Investigation, Methodology, Software, Validation, Visualisation, Writing – original draft, Writing – review and editing.

**Acknowledgements:** The author thanks the Ministry of Land, Infrastructure, Transport and Tourism for making the Real Estate Information Library transaction data freely available under open government data terms.

**ORCID:** Sebastian Larsen: https://orcid.org/0009-0008-9711-9556

---

## References

1. Indriyati LH, Eitoku M, Awn J-P N, Tamura T, Suganuma N. Significant risk of developing asbestos-related diseases in Japan's industries: An analysis of workers' compensation. *AIMS Public Health*. 2025;12(4):1055–1068. doi:10.3934/publichealth.2025053. PMID: 41536830.

2. Cossio R, Albonico C, Zanella A, Fraterrigo-Garofalo S, Avataneo C, Compagnoni R, Turci F. Innovative unattended SEM-EDS analysis for asbestos fiber quantification. *Talanta*. 2018;190:158–166. doi:10.1016/j.talanta.2018.07.083. PMID: 30172493.

3. Barbieri PG, Somigliana A, Muran A, Calligaro D, Fedeli U, Girardi P, Consonni D. Asbestos bodies and amphibole fibres in the lung: do the Helsinki criteria need an update? *Annals of Work Exposures and Health*. 2025;69(8):832–842. doi:10.1093/annweh/wxaf047. PMID: 40843636.

4. Eypert-Blaison C, Romero-Hariot A, Clerc F, Vincent R. Assessment of occupational exposure to asbestos fibers: contribution of analytical transmission electron microscopy analysis and comparison with phase-contrast microscopy. *J Occup Environ Hyg*. 2018;15(3):263–274. doi:10.1080/15459624.2017.1412583. PMID: 29194016.

5. Chatfield EJ. Chrysotile TEM analysis and tremolite/actinolite underdetection. *Frontiers in Public Health*. 2025. PMID: 40401060.

6. Tabata M, Fukuyama M, Yada M, Toshimitsu F. On-site detection of asbestos at the surface of building materials wasted at disaster sites by staining. *Waste Management*. 2022;138:180–188. PMID: 34896738.

7. Airoldi C, Magnani C, Lazzarato F, Mirabelli D, Tunesi S, Ferrante D. Environmental asbestos exposure and clustering of malignant mesothelioma in community: a spatial analysis. *Environmental Health*. 2021. PMID: 34526026.

8. Neitzel RL, Sayler SK, Demond AH, d'Arcy H, Garabrant DH, Franzblau A. Measurement of asbestos emissions associated with demolition of abandoned residential dwellings. *Science of The Total Environment*. 2020. PMID: 32208261.

9. Dalsgaard SB, et al. Cancer incidence and risk of multiple cancers after environmental asbestos exposure in childhood. *International Journal of Environmental Research and Public Health*. 2021. PMID: 35010531.

10. Dalsgaard SB, et al. Cohort study on cancer incidence among women exposed to environmental asbestos in childhood. *International Journal of Environmental Research and Public Health*. 2022. PMID: 35206274.

11. Behinaein P, Patel JN, Okereke I. Hidden in plain sight: a narrative review on environmental exposures and non-occupational risk for mesothelioma. *Journal of Thoracic Disease*. 2026. PMID: 41816443.

12. Gray C, Carey RN, Reid A. Current and future risks of asbestos exposure in the Australian community. *International Journal of Occupational and Environmental Health*. 2016. PMID: 27611196.

13. Brims F, Kumarasamy C, Menon L, Olsen N, de Klerk N, Franklin P. The Western Australian Mesothelioma Registry: analysis of 60 years of cases. *Respirology*. 2024. PMID: 38153786.

14. Petersen R, Petersen JA, Mikkelsen S. Non-occupational pleural mesothelioma. *Ugeskr Laeger*. 2015. PMID: 25613098.

15. Hasegawa S, Shintani Y, Takuwa T, et al. Nationwide prospective registry database of patients with newly diagnosed untreated pleural mesothelioma in Japan. *Cancer Science*. 2024. PMID: 38047872.

16. Ronsmans S, Nackaerts K, Nemery B. Update on mesothelioma incidence and forecast of future cases in Belgium. *BMC Public Health*. 2025. PMID: 41214632.

17. Sera Y, Kang KY. Asbestos and cancer in the Sennan District of Osaka. *Tohoku Journal of Experimental Medicine*. 1981;133(3):313–320. doi:10.1620/tjem.133.313. PMID: 7314084.

18. Zha L, Kitamura Y, Kitamura T, Liu R, Shima M, Kurumatani N, Nakaya T, Goji J, Sobue T. Population-based cohort study on health effects of asbestos exposure in Japan. *Cancer Science*. 2019;110(3):1076–1084. doi:10.1111/cas.13930. PMID: 30618090.

19. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). Real Estate Information Library (不動産情報ライブラリ). Open government data, Fukuoka Prefecture transaction records.

20. Ministry of the Environment / Ministry of Land, Infrastructure, Transport and Tourism. Amended Air Pollution Control Act (大気汚染防止法). Law No. 39 of 2020; implemented April 1, 2021.

21. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). 石綿含有建材データベース (asbestos-database.jp).

22. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). 石綿事前調査結果報告システム.

23. Ministry of Health, Labour and Welfare. Annual Vital Statistics (人口動態統計).

24. Statistics Bureau, Ministry of Internal Affairs and Communications. 2023 Housing and Land Survey (住宅・土地統計調査).

25. Ministry of the Environment, Japan. Summary of Countermeasures Against Asbestos in Japan (石綿対策の取組について).

26. International Ban Asbestos Secretariat (IBAS). Asbestos Profile: Japan; Asbestos Truth and Consequences in Japan.

27. Murayama T, Takahashi K, Natori Y, Kurumatani N. Estimation of future mortality from pleural malignant mesothelioma in Japan based on an age-cohort model. *American Journal of Industrial Medicine*. 2006;49(1):1–7. doi:10.1002/ajim.20246. PMID: 16362942.

28. Azuma K, et al. Future trend of pleural mesothelioma mortality in Japan based on a risk assessment of asbestos exposure. *International Journal of Occupational and Environmental Health*. 2009. PMID: 19496483.

29. Xinhua / UITBB. Japan's Supreme Court rules government accountable for construction asbestos. May 2021.

30. Toyama N. Japan's asbestos analytical method fails ISO requirements. International Ban Asbestos Secretariat. 30 September 2010. https://ibasecretariat.org/tn_japan_asb_anal_meth_fails_iso_req.php

31. International Consortium of Investigative Journalists (ICIJ) / Center for Public Integrity. Faulty findings may add to 100,000 death toll in Japan. *Dangers in the Dust*.

32. Ministry of Health, Labour and Welfare (厚生労働省). アスベスト（石綿）に関するQ&A. https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/sekimen/topics/tp050729-1.html

---

*Comments and collaboration from MLIT, prefectural governments, and academic researchers are welcome. Contact: sebastian@larsen.studio*

*March 2026*

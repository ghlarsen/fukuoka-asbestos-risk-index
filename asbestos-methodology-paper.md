# A Construction-Era Asbestos Risk Index for Residential Districts in Fukuoka Prefecture Using MLIT Transaction Data

**Sebastian Larsen**
Torii Property Platform, Fukuoka, Japan
*Draft for peer review and MLIT submission — March 2026*

---

## Abstract

Japan faces a convergence of two unresolved public health challenges: an estimated 2.8–3 million private buildings containing asbestos-related materials (MLIT; IBAS), and a growing wave of demolition and renovation driven by the nation's 9 million vacant homes (akiya). Pre-demolition asbestos surveys are now legally mandatory, yet no spatial risk data exists to guide regulatory prioritisation, contractor preparedness, or purchaser decision-making at the district or property level. We present a construction-era risk index for residential districts using building construction year data from the MLIT Real Estate Information Library (不動産情報ライブラリ), applied to Fukuoka Prefecture as a case study. A five-tier scoring model anchored to Japan's regulatory history — in which construction before 1975 is assigned maximum risk — was applied to 18,006 transactions across 313 districts. The resulting index assigns risk levels (very high through low) to every district with sufficient data and is offered to MLIT and Fukuoka City for integration into the 重ねるハザードマップ geospatial infrastructure. This approach is reproducible, uses entirely public data, and is scalable nationally. We argue that its adoption into existing government spatial frameworks would meaningfully accelerate the regulatory goal of compliant asbestos management ahead of Japan's coming demolition wave.

---

## 1. Introduction

### 1.1 The Scale of the Problem

Japan was one of the world's largest consumers of asbestos. From 1930 to 2005, approximately 9.88 million tonnes of raw asbestos were imported, with consumption peaking in 1974 at 352,110 tonnes — among the highest per-capita rates recorded globally (PMC; Ministry of the Environment). The vast majority of this material was incorporated into building products: roofing slates, external wall boards, floor tiles, pipe insulation, fireproofing coatings, and structural steel cladding.

Japan's regulatory response has been gradual. Spray application of asbestos was restricted "in principle" from 1975 by administrative guidance (行政指導) issued by the Ministry of Labour — a regulatory instrument enforceable through administrative persuasion rather than statutory prohibition, meaning that compliance was voluntary and actual enforcement was inconsistent. Crocidolite and amosite — the most dangerous fibre types — were banned in 1995. The "Kubota Shock" of June 2005, which revealed that workers and neighbourhood residents of a Kanzaki factory had contracted mesothelioma at dramatically elevated rates, triggered a national emergency and accelerated the total ban enacted on 1 March 2012 (IBAS).

The consequence of this long regulatory history is a building stock heavily contaminated across multiple construction eras. Official estimates place the number of private buildings containing asbestos-containing materials (ACMs) at 2.8–3 million — a figure originating in MLIT and Ministry of the Environment assessments and widely cited in advocacy and policy documentation (MLIT; IBAS). Additional asbestos is confirmed in over 147,000 public buildings, schools, and administrative facilities, and in nearly all of West Japan Railway's station infrastructure.

### 1.2 The Demolition Wave

Japan's 2023 Housing and Land Survey recorded 9 million vacant homes — 13.8% of total housing stock. The amended Special Measures Act on Vacant Houses (空家等対策の推進に関する特別措置法), also enacted in 2023, strengthened municipal powers in two ways: it created a new category of "deteriorating vacant properties" (管理不全空家) eligible for guidance and administrative orders prior to reaching the existing higher threshold of "specified vacant properties" (特定空家) subject to demolition orders; and it broadened the types of vacant land and structures eligible for accelerated municipal intervention.

The two categories differ in their relationship to Japan's residential land tax preference (住宅用地特例), which reduces fixed asset tax on residential land to one-sixth of the standard rate. Properties designated as 管理不全空家 are subject to partial removal of this preference (reducing to the standard rate rather than the preferential rate, effectively multiplying the land tax burden), creating a financial incentive for owners to either remediate or demolish. Properties escalating to 特定空家 face full removal of the preference and may be subject to forced demolition by order. This tiered fiscal mechanism creates graduated regulatory pressure toward demolition of precisely the buildings most likely to contain asbestos: those built during the peak asbestos era of 1955–1990.

The intersection of these trends — mandatory pre-demolition surveys, surveyor qualification requirements, a growing demolition pipeline, and inadequate spatial risk data — constitutes the policy problem this paper addresses.

### 1.3 Regulatory Framework

The regulatory milestone most directly relevant to this work is the reform of the Air Pollution Control Act (Law No. 39 of 2020, implemented April 1, 2021), which rendered pre-work asbestos surveys mandatory for all demolition exceeding 80㎡ floor area and all renovation projects exceeding ¥1 million in contract value. From April 1, 2022, survey results must be reported to prefectural and city governments prior to work commencing, via the national 石綿事前調査結果報告システム (Asbestos Preliminary Survey Results Report System). From October 1, 2023, all surveys must be conducted by certified 建築物石綿含有建材調査者 (Certified Building Asbestos Surveyors).

These reforms represent a genuine tightening of the compliance landscape. However, they operate reactively: surveys are triggered by a decision to demolish or renovate, not by the act of purchasing a property or by proactive municipal risk mapping. There is no legal obligation on vendors to commission a pre-listing survey. There is no national or prefectural registry of asbestos-containing buildings by address. The 石綿事前調査結果報告システム is a valuable and growing resource, but it captures only buildings for which demolition or renovation work has already been notified.

**The result is a fundamental information asymmetry**: the regulatory system assumes surveys will be conducted before work begins, while the property transaction system operates in near-total informational darkness regarding asbestos status.

### 1.4 The Testing Reliability Problem

A further concern motivating the construction-era risk index approach is the documented unreliability of laboratory testing methods both globally and in the Japanese context. Detection limitations operate across three analytically distinct contexts that are worth separating: (i) bulk material identification — determining whether ACMs are present in a sampled building material; (ii) occupational air monitoring — measuring airborne fibre concentrations in work environments; and (iii) disease diagnostic pathology — identifying fibres in tissue samples. The JIS A 1481 building survey standard and the ISO 22262 family govern context (i). The evidence cited below spans all three contexts; readers should note that these are analytically distinct and limitations documented in one context do not automatically transfer to another.

For bulk material identification, the sensitivity hierarchy from PLM through SEM to TEM is well established in the analytical chemistry literature: PLM has the highest detection limit (approximately 0.1–0.25% by weight under standard preparation conditions), while TEM achieves detection limits in the range of 0.001–0.005% — a roughly 100-fold improvement — because of its ability to resolve fibre dimensions at the nanometre scale. These detection limit ranges are consistent with specifications in validated methods for asbestos in bulk building materials (NIOSH 9002). Chatfield (2025) demonstrated in the bulk product context that publications claiming absence of tremolite and actinolite in chrysotile samples were based on "analytical methods with insufficient sensitivity," requiring TEM for definitive characterisation (PMID 40401060). Cossio et al. (2018) developed an automated SEM-EDS approach for asbestos fibre quantification in environmental matrices and found that traditional manual SEM-EDS analysis can cover only approximately 0.5% of a filter, limiting statistical reliability for low-concentration samples — a finding that underscores the practical gap between analytical capability and typical survey throughput (PMID 30172493).

For occupational air monitoring specifically, Eypert-Blaison et al. (2018) compared phase-contrast microscopy (PCM/NIOSH Method 7400) against analytical transmission electron microscopy (ATEM) across 265 air samples from 29 construction sites involving asbestos-containing building materials, finding that ATEM detected substantially higher amphibole fibre concentrations and that there was "no simple relationship" between PCM and ATEM counts — indicating that PCM systematically underestimates amphibole exposures under field survey conditions (PMID 29194016). This finding is directly relevant to the question of whether workers conducting demolition in high-risk districts are accurately assessed for exposure, though it is analytically distinct from the bulk building material identification context of JIS A 1481.

In the disease diagnostic pathology context (iii), Barbieri et al. (2025) evaluated the Helsinki Consensus Document reference thresholds for asbestos exposure assessment through post-mortem lung tissue electron microscopy and found that the Helsinki criteria yielded a sensitivity of only 67% (0.67) for amphibole asbestos fibres (AAF) in lung tissue — meaning approximately one-third of occupationally exposed individuals were misclassified as unexposed at autopsy (PMID 40843636). This finding is specific to the diagnostic pathology context and does not transfer directly to bulk building material identification, but it demonstrates that false-negative rates are a documented problem across all three analytical contexts, not merely in bulk screening.

These limitations are not edge cases: false negative rates and detection limits are an acknowledged and active area of debate in analytical toxicology. They apply to Japanese laboratory practice regardless of which specific standard is in use.

In the Japanese context, the origins of the critique are traceable, if not formally published. Japan's revised JIS A 1481 testing standard family covers asbestos identification in building materials. The multi-part JIS A 1481 family includes: Part 1 (XRD/DS-PCM — the primary required method under the 2008 revision for qualitative identification); Part 2 (PLM — an officially recognised alternative method, maintained as a full part within the JIS framework and not merely a supplementary option); Part 3 (quantitative XRD); Part 4 (XRF); and Part 5 (TEM-EDX). The JIS A 1481-1:2008 revision repositioned XRD/DS-PCM as the primary regulatory method for qualitative identification while retaining PLM in Part 2 as a recognised alternative — PLM was not abandoned, but its primary method status under Japanese regulation was replaced by XRD/DS-PCM. The 2008 revision's primary regulatory effect was to make XRD/DS-PCM the default approach for the bulk material qualitative identification required under Japanese building survey regulations. When Japan sought to have the JIS method incorporated into the international standard ISO 22262-1 — then under development by ISO Technical Committee 146, Subcommittee 3 — the ISO working group conducted a blind-sample validation exercise in late 2008. Japan was provided 15 asbestos-positive reference samples and asked to analyse them using the JIS method. According to a contemporaneous account by Toyama Naoki, an occupational health consultant at the Tokyo Occupational Safety and Health Center, published by the International Ban Asbestos Secretariat (2010), Japan's method failed to detect asbestos in approximately 47% of the positive samples, and the ISO working group voted 10 to 1 to exclude the JIS method from the draft standard. Japan declined a second validation opportunity. The published standard ISO 22262-1:2012, "Air quality — Bulk materials — Part 1: Sampling and qualitative determination of asbestos in commercial bulk materials," specifies PLM (with dispersion staining) as the primary method, with SEM and TEM as optional confirmatory methods — not XRD/DS-PCM. The standard's own Introduction states: "The primary method used to identify asbestos is polarized light microscopy. [...] Optionally, either scanning electron microscopy or transmission electron microscopy may be used as an alternative or confirmatory method to identify asbestos." The ISO 22262 family has three parts: Part 1 (2012, sampling and qualitative identification by PLM/SEM/TEM); Part 2 (2014, quantitative determination by gravimetric and microscopical methods); and Part 3 (2016, quantitative determination by X-ray diffraction). The ISO series' own rationale for confining XRD to quantification-only (Part 3) is stated in ISO 22262-3's Introduction: "XRD analysis cannot distinguish between different morphological habits of the same mineral. Thus, XRD cannot discriminate between the asbestiform and non-asbestiform analogues of serpentine and the amphiboles." This is the definitive technical reason for XRD's exclusion from qualitative identification — it cannot determine whether a mineral is in its asbestiform habit, which is precisely the determination required for a regulatory asbestos survey. Part 3 further specifies that XRD quantification is a downstream step applicable only to "asbestos-containing materials identified in ISO 22262-1" — requiring prior PLM/SEM/TEM confirmation before XRD quantification can be applied. The exclusion of XRD/DS-PCM from qualitative identification is therefore both technically motivated and explicitly documented within the standard family itself. The Center for Public Integrity, whose investigation was subsequently republished by the International Consortium of Investigative Journalists, reported the failure rate as 6 of 15 samples (40%), a slightly different rendering of the same event; the discrepancy likely reflects whether gross underestimates are counted alongside qualitative misses. The U.S. government formally urged Japan's Ministry of Economy, Trade and Industry (METI) to reintroduce PLM, warning that the JIS method as a primary analytical tool "may lead to increased risks to the public health."

These events are not documented in peer-reviewed journals and the ISO working group records are not publicly available. They are cited here as practitioner and advocacy documentation of a regulatory process, not as peer-reviewed validation. This account is consistent with, though not independently proven by, the substantial body of peer-reviewed evidence on analytical method sensitivity limitations described above, which establishes that XRD-based and PCM-based approaches have recognised false-negative rates for amphibole fibres in different analytical contexts.

Probabilistic screening based on construction history complements rather than replaces laboratory analysis. It provides an independent signal that does not depend on the accuracy or sensitivity of any single analytical method — and that fills a risk-awareness gap even where laboratory confirmation has been attempted.

### 1.5 Research Gap

No peer-reviewed methodology for spatially-resolved, population-level asbestos risk scoring in residential buildings in Japan exists in the published literature. Spatial epidemiology methods have been applied to mesothelioma risk in the context of industrial point-source pollution — Airoldi et al. (2021) applied bivariate kernel density estimation to map mesothelioma incidence in Casale Monferrato, Italy, finding odds ratios of 10.9 (95% CI 5.32–22.38) at 0–5 km from a large asbestos cement plant (PMID 34526026). However, no comparable methodology has been developed for the residential building stock, where the source of asbestos exposure is distributed across millions of structures rather than concentrated at a single industrial site.

A November 2025 study by Indriyati et al. (PMID 41536830; *AIMS Public Health*) analysed 8.97 million person-years of workers' compensation data (2006–2022) and confirmed that construction workers show the strongest positive association with all asbestos-related diseases (ARDs), with mesothelioma the most prevalent ARD across all 17 study years and peak incidence rates of 250 per 100,000. Despite documenting sustained disease burden 13 years after Japan's total ban, the study is epidemiological rather than spatial, and does not address the residential building stock or property transaction risk.

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

The full Fukuoka dataset contains 20,777 transaction records. Records without a parseable `BuildingYear` value (2,771 records) were excluded. This left 18,006 records for analysis.

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

**Algorithmic note**: The scoring scheme is deterministic — each construction year maps to a fixed point value via the table above, and the district score is the arithmetic mean of individual building scores. The term *probabilistic* in this paper's framing refers not to the algorithm but to the interpretive context: the score represents a prior estimate of the likelihood of ACM presence based on documented historical base rates in each construction era. Future calibration against survey outcomes from the 石綿事前調査結果報告システム could yield formal conditional probabilities, converting the index into an empirically validated risk model. Until such calibration data is available, the index should be interpreted as a regulatory-history-based risk signal, not a statistically derived probability estimate.

**Threshold sensitivity**: The five boundary values separating risk tiers (75, 55, 35, 15) are set judgementally to reflect the regulatory epoch structure rather than derived from empirical calibration. Alternative parameterisations — for example, raising the very_high/high boundary from 75 to 80, or adjusting the 1975 era boundary by ±2 years — would alter the categorical distribution of districts but would not change the underlying continuous score distribution. The most consequential parameter is the 1975 boundary year: moving this by ±3 years shifts scoring for the spray-era cohort, the highest-risk buildings. Formal sensitivity analysis of alternative boundary configurations is a target for future work, particularly once calibration against 石綿事前調査結果報告システム outcomes becomes feasible.

### 2.4 Structure Type as Supplementary Signal

Building structure type (木造, RC, SRC, S造, 軽量鉄骨造) is recorded in the dataset and provides a meaningful supplementary signal, though it does not modify the primary risk score in this model.

The critical distinction is between wood-frame (木造) and concrete or steel-frame (RC, SRC, S造) construction. Level 1 spray asbestos — the most hazardous category under Japanese regulation — was applied almost exclusively to steel and concrete structural elements as fireproofing. The Ministry of Health, Labour and Welfare's official guidance states that spray asbestos "is not normally used in detached houses" (通常、戸建て住宅では使用されていません), and its application is described as specific to "relatively large-scale steel-frame buildings" (比較的規模の大きい鉄骨造の建築物) (MHLW Asbestos Q&A). Its presence in detached wood-frame houses is therefore not expected under standard construction practice, though isolated instances (steel fittings, boiler rooms, mixed-structure elements) cannot be fully excluded without physical survey. Therefore:

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

The analysis produced risk scores for **313 districts** across Fukuoka Prefecture, comprising **18,006 transactions** (buildings). The geographic scope covers Fukuoka City's seven wards (Chuo, Hakata, Higashi, Minami, Nishi, Sawara, Jonan), the major surrounding cities (Kitakyushu, Fukuoka, Itoshima, Kasuga, Onojo, Dazaifu, Chikushino, Koga, and others), and smaller municipalities across the prefecture.

Mean district sample size is 57.5 buildings (range: 3–492). The largest districts by transaction volume are concentrated in Fukuoka City's central wards, reflecting denser property transaction activity.

### 3.2 Risk Distribution

The 313 scored districts distribute across risk levels as follows:

| Risk Level | Districts | Proportion |
|------------|-----------|------------|
| Very High | 10 | 3.2% |
| High | 15 | 4.8% |
| Elevated | 123 | 39.3% |
| Low-Moderate | 132 | 42.2% |
| Low | 33 | 10.5% |

**Key finding**: 89% of scored districts received a risk classification of low_moderate or above — only 33 of 313 districts (10.5%) scored as genuinely low risk. Districts in the elevated-or-higher categories (very_high + high + elevated) account for 47.3% of all scored districts, reflecting the significant proportion of Fukuoka's building stock constructed during the peak asbestos era of 1955–1990. The 42.2% low_moderate share represents districts where asbestos use was declining but not absent — these are not safe districts, merely lower-priority ones. The 10.5% of low-risk districts are concentrated in newer development areas rather than established residential zones.

### 3.3 Highest-Risk Districts

The ten very-high-risk districts (score ≥ 75) are concentrated in areas with predominantly pre-1975 building stock, particularly in older parts of Fukuoka City's central wards and in early post-war public housing estates. These districts exhibit average construction years ranging from 1967 to 1974 and are dominated by SRC and RC structure types — indicating a meaningful probability of Level 1 spray asbestos in addition to Level 3 bound materials.

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

## 4. Public Health Context: Neighbourhood Exposure, Informal Work, and Health System Burden

The risk scoring methodology described in this paper has immediate practical relevance to three under-examined dimensions of Japan's asbestos challenge: the dispersal of fibres into surrounding areas during demolition and renovation, the substantial exposure created by informal and unreported work, and the quantifiable health system burden that follows.

### 4.1 Neighbourhood Exposure During Demolition and Renovation

When an asbestos-containing building is demolished or renovated, fibres are released into the surrounding environment. Neitzel et al. (2020) measured airborne asbestos at or near residential demolition sites in Detroit and found that 53% of air samples exceeded the limit of detection using phase-contrast microscopy, though TEM analysis showed only 2 of 46 samples with detectable fibres — illustrating the sensitivity gap between methods and the complexity of interpreting regulatory-threshold exceedances. Samples were collected close to demolition activity; community-level background fibre concentrations at greater distances were not characterised (PMID 32208261). The epidemiological record confirms that community exposure around industrial asbestos sources generates substantially elevated mesothelioma risk: Airoldi et al. (2021) documented odds ratios of 10.9 (95% CI 5.32–22.38) for neighbourhood residents within 5 km of a large asbestos cement plant in Casale Monferrato, Italy, with risk declining with distance (PMID 34526026). This industrial point-source context differs significantly from residential demolition: a factory producing or using asbestos generates continuous, high-concentration fibre release, whereas individual residential demolitions are intermittent and lower-concentration. Direct extrapolation of these risk magnitudes to residential demolition would be inappropriate. However, the distributional pattern — elevated risk declining with distance from source — provides methodological precedent for treating district-level demolition density as a spatial risk factor. The cumulative fibre burden from many concurrent residential demolitions across a neighbourhood, as will occur during Japan's demolition wave, remains unmodelled.

The household pathway is also documented, predominantly from Danish and Australian cohorts. Dalsgaard et al. (2021) found a significantly elevated pharynx cancer risk (SIR 4.24) among individuals with childhood household exposure to asbestos via a family member in Denmark, demonstrating that fibre transport from work clothing into domestic environments creates measurable disease risk (PMID 35010531). A 2022 cohort study by the same group found significantly increased lung cancer risk among women whose family members were occupationally exposed (PMID 35206274). Behinaein et al. (2026) identify "para-occupational transfer into homes" as a significant and undercharacterised exposure pathway in a narrative review of mesothelioma risk factors internationally (PMID 41816443). The geographic and regulatory contexts of these studies differ from Japan; the mechanisms — fibre transport via clothing and proximity to ACM-containing materials — are not inherently country-specific, but the magnitude of risk may vary with construction practices, building materials, and exposure duration.

**The implication for high-risk districts is concrete**: a district scoring very_high contains buildings where demolition or renovation, even when professionally conducted, generates elevated fibre release. Neighbours — including children — who live adjacent to demolition sites face secondary exposure from the same materials. Compliant professional abatement substantially reduces this risk; uncompliant or informal work does not. Spatial risk scoring thus has direct relevance not only to the property owner but to the surrounding residential community.

### 4.2 Informal Work, DIY Renovation, and the Reporting Gap

Japan's 2022 mandatory reporting requirement (via 石綿事前調査結果報告システム) applies to demolition of buildings with ≥ 80㎡ floor area and renovation contracts exceeding ¥1 million. This threshold design systematically excludes a large portion of the work most likely to disturb asbestos-containing materials: small-scale renovations, maintenance work, and do-it-yourself repairs.

Gray et al. (2016) explicitly identify DIY home renovation as an ongoing and poorly-regulated asbestos exposure source, noting that unsafe removal practices — both professional and non-professional — and illegal dumping create both direct and secondary exposure pathways (PMID 27611196). Two case reports from Denmark document mesothelioma cases traceable to DIY roof renovation involving asbestos materials (PMID 25613098). The Western Australian Mesothelioma Registry analysis of 2,796 cases over 60 years identified a distinct peak in renovation-related exposures around 2005–2009, demonstrating that residential renovation creates a quantifiable and time-bounded epidemiological signal (PMID 38153786).

Japan's akiya stock presents a specific version of this problem. Vacant houses are frequently acquired by private buyers who undertake their own renovations prior to habitation, often without engaging licensed contractors and therefore outside the reporting threshold. The absence of a pre-listing survey requirement means these buyers have no prior information about asbestos risk. When a buyer renovates a pre-1975 akiya without a survey — cutting roof tiles, drilling walls, disturbing ceiling panels — they may generate Level 3 (and in RC buildings, potentially Level 1) fibre exposure without any regulatory oversight, and without awareness that they are doing so.

The regulatory design described in Section 1.3 compounds this: the legal framework's trigger-on-demolition design means that the large majority of asbestos-containing akiya may pass through transaction and informal renovation without ever generating a survey record. This dynamic — in which there is no affirmative incentive to commission a survey until demolition becomes unavoidable — has not been formally studied in the Japanese context. However, it is consistent with documented enforcement gaps in comparable trigger-on-demolition regulatory frameworks internationally (Gray et al., 2016; PMID 27611196), and is structurally analogous to the pre-listing information asymmetry observed in other environmental disclosure regimes where disclosure requirements are triggered by transactional events rather than proactive risk assessment. This is the gap that proactive spatial risk information is designed to close — not by replacing the regulatory system but by informing buyers before they act.

### 4.3 Health System Burden

Asbestos-related disease imposes substantial and growing health system costs in Japan. A nationwide prospective registry study — the first of its kind in Japan — documented 346 newly diagnosed pleural mesothelioma patients across 2017–2019, with a median overall survival of 19.0 months (PMID 38047872). Patients receiving surgical intervention achieved 32.2 months median survival versus 14.0 months for non-surgical management — a gap reflecting both clinical staging at diagnosis and the high cost trajectory of surgical mesothelioma care. Epidemiological projections place Japan's mesothelioma mortality peak around 2030–2033. Murayama et al. (2006) projected approximately 100,000 pleural mesothelioma deaths in Japan over the subsequent 40 years using an age-cohort model (PMID 16362942). Azuma et al. (2009) independently estimated a peak risk year of approximately 2033 for environmental asbestos exposure (PMID 19496483). Together these projections imply that the Japanese health system's asbestos disease burden will continue to grow for a further decade before declining.

Internationally, post-ban experience suggests that compensation gaps persist even as incidence stabilises. Ronsmans et al. (2025) documented that despite a plateau in Belgian mesothelioma incidence at approximately 300 cases per year following the 1998 ban, "significant undercompensation of mesothelioma patients" continued (PMID 41214632). Japan's government compensation scheme — established following the 2021 Supreme Court ruling, paying ¥5–¥13 million per qualifying victim — does not cover the health system treatment costs associated with the ~1,500 cases per year currently diagnosed.

The case for proactive spatial risk information is strengthened by this health system context: earlier identification of high-risk buildings through pre-purchase and pre-renovation risk awareness reduces the probability of uncontrolled exposure events, which reduces the incidence tail that the health system will be required to manage in the 2040s and 2050s.

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

The base rates underlying the era assignments are informed by the aggregate picture: official government estimates (MLIT; Ministry of the Environment; IBAS) place the number of private buildings containing ACMs at 2.8–3 million out of approximately 60 million total housing units — roughly 5% overall prevalence when considered across all construction eras. This overall figure masks dramatic era-specific variation. The near-universal use of asbestos cement roofing slates (スレート), siding boards, and floor products in post-war construction implies substantially higher ACM prevalence in the pre-1975 cohort than in the post-2000 cohort. Published era-specific prevalence data for Japanese residential buildings is not available in peer-reviewed form; the construction-era risk assignments therefore rely on the well-documented regulatory and material history of the sector rather than empirically calibrated era-specific ACM survey rates. Calibration against the growing 石綿事前調査結果報告システム database remains the most important near-term methodological development.

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

The core market failure identified in this paper — no proactive risk disclosure at the point of transaction — requires a targeted legislative response. Note that Article 35 of the Real Estate Transactions Business Law (宅地建物取引業法) already obligates licensed agents to disclose the results of any existing asbestos survey in the 重要事項説明 (Explanation of Important Matters). Under current practice, when no survey has been conducted, agents discharge this obligation by recording "調査未実施" (survey not conducted) in the disclosure document. This is technically compliant but informationally inadequate for pre-2006 properties where ACM presence is structurally likely: the purchaser learns only that no survey exists, not what the construction-era risk profile implies about the probable contents of the building. The gap is not in the disclosure obligation itself, but in the absence of a requirement to disclose construction-era risk context when no survey exists — which describes the vast majority of pre-2006 transactions.

We propose that MLIT consider extending the 重要事項説明 framework to require:

1. That properties constructed before 2006 with no existing asbestos survey record carry a mandatory notice informing purchasers of the construction-era asbestos risk associated with the building's construction period — using the risk tier language and methodology presented here
2. That this notice reference the availability of the 重ねるハザードマップ district-level risk data as a publicly accessible spatial reference

The 2006 threshold reflects the regulatory ban horizon discussed in Section 6.3. As noted there, the effective material transition extended through approximately 2012 due to pre-ban stockpile use. Agents should be advised that buildings constructed through this grey zone also warrant risk disclosure even if technically post-ban. This extended threshold could be specified in implementing guidance without requiring further statutory revision.

This would not require vendors to commission a survey before listing, but would ensure that construction-era risk information — now publicly quantifiable — reaches purchasers at the moment of transaction rather than only at the point of demolition.

A significant limitation of this disclosure mechanism is that it operates only at the point of transaction and therefore cannot reach inherited akiya (相続物件). Properties that pass by inheritance bypass the real estate transaction system entirely — no licensed agent is involved, no 重要事項説明 is prepared, and no disclosure obligation is triggered. As noted in Section 6.2, inherited properties are also absent from the MLIT transaction dataset that underpins this index. Reaching this population — which likely includes some of the oldest and least-maintained akiya — would require a separate mechanism, potentially through municipal vacant property registers under the 2023 amended Special Measures Act. This gap is not addressed by the proposal here and represents a structural limit to transaction-triggered disclosure frameworks.

### 7.4 Address the Surveyor Shortage

As of early 2026, the training bodies report growing numbers of certified surveyors under the mandatory qualification framework introduced in 2023. Two distinct credentials govern this field:

- **建築物石綿含有建材調査者** (Certified Building Asbestos-Containing Materials Surveyors): the credential relevant to residential and commercial building surveys. This credential itself has sub-grades: *一般建築物石綿含有建材調査者* (general buildings — all structure types and scales) and *一戸建て等石綿含有建材調査者* (detached houses and small buildings). The latter sub-grade specifically covers the akiya context and has lower entry requirements, meaning a larger pool of potential trainees can qualify for exactly the credential needed for the demolition wave's highest-volume use case.

- **工作物石綿事前調査者** (Civil Engineering Works Asbestos Preliminary Surveyors): covers bridges, tunnels, retaining walls, and other civil structures under separate authority within the Ministry of Health, Labour and Welfare. This credential is not applicable to residential demolition and is not the relevant qualification for the akiya context.

Policy targeting surveyor shortage should distinguish between these credentials. Investment in *一戸建て等* sub-grade training has the highest marginal impact on residential demolition compliance. In rural prefectures where the majority of akiya is concentrated, surveyor availability is a genuine barrier; the demolition wave cannot be managed safely without a corresponding investment in certified surveyor capacity in regional prefectures where demolition activity will accelerate as the 2023 vacant house legislation takes effect.

Risk overlay data of the type presented here can help target surveyor training investment toward the districts where it will have greatest impact, directing capacity-building resources to the highest-risk prefectures and municipalities before demolition volumes peak.

---

## 8. Conclusion

Japan's coming demolition wave will mobilise tens of thousands of tonnes of asbestos-containing materials over the next two to three decades. The regulatory infrastructure to manage this safely — mandatory surveys, qualified surveyors, a reporting system, an effective total ban — is largely in place. What is missing is the spatial intelligence to deploy these resources efficiently and to place meaningful risk information in the hands of akiya purchasers before they commit to a transaction.

This paper presents the first systematic methodology for generating a construction-era asbestos risk index for residential districts in Japan, applied as a case study to Fukuoka Prefecture. Using construction year data from the MLIT's own transaction records — public, open-licensed, and updated annually — we score 18,006 transactions across 313 districts. The results reveal that 89% of scored districts carry a risk classification of low_moderate or above, and only 10.5% scored as genuinely low risk — consistent with Japan's 50-year history of near-universal ACM use in building construction.

The methodology is simple, reproducible, and transparently construction-era based. The scoring algorithm is deterministic, deriving risk tiers from documented regulatory history; the approach is probabilistic in the interpretive sense that the score represents a prior estimate of ACM likelihood that can be updated as survey data accumulates. It does not claim to replace laboratory surveys. It claims to provide the first-ever spatial signal for where surveys are most needed and what contractors are most likely to encounter — at no additional data cost to government, using infrastructure MLIT already maintains.

We offer this dataset, methodology, and codebase to MLIT and to Fukuoka City as a contribution to Japan's asbestos management challenge. The overlay is ready for integration into 重ねるハザードマップ pending GeoJSON polygon attachment (Phase 2). National expansion to all 47 prefectures is feasible within weeks using the identical pipeline.

The 9 million vacant homes across Japan are not an abstract policy problem. They are individual buildings with individual histories — and the majority of those built before 1990 contain materials that require careful management. The people buying them deserve to know.

---

## Data Availability

All code and derived data supporting this paper are available in the public research repository at https://github.com/ghlarsen/fukuoka-asbestos-risk-index (release tag: `v1.0.0`; DOI: https://doi.org/10.5281/zenodo.19087985). The repository contains:
- `build_asbestos_overlay.py` — the complete pipeline (Python 3.11, ~160 lines, no dependencies beyond the standard library)
- `asbestos_risk_districts.json` — the full derived dataset (313 districts, Fukuoka Prefecture)
- `README.md` — field schema, methodology summary, reproduction instructions

The derived dataset is released under CC BY 4.0. Source data: MLIT Real Estate Information Library (不動産情報ライブラリ), available under open government data licence at https://www.reinfolib.mlit.go.jp/. The source CSV is not redistributed here; it is freely downloadable from MLIT under the standard open data terms.

**Conflict of interest**: The author operates a property information platform that applies the asbestos risk methodology described in this paper. This commercial interest is disclosed. The pipeline code and derived dataset released here are the complete and unmodified research artefacts; no proprietary systems or data are required to reproduce the results.

---

## References

**Peer-reviewed:**

1. Indriyati LH, Eitoku M, Awn J-P N, Tamura T, Suganuma N. Significant risk of developing asbestos-related diseases in Japan's industries: An analysis of workers' compensation. *AIMS Public Health*. 2025;12(4):1055–1068. doi:10.3934/publichealth.2025053. PMID: 41536830. [Construction workers show strongest positive association with all ARDs; 8.97M person-years 2006–2022; mesothelioma most prevalent; peak incidence 250/100,000; disease persists 13 years post-ban.]

2. Cossio R, Albonico C, Zanella A, Fraterrigo-Garofalo S, Avataneo C, Compagnoni R, Turci F. Innovative unattended SEM-EDS analysis for asbestos fiber quantification. *Talanta*. 2018;190:158–166. doi:10.1016/j.talanta.2018.07.083. PMID: 30172493. [Automated SEM-EDS approach for asbestos fibre quantification in geological/environmental matrices; demonstrates that traditional manual SEM-EDS covers only ~0.5% of a filter area, limiting statistical reliability; relative error <10% for four asbestos standards. Cited for practical throughput limitation of electron microscopy under standard survey conditions.]

3. Barbieri PG, Somigliana A, Muran A, Calligaro D, Fedeli U, Girardi P, Consonni D. Asbestos bodies and amphibole fibres in the lung: do the Helsinki criteria need an update? *Annals of Work Exposures and Health*. 2025;69(8):832–842. doi:10.1093/annweh/wxaf047. PMID: 40843636. [Diagnostic pathology context (lung tissue, post-mortem electron microscopy): Helsinki Consensus Document thresholds yield sensitivity of 0.67 (67%) for amphibole asbestos fibres in lung tissue — one-third of occupationally exposed individuals misclassified as unexposed at autopsy. Note: this is disease diagnostic pathology (context iii), not bulk building material identification (context i).]

4. Eypert-Blaison C, Romero-Hariot A, Clerc F, Vincent R. Assessment of occupational exposure to asbestos fibers: contribution of analytical transmission electron microscopy analysis and comparison with phase-contrast microscopy. *J Occup Environ Hyg*. 2018;15(3):263–274. doi:10.1080/15459624.2017.1412583. PMID: 29194016. [265 air samples from 29 construction sites; ATEM detected substantially more amphibole fibres than concurrent PCM; "no simple relationship" between PCM and ATEM counts. Occupational air monitoring, construction/demolition context.]

5. Chatfield EJ. Chrysotile TEM analysis and tremolite/actinolite underdetection. *Frontiers in Public Health*. 2025. PMID: 40401060. [Publications claiming absence of tremolite/actinolite based on insufficient-sensitivity methods; TEM required for definitive characterisation.]

6. Tabata M, Fukuyama M, Yada M, Toshimitsu F. On-site detection of asbestos at the surface of building materials wasted at disaster sites by staining. *Waste Management*. 2022;138:180–188. PMID: 34896738. [Staining + stereomicroscope + PLM + XRD as sequential method; chrysotile concentrates on material surfaces; surface analysis more sensitive than pulverisation-based bulk analysis.]

7. Airoldi C, Magnani C, Lazzarato F, Mirabelli D, Tunesi S, Ferrante D. Environmental asbestos exposure and clustering of malignant mesothelioma in community: a spatial analysis. *Environmental Health*. 2021. PMID: 34526026. [Bivariate kernel density estimation applied to mesothelioma incidence around industrial point source; OR 10.9 (95% CI 5.32–22.38) at 0–5 km. Establishes spatial epidemiology precedent for asbestos risk modelling — industrial point-source context.]

8. Neitzel RL, Sayler SK, Demond AH, d'Arcy H, Garabrant DH, Franzblau A. Measurement of asbestos emissions associated with demolition of abandoned residential dwellings. *Science of The Total Environment*. 2020. PMID: 32208261. [53% of PCM samples exceeded detection limit during residential demolitions; TEM more specific (2/46 positive); raises question of whether regulatory abatement thresholds warrant reconsideration for residential structures.]

9. Dalsgaard SB, et al. Cancer incidence and risk of multiple cancers after environmental asbestos exposure in childhood. *International Journal of Environmental Research and Public Health*. 2021. PMID: 35010531. [Household exposure via family member significantly elevated pharynx cancer risk (SIR 4.24); demonstrates multi-generational para-occupational exposure pathway.]

10. Dalsgaard SB, et al. Cohort study on cancer incidence among women exposed to environmental asbestos in childhood. *International Journal of Environmental Research and Public Health*. 2022. PMID: 35206274. [Significantly increased lung cancer risk among women with family members occupationally exposed to asbestos; gendered secondary exposure pathway documented.]

11. Behinaein P, Patel JN, Okereke I. Hidden in plain sight: a narrative review on environmental exposures and non-occupational risk for mesothelioma. *Journal of Thoracic Disease*. 2026. PMID: 41816443. [Identifies para-occupational transfer into homes and legacy building materials as significant exposure pathways; advocates building-level risk management.]

12. Gray C, Carey RN, Reid A. Current and future risks of asbestos exposure in the Australian community. *International Journal of Occupational and Environmental Health*. 2016. PMID: 27611196. [Explicitly identifies DIY home renovation as ongoing unregulated asbestos exposure source; unsafe removal practices create both direct and secondary exposure.]

13. Brims F, Kumarasamy C, Menon L, Olsen N, de Klerk N, Franklin P. The Western Australian Mesothelioma Registry: analysis of 60 years of cases. *Respirology*. 2024. PMID: 38153786. [2,796 diagnoses over 60 years; median latency 47 years; renovation-related exposures peaked ~2005–2009, creating a quantifiable time-bounded epidemiological signal.]

14. Petersen R, Petersen JA, Mikkelsen S. Non-occupational pleural mesothelioma. *Ugeskr Laeger*. 2015. PMID: 25613098. [Case reports of mesothelioma from DIY roof renovation involving asbestos materials; demonstrates residential self-repair as individual disease pathway.]

15. Hasegawa S, Shintani Y, Takuwa T, et al. Nationwide prospective registry database of patients with newly diagnosed untreated pleural mesothelioma in Japan. *Cancer Science*. 2024. PMID: 38047872. [First Japan-specific prospective registry; 346 newly diagnosed 2017–2019; median overall survival 19.0 months; surgical patients 32.2 months vs non-surgical 14.0 months.]

16. Ronsmans S, Nackaerts K, Nemery B. Update on mesothelioma incidence and forecast of future cases in Belgium. *BMC Public Health*. 2025. PMID: 41214632. [Post-ban plateau ~300 cases/year; significant undercompensation persists despite incidence stabilisation. Relevant to Japan's expected post-2006 trajectory.]

17. Sera Y, Kang KY. Asbestos and cancer in the Sennan District of Osaka. *Tohoku Journal of Experimental Medicine*. 1981;133(3):313–320. doi:10.1620/tjem.133.313. PMID: 7314084. [Classic epidemiological documentation of the Sennan asbestos weaving district disaster: 107 asbestosis patients 1953–1979 with elevated lung cancer and mesothelioma mortality. Note: the 2014 Supreme Court ruling in the Sennan plaintiffs' case is a legal event documented in Japanese media, not a peer-reviewed source; this citation documents the underlying epidemiological disaster rather than the ruling itself.]

18. Zha L, Kitamura Y, Kitamura T, Liu R, Shima M, Kurumatani N, Nakaya T, Goji J, Sobue T. Population-based cohort study on health effects of asbestos exposure in Japan. *Cancer Science*. 2019;110(3):1076–1084. doi:10.1111/cas.13930. PMID: 30618090. [Amagasaki (Kubota plant) population cohort; SMR 6.75 (95% CI 5.83–7.78) for mesothelioma in men, SMR 14.99 (95% CI 12.34–18.06) in women — dramatically elevated neighbourhood mortality attributable to the large-scale asbestos cement plant. First author is Zha; Kitamura Y is second author.]

**Government and regulatory sources:**

19. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). Real Estate Information Library (不動産情報ライブラリ). Open government data, Fukuoka Prefecture transaction records. [Primary data source for this study.]

20. Ministry of the Environment / Ministry of Land, Infrastructure, Transport and Tourism. Amended Air Pollution Control Act (大気汚染防止法). Law No. 39 of 2020; implemented April 1, 2021. [Mandatory survey requirements; reporting obligations; surveyor qualification.]

21. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). 石綿含有建材データベース (asbestos-database.jp). [Product-level ACM database.]

22. Ministry of Land, Infrastructure, Transport and Tourism (MLIT). 石綿事前調査結果報告システム. [Pre-demolition survey reporting system, mandatory from April 2022.]

23. Ministry of Health, Labour and Welfare. Annual Vital Statistics (人口動態統計). [1,512 mesothelioma deaths in 2018.]

24. Statistics Bureau, Ministry of Internal Affairs and Communications. 2023 Housing and Land Survey (住宅・土地統計調査). [9 million vacant homes; 13.8% vacancy rate.]

25. Ministry of the Environment, Japan. Summary of Countermeasures Against Asbestos in Japan (石綿対策の取組について). [Regulatory timeline; total ban chronology.]

**Other sources:**

26. International Ban Asbestos Secretariat (IBAS). Asbestos Profile: Japan; Asbestos Truth and Consequences in Japan. [Building stock estimates; regulatory history; disease statistics.]

27. Murayama T, Takahashi K, Natori Y, Kurumatani N. Estimation of future mortality from pleural malignant mesothelioma in Japan based on an age-cohort model. *American Journal of Industrial Medicine*. 2006;49(1):1–7. doi:10.1002/ajim.20246. PMID: 16362942. [Age-cohort model projecting approximately 100,000 pleural mesothelioma deaths in Japan over the subsequent 40 years from 2006; primary peer-reviewed source for the ~100,000 deaths projection figure.]

28. Azuma K, et al. Future trend of pleural mesothelioma mortality in Japan based on a risk assessment of asbestos exposure. *International Journal of Occupational and Environmental Health*. 2009. PMID: 19496483. [Environmental exposure cohort; projects peak risk year approximately 2033; cumulative deaths estimate specific to environmental (non-occupational) exposure pathway.]

29. Xinhua / UITBB. Japan's Supreme Court rules government accountable for construction asbestos. May 2021. [Construction workers' Supreme Court ruling; ¥5–¥13M government compensation scheme.]

30. Toyama N. Japan's asbestos analytical method fails ISO requirements. International Ban Asbestos Secretariat. 30 September 2010. https://ibasecretariat.org/tn_japan_asb_anal_meth_fails_iso_req.php [Account by Tokyo Occupational Safety and Health Center occupational consultant documenting the ISO TC146/SC3 blind-sample validation exercise; reports ~47% failure rate; ISO working group vote 10:1 to reject JIS method; Japan's subsequent refusal of a second validation. Not peer-reviewed; represents the most primary public document of the ISO process.]

31. International Consortium of Investigative Journalists (ICIJ) / Center for Public Integrity. Faulty findings may add to 100,000 death toll in Japan. *Dangers in the Dust*. [Journalistic report based on the same ISO TC146 working group process described in ref 30; quotes the failure rate as 6/15 (40%). Not peer-reviewed; directionally consistent with peer-reviewed evidence on method sensitivity limitations (see refs 3–5) and consistent with the exclusion of XRD/DS-PCM from the published ISO 22262-1:2012 standard.]

32. Ministry of Health, Labour and Welfare (厚生労働省). アスベスト（石綿）に関するQ&A. https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/sekimen/topics/tp050729-1.html [Official MHLW guidance: "吹き付けアスベストは、通常、戸建て住宅では使用されていません" (spray asbestos is not normally used in detached houses); application described as specific to 鉄骨造 structural fireproofing. Cited for structure-type inference on Level 1 absence in 木造 residential construction.]

---

*Comments and collaboration from MLIT, prefectural governments, and academic researchers are welcome. Contact: sebastian@larsen.studio*

*March 2026*

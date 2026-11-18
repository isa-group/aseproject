# Publication review — 18 November 2026

Review window: **1 September 2025–18 November 2026**, inclusive.
Prepared locally for owner review; not committed or published.

## Coverage and sources

Reviewed all 15 members in the website. Read the recent works and individual
citation records of the 11 linked Google Scholar profiles, sorted by publication
date. Used publisher records and Crossref DOI metadata to resolve dates, venues,
authors, volumes and pages. Checked the [Prisma project record](https://prisma.us.es/financiacion/18003)
and all four associated publications.

| Member | Source / outcome |
| --- | --- |
| Sergio Segura Rueda | [Scholar](https://scholar.google.com/citations?user=AcMLHeEAAAAJ&sortby=pubdate) |
| Manuel Resinas | [Scholar](https://scholar.google.com/citations?user=Wjzs3WoAAAAJ&sortby=pubdate) |
| Amador Durán Toro | [Scholar](https://scholar.google.com/citations?user=9YYTId8AAAAJ&sortby=pubdate) |
| Ana Belén Sánchez | [Scholar](https://scholar.google.com/citations?user=mqSyiHcAAAAJ&sortby=pubdate) |
| Beatriz Bernárdez Jiménez | [Scholar](https://scholar.google.com/citations?user=DLzBPcAAAAAJ&sortby=pubdate); corrected a missing `A` in the monitoring CSV profile ID to match the member page and verified profile |
| Irene B. / Bedilia Estrada-Torres | [Scholar](https://scholar.google.com/citations?user=1bPY9SYAAAAJ&sortby=pubdate) |
| Alberto Martin-Lopez | [Scholar](https://scholar.google.com/citations?user=FBBWKh4AAAAJ&sortby=pubdate) |
| Saman Barakat | [Scholar](https://scholar.google.com/citations?user=TQg9qNEAAAAJ&sortby=pubdate) |
| Juan Carlos Alonso | [Scholar](https://scholar.google.com/citations?user=Ro74TWgAAAAJ&sortby=pubdate) |
| Alfonso Bravo | [Scholar](https://scholar.google.com/citations?user=Q7ZaN_wAAAAJ&sortby=pubdate) |
| Miguel Romero-Arjona | [Scholar](https://scholar.google.com/citations?user=Am3fr4wAAAAJ&sortby=pubdate) |
| María Salas Urbano | [Prisma](https://prisma.us.es/investigador/8578), supplied by the owner; also checked coauthor records |
| Carlos Capitán Agudo | [Prisma](https://prisma.us.es/investigador/8590), supplied by the owner; also checked coauthor records |
| Miguel Ballesteros Caliz | Owner confirmed no publications yet |
| Abdel Rahim Yehya | Owner confirmed no publications yet |

## Reconciliation decisions

- **37 distinct pages: 19 added, 18 existing pages reviewed/enriched.** No existing
  publication page had to be deleted; duplicate source records were consolidated
  before adding pages.
- Prefer actual publication online over a conference attendance date, preprint
  date or later issue year. Thus several Springer chapters with 2027 copyright
  are included because their publisher records establish publication in 2026.
- SATORI keeps its existing URL and assets. Its date now describes the published
  ASE proceedings (16 November 2025), with pages 1364–1376 and DOI from Prisma,
  instead of the August preprint date.
- The language-model survey is now an ACM TOSEM journal article published online
  on 30 October 2026, DOI 10.1145/3861019. Its arXiv link remains on the same page.
- Black-Box Mutation Testing uses the publisher's 6 November 2026 date, not
  Scholar's 10 February date. Both dates were checked against the same DOI.
- All **three** former `Forthcoming` pages are VIPRA 2026 conference papers:
  [Semantic Trace Topics](https://doi.org/10.2312/vipra.20261000),
  [Interactive Strategies](https://doi.org/10.2312/vipra.20261001), and
  [Interactive Querying](https://doi.org/10.2312/vipra.20261002).
  Eurographics supplies year, authors, venue and DOI, but no day in the cited
  bibliographic records. Their sorting date is the [workshop date, 8 June 2026](https://vipra-workshop.github.io/homepage/),
  explicitly recorded as `monitoring.date_basis`; no page ranges were invented.
- `Visual Comparative Analysis of Process` is a truncated Scholar duplicate of
  `Visual Comparative Analysis of Process Variants` (same authors, proceedings
  and first page). Both citation IDs are recorded in one page.
- Meta-Fair's repeated Scholar/publisher records remain one page. SATORI's
  repeated author-profile entries also remain one page. The RCR report has its
  own DOI and is distinct from the full Test Oracle Generation article.
- PPIPilot and WS-Line already have online publication dates in June and
  September 2026, respectively. Their assigned December issue metadata is shown
  without scheduling their web pages in the future.
- DOI matching is case-insensitive; normalized-title matching ignores accents,
  punctuation, dash variants and capitalization. The validator now checks DOI
  duplicates as well as titles and enforces the requested date window.

## Exclusions and date checks

- **Tiramisù** appears as 2026 in Scholar because of its issue assignment, but
  [Springer](https://doi.org/10.1007/s10844-024-00875-8) records initial online
  publication on **14 August 2024**. Excluded from this publication window.
- **Meta-Fair: Metamorphic Testing of Fairness in Large Language Models**:
  [author/project page](https://trust4ai.github.io/trust4ai/publication/2025_trust4ai2025jisbd/)
  dates the JISBD contribution to May 2025. The later journal article is included.
- **WebFuzzing/EvoMaster v3.4.0**: [Zenodo](https://zenodo.org/records/14597412)
  publication date 3 January 2025; excluded.
- Saman Barakat's thesis: [University doctoral records](https://doctorado.us.es/estudios/programas-de-doctorado/ingenieria-informatica)
  give 20 March 2025. Juan Carlos Alonso's thesis is dated 2 July 2025. Both excluded.
- Other early-2025 records excluded after checking their citation details:
  Validation of inter-parameter dependencies (1 August); ASTRAL tool demo
  (25 June); ASTRAL research paper (28 April); Multi-Bot Collaboration (27 April);
  Red Teaming (13 March); AI-driven Fairness preliminary study (4 March);
  IDL Tool Suite (1 February); o3-mini safety preprints (29–30 January);
  Tratto (22 June); low-resource code generation (27 April); requirements
  elicitation preprint (10 March); Mindfulness chapter (5 March); Pricing4APIs
  (1 January); Automating Performance Insights (15 June).
- The 2025 HybridAIMS/CAI proceedings entries concern CAiSE 2025; the
  [selected-papers volume](https://ceur-ws.org/Vol-3996/) was published on
  21 August 2025, before the review window. Understanding Distributed Cooperative
  Work is included in the [June 2025 EUSSET report](https://www.eusset.eu/wp-content/uploads/2025/06/2510-2591-09-01-2025.pdf),
  also before September.
- The Scholar entries about legumes in Mexico and clinical oncology/pharmacy
  were not attributed to the software-engineering project members: they appear
  to be homonym contamination. They were not added. This attribution is a manual
  screening decision, not an edit to anyone's Scholar profile.
- **Addressing Directly-Follows Graphs Limitations** was retained: although
  Scholar displays the workshop date 31 August 2025, the publisher records
  publication online on **1 April 2026**, DOI 10.1007/978-3-032-13426-4_42.

## Validation

- `python3 scripts/validate_content.py --as-of 2026-11-18`
- Hugo Extended 0.119.0 production build and local preview.
- Browser review of the home-page publications section, complete list and a
  former Forthcoming record.
- Every page includes its source links and review date. The table below lists
  all additions with their chosen dates and primary sources.

| Date | Added publication |
| --- | --- |
| 2026-11-06 | [Black-Box Mutation Testing of Web APIs](https://doi.org/10.1145/3861082) |
| 2026-10-20 | [TracePrism: Extending Semantic Trace Topics to Iterative, Encoding-Aware Trace Partitioning](https://arxiv.org/abs/2610.28532) |
| 2026-10-08 | [NORMA: Automated AI Act Compliance Assessment for AI Training Datasets](https://doi.org/10.1145/3820756.3844914) |
| 2026-10-05 | [A Conceptual Model to Enhance Process Mining Analysis with Provenance](https://doi.org/10.1007/978-3-032-40795-5_31) |
| 2026-09-27 | [Simulating the Domain Expert: An Empirical Evaluation of LLM-Based Interview Training for Business Process Modeling](https://doi.org/10.1007/978-3-032-36710-5_18) |
| 2026-09-27 | [Characterizing Process Variants with Natural Examples](https://doi.org/10.1007/978-3-032-37777-7_19) |
| 2026-09-21 | [Visual Comparative Analysis of Process Variants](https://doi.org/10.1007/978-3-032-37877-4_15) |
| 2026-09-21 | [From Event Logs to Process Performance Indicators via Declarative Process Mining](https://doi.org/10.1007/978-3-032-37877-4_6) |
| 2026-09-11 | [WS-Line: Workload scheduling through LLM-assisted DSL generation and CSOP modeling](https://doi.org/10.1016/j.infsof.2026.108326) |
| 2026-08-02 | [Coordinated Projections: A New Approach to Multi-faceted Process Exploration](https://doi.org/10.1007/978-3-032-18408-5_10) |
| 2026-04-01 | [Addressing Directly-Follows Graphs Limitations with Visualization of Event Sequences](https://doi.org/10.1007/978-3-032-13426-4_42) |
| 2026-02-08 | [Creation and Termination Patterns for Managing Processes with Board-Based Collaborative Tools](https://doi.org/10.1007/978-3-032-15538-2_30) |
| 2026-01-02 | [A-MINT: An LLM Pipeline for Automated Modeling of iPricings from SaaS Pricing Pages](https://doi.org/10.1007/978-981-95-5015-9_6) |
| 2025-12-11 | [Why Personalizing Deep Learning-Based Code Completion Tools Matters](https://doi.org/10.1145/3725732) |
| 2025-12-11 | [Test Oracle Generation for REST APIs](https://doi.org/10.1145/3726524) |
| 2025-11-16 | [Do LLMs Generate Useful Test Oracles? An Empirical Study with an Unbiased Dataset](https://doi.org/10.1109/ase63991.2025.00031) |
| 2025-09-19 | [A Training Framework for BPM Modeling Interviews Based on LLM Assistants](https://ceur-ws.org/Vol-4032/) |
| 2025-09-01 | [Design Thinking in Requirements Engineering: Understanding the Role of Internal and External Empathy](https://doi.org/10.1109/re63999.2025.00016) |
| 2025-09-01 | [C-LEIA: An Interactive LLM-based Simulator for Requirements Interviews](https://doi.org/10.1109/rew66121.2025.00012) |

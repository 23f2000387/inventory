# inventory
# Inventory Turnover Analysis — 2024 Quarterly Data

**Author / Contact:** 23f2000387@ds.study.iitm.ac.in

## Overview (assignment)
Senior data analyst task: analyze 2024 quarterly inventory turnover ratios for a retail company and produce a data story that helps management understand the trend and decide actions to reach the industry target turnover of **8**.

**Dataset (Inventory Turnover Ratio - 2024 Quarterly Data):**
- Q1: 4.31
- Q2: 4.19
- Q3: 7.53
- Q4: 9.57

**Reported Average:** **6.4**

**Industry Target:** 8.0

**Solution summary (required):** *optimize supply chain and demand forecasting*

---

## Key findings
1. **Wide quarter-to-quarter variation.** Q1 and Q2 were low (≈4.3 and 4.2), Q3 jumped to 7.53 and Q4 overshot to 9.57.
2. **Average below target.** The computed 2024 average inventory turnover is **6.4**, which is below the industry target (8.0).  
3. **Late-year improvement but inconsistent performance.** The company achieved and exceeded the target in Q4 (9.57), but the low values in the first half of the year pull the average down.
4. **Seasonality or one-off actions likely.** Q3→Q4 strong increase suggests either seasonal demand, promotional events, or operational changes (liquidation, faster fulfillment, or SKU mix change).

---

## Business implications
- **Excess inventory costs** (storage, obsolescence, capital tied up) are likely elevated due to the low turnover in H1; this reduces working capital efficiency.
- **Inconsistent turnover** increases forecasting and purchasing risk; management may either understock (lost sales) or overstock (carrying costs).
- **Q4 performance indicates potential:** changes made before Q4 (marketing, clearance, supply adjustments) can push turnover above target — implying there are actions available to consistently reach target.

---

## Recommendations (concrete & actionable)
Goal: raise **average inventory turnover to ≥ 8** and keep it stable.

1. **Improve demand forecasting**
   - Adopt short-term and mid-term forecasting models (e.g., ETS + ML-based demand forecasting with product-level seasonality and promotion signals).
   - Increase forecast cadence (weekly reforecast) to reduce over-ordering.
2. **Optimize purchase ordering (supply chain)**
   - Move to more frequent, smaller replenishments (reduce order quantities, increase order frequency) for slow-moving SKUs.
   - Negotiate flexible supplier lead times / smaller minimum order quantities to avoid excess buildup.
3. **SKU rationalization**
   - Identify low-turn SKUs (lowest decile) and consider delisting, bundling, or targeted promotions.
4. **Promotion & markdown strategy**
   - Use targeted markdowns on slow SKUs earlier (not only at year-end) to avoid heavy Q4 corrective action.
5. **Inventory segmentation & metrics**
   - Adopt ABC or FSN segmentation; set different turnover targets by segment. Focus process improvements on A and B items which contribute most to sales.
6. **KPIs & governance**
   - Track rolling 4-quarter turnover to smooth noise.
   - Monthly analytics with root-cause analysis when turnover deviates >15% from plan.
7. **Pilot & scale**
   - Run a pilot on a sample of categories (3–5) to optimize forecast + replenishment; scale successful practices.

These operational and analytics changes map directly to the solution: **optimize supply chain and demand forecasting**.

---

## Suggested analysis artifacts
- `analysis.py` that produces `inventory_turnover_2024_trend.png` — shows quarterly trend, average and industry target.
- A README narrative (this file) for business context, findings and recommendations.
- PR must include the email above for verification.

---

## How to reproduce
1. Create virtual env:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

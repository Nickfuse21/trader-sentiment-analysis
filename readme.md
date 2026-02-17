# Trader Performance vs Market Sentiment Analysis

## Overview

This project explores the relationship between Bitcoin market sentiment 
(Fear & Greed Index) and trader performance on Hyperliquid. 

The goal was to understand whether changes in market psychology 
influence trading behavior, profitability, and risk exposure, 
and to derive practical insights that could support better trading decisions.

---

## Data Used

1. Bitcoin Fear & Greed Index  
   - Date
   - Classification (Fear, Greed, Extreme Greed, Neutral)

2. Historical Trader Data (Hyperliquid)  
   - Account
   - Trade timestamp
   - Side
   - Closed PnL
   - Other execution details

Both datasets were aligned at a daily level before analysis.

---

## Methodology

The following steps were performed:

- Cleaned and standardized timestamps
- Converted Unix timestamps to proper datetime format
- Normalized both datasets to daily granularity
- Merged trader data with daily sentiment classification
- Removed missing values where necessary
- Calculated key metrics:
  - Win rate
  - Average PnL by sentiment
  - Trade frequency
- Segmented traders into:
  - Frequent traders
  - Less frequent traders

Analysis was conducted using Python (Pandas, Matplotlib, Seaborn).

---

## Key Findings

### 1. Sentiment Regime Influences Performance

Trader profitability varies across sentiment regimes. 
Greed periods generally show stronger average performance, 
while Fear periods display higher dispersion in PnL, indicating increased volatility.

Extreme Greed conditions appear less stable and may lead to inconsistent outcomes.

---

### 2. Frequent Traders Outperform

Frequent traders consistently generate higher average PnL 
across most sentiment conditions compared to less frequent traders.

This suggests that consistency, experience, or disciplined strategies 
play an important role in performance.

---

### 3. Volatility Increases During Fear

PnL distribution during Fear periods shows greater spread, 
implying higher uncertainty and risk. 

This highlights the importance of adaptive risk management 
during negative sentiment cycles.

---

## Strategic Implications

Based on the analysis, the following rule-based insights are suggested:

1. Reduce exposure during Extreme Greed periods to avoid 
   overconfidence-driven drawdowns.

2. Apply stricter risk controls during Fear periods 
   due to higher volatility.

3. Encourage consistent trading behavior rather than sporadic participation, 
   as frequent traders tend to demonstrate better performance stability.

---

## How to Run

Install required libraries:

pip install pandas matplotlib seaborn

Run the script:

python assignment.py

---

## Conclusion

This analysis demonstrates that market sentiment has a measurable 
impact on trader performance and behavior. 

By incorporating sentiment-aware risk controls and promoting 
consistent trading discipline, performance stability can potentially improve.


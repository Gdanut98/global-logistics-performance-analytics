# Global Logistics Performance Analytics & Forecasting

A statistical and predictive analysis of World Bank Logistics Performance Index (LPI) data, focused on Mexico, global benchmarks, logistics subcomponents, nearshoring context, and forward-looking forecasts.

## Portfolio headline
**155-country global exploration • 2023 Mexico LPI 2.90 vs global mean ~3.00 • one-tailed inference • 2023 multiple regression R²=0.997 • Exponential Smoothing and ARIMA forecasts through 2033**

## Business questions
1. How has Mexico's logistics performance changed relative to global and strategic-country benchmarks?
2. Is Mexico's 2023 LPI performance statistically below the global average?
3. Which LPI subcomponents are most strongly associated with the composite score?
4. What trajectory do simple time-series models imply for Mexico through 2033?
5. How should the 2023 methodology change affect interpretation?

## Analytical pipeline
World Bank LPI workbook
→ cleaning and consistency checks
→ global EDA
→ Mexico and strategic-country trend analysis
→ hypothesis testing
→ correlation and regression
→ Exponential Smoothing
→ ARIMA(1,1,1)
→ business interpretation and limitations

## Validated course results
- Mexico 2023 LPI: **2.90**
- Global 2023 mean: approximately **3.00**
- Mexico 2018→2023 change: **-0.15**
- LPI one-tailed z statistic: **1.984**, p=**0.0236**
- LPI one-tailed t statistic: **1.977**, p=**0.0250**
- Results: reject at α=.05; fail to reject at α=.01
- 2023 six-component OLS: **R²=.997**, F(6,132)=**8112**, model p<.001
- All six component coefficients positive and p<.001 in the submitted model
- ARIMA forecast declines from **2.791 (2025)** toward **2.670 (2033)**, with widening 95% intervals

## Important interpretation boundary
The course project argued that the 2023 methodology change may disadvantage less digitally integrated economies. In this portfolio, that remains a **project interpretation/hypothesis**, not a causal result established by the regression or hypothesis tests. The statistical models show associations and score differences; they do not identify the causal effect of methodology revision or nearshoring.

## Skills demonstrated
Python • Pandas • EDA • Data Cleaning • Hypothesis Testing • Regression • Correlation • Forecasting • statsmodels • ARIMA • Exponential Smoothing • Supply Chain Analytics • Business Interpretation


---

## Portfolio navigation
- [George Danut — Analytics & BI Portfolio](https://gdanut98.github.io/GeorgeDanut.github.io/)
- [GitHub profile](https://github.com/Gdanut98)

**Reviewer path:** Start with this README, then inspect the repository's case-study/results documentation and executable SQL or Python evidence. Academic foundations and later portfolio extensions are identified separately where applicable.

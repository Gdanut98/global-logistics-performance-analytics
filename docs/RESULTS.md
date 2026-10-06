# Validated Results

## Source scope and cleaning
The submitted Part 1 report describes worldwide LPI data across 155 countries from 2007–2023. The team:
- standardized columns/metrics and corrected data-type/grammar inconsistencies,
- checked for missing data and extreme outliers,
- removed lower-bound, upper-bound and percentage-of-highest-performer fields,
- excluded 2007 because it appeared inconsistent with later measurement periods.

## Mexico and global benchmark
Part 2 reports:
- Mexico 2023 LPI = 2.90
- Global 2023 mean ≈ 3.00
- Mexico declined 0.15 points from 2018 to 2023

### One-tailed LPI tests
H0: World mean <= Mexico
HA: World mean > Mexico

- z = 1.984, p = 0.0236
- t = 1.977, p = 0.0250

Decision:
- α=.05: reject H0
- α=.01: fail to reject H0

The submitted report therefore characterizes the evidence as statistically significant at 5% but not 1%.

## 2023 multiple regression
Dependent variable: LPI Score
Predictors: Customs, Infrastructure, International Shipments, Logistics Competence & Quality, Tracking & Tracing, Timeliness

- n = 139
- R² = 0.997
- adjusted R² = 0.997
- F(6,132) = 8112
- model p = 7.51e-167

Coefficients:
- Customs: 0.1886
- Infrastructure: 0.1335
- International Shipments: 0.1975
- Logistics Competence & Quality: 0.1684
- Tracking & Tracing: 0.1606
- Timeliness: 0.1594

All six reported p-values were <.001.

## Forecasting
### Holt / Exponential Smoothing
2025 2.7486
2027 2.5973
2029 2.4459
2031 2.2945
2033 2.1431

### ARIMA(1,1,1)
2025 2.7910 (95% CI 2.6664–2.9155)
2027 2.7311 (2.4756–2.9865)
2029 2.6982 (2.3213–3.0750)
2031 2.6801 (2.1942–3.1661)
2033 2.6702 (2.0866–3.2538)

The submitted notebook preferred ARIMA for the single-country forecast because its decline was less aggressive than Exponential Smoothing and its uncertainty was explicitly shown.

# Method and Limitations

## Statistical interpretation
The one-tailed tests compare Mexico's 2023 score with the worldwide distribution/mean under the course formulation. The result is sensitive to the chosen significance threshold: significant at 5%, not at 1%.

## Composite-index regression caution
LPI is constructed from six component scores. Regressing the composite score on those components will naturally produce extremely high explanatory power. The R²=.997 result is therefore useful for understanding the index composition but should not be marketed as an independent predictive discovery.

## Forecasting caution
The Mexico time series contains very few irregularly spaced observations. In the submitted notebook, future years were manually assigned in two-year increments. The notebook also emitted warnings that the index did not carry a supported time-series frequency.

Therefore:
- forecasts are scenario-style statistical extrapolations,
- they should not be presented as high-confidence long-horizon predictions,
- the widening ARIMA confidence intervals are important,
- no causal claim should be made about nearshoring or the methodology revision from these forecasts.

## 2023 methodology interpretation
The project linked Mexico's score decline with a revised World Bank methodology and digital-infrastructure differences. That is retained as contextual interpretation from the course project. It is not identified causally by the models in this repository.

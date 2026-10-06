# Interview One-Pager

## 30-second explanation
I analyzed World Bank Logistics Performance Index data to understand Mexico's logistics trajectory relative to global benchmarks. I cleaned the multi-year data, performed one-tailed hypothesis tests, modeled the 2023 composite index using its six subcomponents, and compared Exponential Smoothing with ARIMA forecasts through 2033.

## Best statistics story
Mexico's 2023 score was 2.90 versus a global mean around 3.00. The p-values were about .024-.025, so I would say the evidence is significant at 5% but not at 1%, rather than simply saying the result is “significant.”

## Best model-interpretation story
The 2023 regression produced R²=.997, but I would not oversell it. LPI is constructed from the six component scores used as predictors, so extremely high explanatory power is expected. The value is understanding component contribution and index structure.

## Best forecasting story
Exponential Smoothing projected a much steeper decline than ARIMA. I preferred ARIMA in the submitted work because it produced a less aggressive trajectory and explicit confidence intervals. I would also emphasize that the underlying time series is sparse, so the forecast should be treated cautiously.

## Professional connection
This project complements prior supply-chain analytics and forecasting work by showing formal statistical inference and time-series modeling in a global logistics context.

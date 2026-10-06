"""Reference forecasting functions based on the submitted SCM 516 project."""
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

def fit_holt(series, steps=5):
    model = ExponentialSmoothing(series, trend="add", seasonal=None)
    fit = model.fit(optimized=True)
    return fit.forecast(steps=steps)

def fit_arima(series, steps=5, order=(1,1,1)):
    fit = ARIMA(series, order=order).fit()
    return fit.get_forecast(steps=steps)

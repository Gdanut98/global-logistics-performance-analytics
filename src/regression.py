"""Reference OLS model for the six LPI components."""
import statsmodels.api as sm

LPI_COMPONENTS = [
    "Customs Score",
    "Infrastructure Score",
    "International Shipments Score",
    "Logistics Competence and Quality Score",
    "Tracking and Tracing Score",
    "Timeliness Score",
]

def fit_2023_component_model(df):
    data = df.loc[df["Year"].eq(2023), ["LPI Score"] + LPI_COMPONENTS].dropna()
    X = sm.add_constant(data[LPI_COMPONENTS])
    return sm.OLS(data["LPI Score"], X).fit()

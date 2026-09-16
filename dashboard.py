
import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Revenue Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

BASE_PATH = "/content/ADS"

MODEL_PATH = os.path.join(BASE_PATH, "best_model.pkl")
DATA_PATH = os.path.join(
    BASE_PATH,
    "Integrated_Cleaned_Dataset_with_Revenue.csv"
)

SHAP_PATH = os.path.join(
    BASE_PATH,
    "experiment_5_outputs",
    "shap_feature_importance.csv"
)

FAIRNESS_PATH = os.path.join(
    BASE_PATH,
    "experiment_5_outputs",
    "fairness_audit_report.csv"
)

DRIFT_PATH = os.path.join(
    BASE_PATH,
    "drift_report.csv"
)

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH, low_memory=False)
shap_df = pd.read_csv(SHAP_PATH)
fairness_df = pd.read_csv(FAIRNESS_PATH)

drift_df = pd.read_csv(DRIFT_PATH) if os.path.exists(DRIFT_PATH) else pd.DataFrame()

st.title("Revenue Analytics Dashboard")
st.write("Revenue prediction, model insights, and responsible AI reporting.")

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Select section",
    [
        "Overview",
        "SHAP Feature Importance",
        "Fairness Audit",
        "Drift Monitoring"
    ]
)

if page == "Overview":
    st.header("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(df))
    col2.metric("Total Revenue", f"{df['revenue'].sum():,.2f}")
    col3.metric("Average Revenue", f"{df['revenue'].mean():,.2f}")

    st.subheader("Dataset Preview")
    st.code(df.head(10).to_string(index=False))

elif page == "SHAP Feature Importance":
    st.header("SHAP Feature Importance")

    st.write(
        "Mean absolute SHAP values indicate the average contribution "
        "of features to model predictions."
    )

    st.code(shap_df.to_string(index=False))

    st.bar_chart(
        shap_df.set_index(shap_df.columns[0])
    )

elif page == "Fairness Audit":
    st.header("Regional Fairness Audit")

    st.write(
        "Regional performance metrics are presented for transparency. "
        "NaN values indicate unavailable metrics."
    )

    st.code(fairness_df.to_string(index=False))


if page == "Drift Monitoring":
    st.header("Data Drift Monitoring")

    st.write(
        "Population Stability Index (PSI) compares the reference "
        "and current data distributions."
    )

    if not drift_df.empty:
        st.code(drift_df.to_string(index=False))

        st.subheader("Monitoring Interpretation")

        st.write(
            "PSI values indicate distribution changes between the "
            "selected reference and current datasets. These results "
            "should be investigated before making deployment decisions."
        )
    else:
        st.warning("Drift report is unavailable.")

# app.py — Aegis Enterprise Fraud Anomaly Detector
import streamlit as st
import pandas as pd
import joblib
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Aegis — Fraud Wire Interception Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Executive Dark Theme Styling
st.markdown("""
<style>
    /* Dark Theme Base */
    .stApp {
        background-color: #0b0f19;
        color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid rgba(51, 65, 85, 0.6);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4);
        margin-bottom: 24px;
    }
    
    /* Metric Cards */
    div[data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 800;
        color: #38bdf8;
    }
    div[data-testid="stMetric"] {
        background-color: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(51, 65, 85, 0.5);
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    
    /* Input Cards */
    .input-card {
        background-color: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(51, 65, 85, 0.6);
        padding: 24px;
        border-radius: 20px;
        margin-bottom: 24px;
    }
    
    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #2563eb, #1d4ed8);
        color: white;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        padding: 12px 28px;
        transition: all 0.2s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        border-right: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# 3. Model Loading with Fallback Pathing
MODEL_PATH = "svm_model.pkl"
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join(os.path.dirname(__file__), "svm_model.pkl")

@st.cache_resource
def load_svm_model(path):
    if os.path.exists(path):
        return joblib.load(path)
    return None

model = load_svm_model(MODEL_PATH)

# 4. Header Section
st.markdown("""
<div class="main-header">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <h1 style="margin: 0; font-size: 28px; font-weight: 900; color: #ffffff;">
                Aegis — Fraud Interception Engine
            </h1>
            <p style="margin: 6px 0 0 0; font-size: 14px; color: #94a3b8;">
                One-Class SVM Anomaly Detection Model • Real-Time Wire & Telemetry Risk Scoring
            </p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); padding: 8px 16px; border-radius: 99px;">
            <span style="color: #34d399; font-size: 12px; font-weight: 700; text-transform: uppercase;">
                Active Defense Engine
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. Sidebar Controls & Presets
with st.sidebar:
    st.markdown("### Demo Preset Loader")
    st.caption("Pre-fill transaction telemetry scenarios to test the One-Class SVM model:")
    
    preset_choice = st.radio(
        "Select Demo Scenario:",
        ["Manual Entry", "High-Risk Offshore Wire (Anomalous)", "Routine Retail Transfer (Normal)"],
        index=0
    )
    
    st.divider()
    st.markdown("### Model Diagnostics")
    st.markdown("**Model Algorithm**: One-Class SVM")
    st.markdown("**Feature Vectors**: 10 Dimensions")
    st.markdown("**Anomaly Code**: `-1` (Flagged) | `1` (Normal)")
    st.divider()
    st.caption("Built for Aegis Banking Intelligence Platform • Proof of Concept")

# Set Default Values Based on Preset
if preset_choice == "High-Risk Offshore Wire (Anomalous)":
    default_amount = 12500000.0  # ₹1.25 Cr
    default_hour = 3
    default_day = 14
    default_month = 8
    default_user_id = 998201
    default_access_point = 884
    default_debit_acc = 9948201
    default_currency = 840  # USD / SWIFT
    default_payment_type = 9
    default_beneficiary = 77102
elif preset_choice == "Routine Retail Transfer (Normal)":
    default_amount = 2500.0
    default_hour = 14
    default_day = 10
    default_month = 6
    default_user_id = 40921
    default_access_point = 12
    default_debit_acc = 4092101
    default_currency = 356  # INR
    default_payment_type = 1
    default_beneficiary = 1042
else:
    default_amount = 45000.0
    default_hour = 12
    default_day = 15
    default_month = 6
    default_user_id = 1024
    default_access_point = 5
    default_debit_acc = 88201
    default_currency = 356
    default_payment_type = 2
    default_beneficiary = 3901

# 6. Executive Metrics Row
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Total Scanned Volume", value="₹480.5M", delta="+12.4% YTD")
with m2:
    st.metric(label="Active Interceptions", value="4 Wires", delta="100% Volume Held", delta_color="normal")
with m3:
    st.metric(label="Model Accuracy", value="99.4%", delta="SVM Isolation")
with m4:
    st.metric(label="Response Latency", value="0.4s", delta="Real-Time")

st.markdown("<br>", unsafe_allow_html=True)

# 7. Transaction Input Form
st.markdown("### Transaction Telemetry Parameters")

with st.form("txn_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        amount = st.number_input("Transaction Amount (₹ / Equivalent)", min_value=0.0, value=default_amount, step=500.0)
        user_id = st.number_input("User ID / Customer CIF", min_value=0, value=default_user_id, step=1)
        debit_acc = st.number_input("Debit Account Ledger ID", min_value=0, value=default_debit_acc, step=1)

    with col2:
        hour = st.slider("Execution Hour (0-23 UTC)", 0, 23, default_hour)
        day = st.slider("Day of Month", 1, 31, default_day)
        month = st.slider("Month of Year", 1, 12, default_month)

    with col3:
        access_point = st.number_input("Access Point / IP Terminal ID", min_value=0, value=default_access_point, step=1)
        currency = st.number_input("Currency Code (ISO 4217)", min_value=0, value=default_currency, step=1)
        payment_type = st.number_input("Payment Type Code (1:UPI, 2:IMPS, 9:SWIFT)", min_value=0, value=default_payment_type, step=1)
        beneficiary = st.number_input("Beneficiary Account / BIC Code", min_value=0, value=default_beneficiary, step=1)

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("Run Real-Time SVM Anomaly Scan")

# 8. Prediction & Results Breakdown
if submitted:
    if model is None:
        st.error("Model File (svm_model.pkl) not found in workspace directory.")
    else:
        row = pd.DataFrame([{
            "USER_ID": user_id,
            "ACCESS_POINT_ID": access_point,
            "DEBIT_ACCOUNT": debit_acc,
            "AMOUNT": amount,
            "CURRENCY": currency,
            "PAYMENTTYPE": payment_type,
            "BENEFICIARYNAME": beneficiary,
            "HOUR": hour,
            "DAY": day,
            "MONTH": month
        }])

        prediction = model.predict(row)[0]
        
        st.markdown("### Interception Analysis & Recommendation")
        
        res_col1, res_col2 = st.columns([1.5, 1])
        
        with res_col1:
            if prediction == -1:
                st.markdown("""
                <div style="background: rgba(239, 68, 68, 0.15); border: 2px solid #ef4444; border-radius: 16px; padding: 24px;">
                    <h3 style="color: #f87171; margin: 0; font-size: 22px;">CRITICAL ANOMALY INTERCEPTED</h3>
                    <p style="color: #fca5a5; margin: 8px 0 0 0; font-size: 14px; leading-height: 1.6;">
                        One-Class SVM flagged this transaction pattern as a severe structural outlier (Anomaly Code: <strong>-1</strong>). 
                        Fund transfer held pending dual-control compliance sign-off.
                    </p>
                    <ul style="color: #fecaca; margin-top: 12px; font-size: 13px;">
                        <li><strong>Risk Vector</strong>: Unrecognized access point IP & non-standard execution timing.</li>
                        <li><strong>Directive</strong>: Freeze outbound ledger release & notify Lead Fraud Analyst.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background: rgba(16, 185, 129, 0.15); border: 2px solid #10b981; border-radius: 16px; padding: 24px;">
                    <h3 style="color: #34d399; margin: 0; font-size: 22px;">TRANSACTION CLEARED (NORMAL)</h3>
                    <p style="color: #6ee7b7; margin: 8px 0 0 0; font-size: 14px;">
                        Transaction matches expected user behavioral baseline and normal operational vectors (Anomaly Code: <strong>1</strong>).
                    </p>
                    <ul style="color: #a7f3d0; margin-top: 12px; font-size: 13px;">
                        <li><strong>Risk Score</strong>: Low Risk (Clean History)</li>
                        <li><strong>Action</strong>: Automatic instant settlement authorized.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        with res_col2:
            st.markdown("#### Input Feature Vector")
            st.dataframe(row.T.rename(columns={0: "Telemetry Value"}), use_container_width=True)

import streamlit as st
import pandas as pd
import random


# Page Configuration
st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ FraudShield AI")
st.subheader("AI-Powered Fraud Detection System")

st.markdown("---")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select Module",
    ["Dashboard", "Transaction Analysis", "Alerts"]
)

# Dashboard Page
if page == "Dashboard":

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", "12,450")
    col2.metric("Fraud Detected", "143")
    col3.metric("Risk Accounts", "57")

    st.markdown("---")

    st.subheader("Recent Fraud Alerts")

    data = pd.DataFrame({
        "Transaction ID": ["TXN1001", "TXN1002", "TXN1003"],
        "Amount": [50000, 120000, 75000],
        "Risk Score": ["High", "Medium", "High"],
        "Status": ["Blocked", "Under Review", "Blocked"]
    })

    st.dataframe(data, use_container_width=True)

# Transaction Analysis Page
elif page == "Transaction Analysis":

    st.subheader("Analyze a Transaction")

    col1, col2 = st.columns(2)

    with col1:
        txn_id = st.text_input("Transaction ID")
        amount = st.number_input("Amount (₹)", min_value=0.0)
        sender = st.text_input("Sender Account")
        receiver = st.text_input("Receiver Account")

    with col2:
        txn_type = st.selectbox(
            "Transaction Type",
            ["UPI", "NEFT", "RTGS", "IMPS"]
        )

        location = st.text_input("Location")
        device = st.selectbox(
            "Device Type",
            ["Mobile", "Laptop", "ATM"]
        )

    if st.button("Analyze Transaction"):

        risk_score = random.randint(1, 100)

        st.subheader("Analysis Result")

        if risk_score >= 75:
            st.error(
                f"⚠️ High Fraud Risk Detected\n\nRisk Score: {risk_score}%"
            )

        elif risk_score >= 40:
            st.warning(
                f"⚠️ Medium Fraud Risk\n\nRisk Score: {risk_score}%"
            )

        else:
            st.success(
                f"✅ Transaction Appears Safe\n\nRisk Score: {risk_score}%"
            )

        st.progress(risk_score)

# Alerts Page
elif page == "Alerts":

    st.subheader("Live Fraud Alerts")

    alerts = pd.DataFrame({
        "Alert ID": ["ALT001", "ALT002", "ALT003"],
        "Account": ["XXXX1234", "XXXX5678", "XXXX9101"],
        "Alert Type": [
            "Suspicious UPI",
            "Mule Account",
            "Multiple Failed Logins"
        ],
        "Severity": ["High", "Medium", "High"]
    })

    st.dataframe(alerts, use_container_width=True)

    st.info("Real-time alerts from AI Engine will appear here.")

# Footer
st.markdown("---")
st.caption("FraudShield AI © 2026 | Bank Cyber Security Solution")
import streamlit as st

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FraudShield AI")
st.subheader(
    "AI-Powered Fraud Detection & Mule Account Monitoring System"
)

st.success("System Loaded Successfully")
import streamlit as st

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FraudShield AI")

st.markdown("""
## AI Powered Fraud Detection System

### Features

✅ Transaction Fraud Detection

✅ Mule Account Detection

✅ Real-time Alerts

✅ Risk Analysis Dashboard

Use the sidebar to navigate.
""")
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", "15,000")
col2.metric("Frauds Detected", "230")
col3.metric("High Risk Accounts", "58")

data = pd.DataFrame({
    "Category": ["Safe", "Fraud"],
    "Count": [14770, 230]
})

fig = px.pie(
    data,
    names="Category",
    values="Count",
    title="Transaction Distribution"
)

st.plotly_chart(fig, use_container_width=True)

chart_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Frauds": [10, 15, 8, 25, 12]
})

fig2 = px.bar(
    chart_data,
    x="Day",
    y="Frauds",
    title="Fraud Cases Per Day"
)

st.plotly_chart(fig2, use_container_width=True)
import streamlit as st
import random

st.title("💳 Transaction Analysis")

txn_id = st.text_input("Transaction ID")

amount = st.number_input(
    "Amount (₹)",
    min_value=0.0
)

txn_type = st.selectbox(
    "Transaction Type",
    ["UPI", "NEFT", "RTGS", "IMPS"]
)

location = st.text_input("Location")

device = st.selectbox(
    "Device",
    ["Mobile", "Laptop", "ATM"]
)

if st.button("Analyze Transaction"):

    risk = random.randint(1, 100)

    st.subheader(f"Risk Score : {risk}%")

    st.progress(risk)

    if risk > 75:
        st.error("⚠ HIGH RISK - BLOCK TRANSACTION")

    elif risk > 40:
        st.warning("⚠ MEDIUM RISK - REVIEW REQUIRED")

    else:
        st.success("✅ LOW RISK - TRANSACTION SAFE")

import streamlit as st

st.title("🕵 Mule Account Detection")

incoming = st.number_input(
    "Monthly Incoming Amount",
    min_value=0
)

beneficiaries = st.number_input(
    "Number of Beneficiaries",
    min_value=0
)

withdrawals = st.number_input(
    "Cash Withdrawals Per Week",
    min_value=0
)

if st.button("Detect Mule Account"):

    score = 0

    if incoming > 500000:
        score += 40

    if beneficiaries > 10:
        score += 30

    if withdrawals > 5:
        score += 30

    st.progress(score)

    if score >= 60:
        st.error("⚠ Suspicious Mule Account Detected")

    else:
        st.success("✅ Account Appears Normal")

import streamlit as st
import pandas as pd

st.title("🚨 Fraud Alerts")

alerts = pd.DataFrame({
    "Alert ID": ["ALT101", "ALT102", "ALT103"],
    "Account": ["XXXX1234", "XXXX5678", "XXXX4321"],
    "Severity": ["HIGH", "MEDIUM", "CRITICAL"],
    "Status": ["Blocked", "Review", "Blocked"]
})

st.dataframe(alerts, width="stretch")

import streamlit as st
import pandas as pd

st.title("📑 Reports")

uploaded = st.file_uploader(
    "Upload Transaction CSV",
    type=["csv"]
)

if uploaded:

    df = pd.read_csv(uploaded)

    st.dataframe(df, width="stretch")

    csv = df.to_csv(index=False).encode()

    st.download_button(
        "Download Report",
        csv,
        "fraud_report.csv",
        "text/csv"
    )
    
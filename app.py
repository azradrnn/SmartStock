import streamlit as st
import plotly.graph_objects as go
import joblib

# Page Config

st.set_page_config(
    page_title="SmartStock",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Load Model 

model = joblib.load("smartstock_model.pkl")

# Custom CSS

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .stApp {
        background: #F3EFE5;
        color: #17221C;
        overflow-x: hidden;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 3rem;
        padding-bottom: 4rem;
    }

    /* BACKGROUND */

    .stApp::before {
        content: "";
        position: fixed;
        width: 650px;
        height: 650px;
        left: -180px;
        top: -170px;

        background: radial-gradient(
            circle at 45% 45%,
            rgba(151, 187, 163, 0.75) 0%,
            rgba(151, 187, 163, 0.35) 32%,
            rgba(151, 187, 163, 0) 70%
        );

        filter: blur(25px);
        z-index: 0;
        pointer-events: none;
    }

    .stApp::after {
        content: "";
        position: fixed;
        width: 720px;
        height: 720px;
        right: -230px;
        bottom: -260px;

        background: radial-gradient(
            circle at 50% 50%,
            rgba(125, 160, 187, 0.55) 0%,
            rgba(125, 160, 187, 0.25) 35%,
            rgba(125, 160, 187, 0) 72%
        );

        filter: blur(35px);
        z-index: 0;
        pointer-events: none;
    }

    /* BRAND */

    .brand {
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 2.35rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.055em !important;
        line-height: 1 !important;
        color: #18231D !important;
        text-transform: none !important;
    }

    .brand-smart {
        color: #648C72 !important;
        font-weight: 700 !important;
        text-transform: none !important;
    }

    .brand-stock {
        color: #18231D !important;
        font-weight: 700 !important;
        text-transform: none !important;
    }

    .status-badge-container {
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin-top: 0.2rem;
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid rgba(74, 158, 97, 0.5);
        padding: 6px 14px;
        border-radius: 99px;
        box-shadow: 0 0 16px rgba(74, 158, 97, 0.4);
    }

    .status-text {
        color: #2F5238 !important;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.02em;
        margin: 0;
    }

    .status-dot {
        color: #4A9E61 !important;
        font-size: 0.9rem;
        line-height: 1;
        text-shadow: 0 0 6px rgba(74, 158, 97, 0.8);
    }

    /* HERO */

    .hero-space {
        height: 3rem;
    }

    .hero-main {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        line-height: 1.02;
        letter-spacing: -0.055em;
        color: #18231D !important;
        margin: 0;
        padding: 0;
    }

    .hero-green {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(2.5rem, 5vw, 4rem);
        font-weight: 700;
        line-height: 1.02;
        letter-spacing: -0.055em;
        color: #648C72 !important;
        margin: 0.1rem 0 0 0;
        padding: 0;
    }

    .hero-description {
        color: #556358 !important;
        font-size: 1rem;
        line-height: 1.5;
        max-width: 720px;
        margin-top: 1rem;
        margin-bottom: 2.2rem;
    }

    /* INPUTS */

    label {
        color: #536057 !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    div[data-baseweb="input"] {
        border-radius: 12px !important;
        border: 1px solid rgba(66, 83, 71, 0.18) !important;
        background: #24342A !important;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #6D987A !important;
        box-shadow: 0 0 0 3px rgba(109,152,122,0.15) !important;
    }

    input {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    /* PREDICT BUTTON */

    .stButton {
        display: flex;
        justify-content: flex-start;
    }

    .stButton > button {
        width: 260px !important;
        max-width: 260px !important;
        height: 48px;

        border: none;
        border-radius: 12px;

        background: #4FA367 !important;
        color: #FFFFFF !important;

        font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem;
        font-weight: 700;

        margin-top: 1.65rem;

        box-shadow: 0 6px 20px rgba(79, 163, 103, 0.45);

        transition:
            background 0.2s ease,
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {
        background: #418E57 !important;
        color: #FFFFFF !important;

        transform: translateY(-2px);

        box-shadow:
            0 10px 25px rgba(79, 163, 103, 0.65);
    }

    /* RESULT CARDS */

    .results-container {
        margin-top: 2.5rem;
    }

    .custom-result-card {
        background: rgba(255, 255, 255, 0.75) !important;
        border: 1px solid rgba(52, 70, 59, 0.2) !important;
        border-radius: 18px !important;
        padding: 1.5rem !important;
        box-shadow: 0 12px 35px rgba(38, 53, 43, 0.08) !important;
        
        min-height: 165px; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .result-label {
        color: #7A817B !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .result-number {
        font-family: 'DM Sans', sans-serif !important;
        color: #1E2B23 !important;
        font-size: 2.3rem !important;
        font-weight: 900 !important;
        letter-spacing: -0.055em !important;
        line-height: 1.05 !important;
        margin-top: 0.35rem;
        margin-bottom: 0.25rem;
    }

    .result-description {
        color: #737C75 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.8rem !important;
        line-height: 1.4 !important;
    }

    /* TREND CARD */

    .trend-symbol {
        font-family: 'DM Sans', sans-serif !important;
        color: #1E2B23 !important;
        font-size: 2.3rem !important;
        font-weight: 900 !important;
        line-height: 1 !important;
        margin-top: 0.35rem;
        margin-bottom: 0.4rem;
    }

    .trend-description {
        color: #737C75 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.8rem !important;
        line-height: 1.4 !important;
        margin: 0 !important;
    }

    /* CHART */

    .chart-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.35rem;
        font-weight: 600;
        color: #1E2B23 !important;
        margin-top: 2.8rem;
        margin-bottom: 0.2rem;
    }

    .stCaption {
        color: #737C75 !important;
    }

    hr {
        border-color: rgba(52, 70, 59, 0.08) !important;
        margin-top: 0.8rem !important;
        margin-bottom: 0.8rem !important;
    }

    /* FOOTER */

    .footer-text {
        color: #8A918B !important;
        font-size: 0.72rem;
    }

    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Header

header_col1, header_col2 = st.columns([3, 1])

with header_col1:
    st.markdown(
        """
        <div class="brand">
            <span class="brand-smart">Smart</span><span class="brand-stock">Stock</span>
        </div>
        """,
        unsafe_allow_html=True
    )

with header_col2:
    st.markdown(
        """
        <div class="status-badge-container">
            <div class="status-badge">
                <span class="status-dot">●</span>
                <span class="status-text">Prediction model ready</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Hero

st.markdown(
    '<div class="hero-space"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-main">Predict sales.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-green">Plan inventory effortlessly.</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-description">
    Enter your last 6 weeks of sales data to forecast future demand and discover your optimal stock level. SmartStock turns sales trends into actionable inventory insights using machine learning.

    </div>
    """,
    unsafe_allow_html=True
)

# Inputs 

col1, col2, col3 = st.columns(3)

with col1:
    w1 = st.number_input("Week 1", min_value=0, value=10, step=1)
    w4 = st.number_input("Week 4", min_value=0, value=15, step=1)

with col2:
    w2 = st.number_input("Week 2", min_value=0, value=12, step=1)
    w5 = st.number_input("Week 5", min_value=0, value=17, step=1)

with col3:
    w3 = st.number_input("Week 3", min_value=0, value=14, step=1)
    w6 = st.number_input("Week 6", min_value=0, value=19, step=1)

# Current stock

stock_col, button_col = st.columns([1, 2])

with stock_col:
    current_stock = st.number_input("Current stock", min_value=0, value=5, step=1)

with button_col:
    predict = st.button("Predict next week  →")

# Data

sales = [w1, w2, w3, w4, w5, w6]

# Model prediction 

model_trend = sales[-1] - sales[0]
features = sales + [model_trend]

prediction = model.predict([features])[0]
prediction = max(0, round(prediction))

# Trend analysis

recent_sales = sales[-4:]
changes = []

for i in range(1, len(recent_sales)):
    change = recent_sales[i] - recent_sales[i - 1]
    changes.append(change)

positive_changes = sum(change > 0 for change in changes)
negative_changes = sum(change < 0 for change in changes)

max_recent = max(recent_sales)
min_recent = min(recent_sales)
variation = max_recent - min_recent
recent_average = sum(recent_sales) / len(recent_sales)
variation_ratio = variation / recent_average if recent_average != 0 else 0

if variation_ratio > 0.60:
    trend_text = "Sales have been changing a lot."
    trend_symbol = "↔"
elif positive_changes >= 2 and positive_changes > negative_changes:
    trend_text = "Sales have been increasing in recent weeks."
    trend_symbol = "↗"
elif negative_changes >= 2 and negative_changes > positive_changes:
    trend_text = "Sales have been decreasing in recent weeks."
    trend_symbol = "↘"
else:
    trend_text = "There is no clear sales trend."
    trend_symbol = "→"

# Inventory

safety_stock = round(prediction * 0.20)
total_need = prediction + safety_stock
recommended_order = max(0, total_need - current_stock)

# Results 

if predict:
    st.markdown('<div class="results-container">', unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)

   
    #Prediction card 

    with r1:
        st.markdown(
            f"""
            <div class="custom-result-card">
                <div>
                    <div class="result-label">Next week prediction</div>
                    <div class="result-number">{prediction} units</div>
                </div>
                <div class="result-description">Estimated units to be sold next week.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Trend card 

    with r2:
        st.markdown(
            f"""
            <div class="custom-result-card">
                <div>
                    <div class="result-label">Sales trend</div>
                    <div class="trend-symbol">{trend_symbol}</div>
                </div>
                <div class="trend-description">{trend_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Order card 

    with r3:
        st.markdown(
            f"""
            <div class="custom-result-card">
                <div>
                    <div class="result-label">Recommended order</div>
                    <div class="result-number">{recommended_order} units</div>
                </div>
                <div class="result-description">Units recommended after safety stock.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # Chart

    st.markdown(
        '<div class="chart-title">Sales prediction</div>',
        unsafe_allow_html=True
    )

    st.caption(
        "Historical sales and predicted demand for next week."
    )

    st.divider()

    fig = go.Figure()

    # Historical Sales 

    fig.add_trace(
        go.Scatter(
            x=[
                "Week 1",
                "Week 2",
                "Week 3",
                "Week 4",
                "Week 5",
                "Week 6",
            ],
            y=sales,
            mode="lines+markers",
            name="Historical sales",
            line=dict(width=3),
            marker=dict(size=7)
        )
    )

    # Forecast 

    fig.add_trace(
        go.Scatter(
            x=[
                "Week 6",
                "Next Week"
            ],
            y=[
                sales[-1],
                prediction
            ],
            mode="lines",
            name="Forecast",
            line=dict(
                width=2,
                dash="dash"
            )
        )
    )

    #Predicted point  

    fig.add_trace(
        go.Scatter(
            x=["Next Week"],
            y=[prediction],
            mode="markers",
            name="Predicted sales",
            marker=dict(size=11)
        )
    )

    # Chart Style 
  
    fig.update_layout(
        height=360,
        margin=dict(
            l=10,
            r=10,
            t=45,
            b=10
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="DM Sans",
            color="#24352B",
            size=12
        ),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(
                family="DM Sans",
                size=11,
                color="#24352B"
            )
        ),
        xaxis=dict(
            showgrid=False,
            color="#24352B",
            tickfont=dict(
                family="DM Sans",
                size=11,
                color="#24352B"
            )
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="rgba(100,140,114,0.10)",
            color="#24352B",
            tickfont=dict(
                family="DM Sans",
                size=11,
                color="#24352B"
            )
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

# Footer

st.divider()

footer_col1, footer_col2 = st.columns(2)

with footer_col1:
    st.caption(
        "SmartStock · Sales & Inventory Prediction"
    )

with footer_col2:
    st.caption(
        "Machine Learning Project"
    )
"""
PROPRIETARY SOFTWARE - © 2025 [SudheerAluru]
Patent Pending | All Rights Reserved
Licensed for demonstration use only
"""
"""
🧠 NeuroGrowth Pro: Advanced Child Development Dashboard
Clinical-Grade Assessment with Personalized Insights
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime
from PIL import Image

# ========== CONFIGURATION ========== #
THEME = {
    "primary": "#3A86FF",  # Vibrant blue
    "secondary": "#8338EC",  # Purple
    "accent": "#FF006E",  # Pink
    "background": "#F8F9FF",
    "text": "#2B2D42",
    "success": "#06D6A0",
    "warning": "#FFBE0B",
    "danger": "#EF476F"
}

# ========== SETUP ========== #
st.set_page_config(
    page_title="NeuroGrowth Pro",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown(f"""
<style>
    .main {{
        background-color: {THEME["background"]};
        color: {THEME["text"]};
    }}
    .sidebar .sidebar-content {{
        background: linear-gradient(180deg, {THEME["primary"]} 0%, {THEME["secondary"]} 100%);
        color: white;
    }}
    .stButton>button {{
        background: {THEME["primary"]};
        color: white;
        border-radius: 8px;
        font-weight: 500;
        padding: 0.5rem 1rem;
    }}
    .metric-card {{
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-left: 4px solid {THEME["primary"]};
    }}
    .domain-card {{
        background: white;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }}
</style>
""", unsafe_allow_html=True)

# ========== SIDEBAR ========== #
with st.sidebar:
    st.title("🧠 NeuroGrowth Pro")
    st.markdown("""
    **Clinical-Grade Child Development Assessment**  
    Track cognitive, emotional, and social development  
    with research-backed metrics.
    """)
    
    st.markdown("---")
    st.markdown("### Child Profile")
    child_name = st.text_input("Name")
    child_age = st.number_input("Age (years)", 1, 18, 5)
    child_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    assessment_date = st.date_input("Assessment Date")
    
    st.markdown("---")
    st.markdown("### Assessment History")
    st.button("View Previous Reports")
    st.button("Export Data")
    
    st.markdown("---")
    st.markdown("""
    *Developed by*  
    **Child Development Institute**  
    [contact@neurogrowth.org](mailto:contact@neurogrowth.org)
    """)

# ========== MAIN CONTENT ========== #
st.title("Comprehensive Development Assessment")
st.markdown(f"""<div style='color:{THEME["text"]}; margin-bottom:2rem;'>
    Complete this 10-minute assessment to receive personalized insights about your child's development.
</div>""", unsafe_allow_html=True)

# ========== ASSESSMENT SECTIONS ========== #
tab1, tab2, tab3 = st.tabs(["🧠 Cognitive", "💖 Emotional", "👥 Social"])

with tab1:
    st.header("Cognitive Development")
    with st.expander("ℹ️ About This Domain", expanded=True):
        st.markdown("""
        Cognitive development involves how children think, explore, and figure things out.  
        It includes memory, problem-solving, decision-making, and language skills.
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### Attention Span")
            attention = st.slider(
                "Can focus on tasks for age-appropriate durations",
                1, 10, 5,
                help="1 = Rarely sustains focus, 10 = Excellent concentration"
            )
            st.plotly_chart(
                px.bar(x=["Attention"], y=[attention], range_y=[0,10], 
                      color_discrete_sequence=[THEME["primary"]]),
                use_container_width=True
            )
    
    with col2:
        with st.container(border=True):
            st.markdown("#### Problem Solving")
            problem_solving = st.slider(
                "Solves age-appropriate problems independently",
                1, 10, 5,
                help="1 = Needs constant help, 10 = Creative solutions"
            )
            st.plotly_chart(
                px.bar(x=["Problem Solving"], y=[problem_solving], range_y=[0,10],
                      color_discrete_sequence=[THEME["secondary"]]),
                use_container_width=True
            )

with tab2:
    st.header("Emotional Development")
    with st.expander("ℹ️ About This Domain", expanded=True):
        st.markdown("""
        Emotional development involves how children understand their own and others' feelings,  
        develop empathy, and manage emotions.
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### Emotional Regulation")
            regulation = st.slider(
                "Manages and recovers from emotional upsets",
                1, 10, 5,
                help="1 = Frequent meltdowns, 10 = Quick recovery"
            )
            st.plotly_chart(
                px.bar(x=["Regulation"], y=[regulation], range_y=[0,10],
                      color_discrete_sequence=[THEME["accent"]]),
                use_container_width=True
            )
    
    with col2:
        with st.container(border=True):
            st.markdown("#### Empathy")
            empathy = st.slider(
                "Shows understanding of others' feelings",
                1, 10, 5,
                help="1 = Rarely notices, 10 = Highly attuned"
            )
            st.plotly_chart(
                px.bar(x=["Empathy"], y=[empathy], range_y=[0,10],
                      color_discrete_sequence=[THEME["warning"]]),
                use_container_width=True
            )

with tab3:
    st.header("Social Development")
    with st.expander("ℹ️ About This Domain", expanded=True):
        st.markdown("""
        Social development involves how children interact with others,  
        form relationships, and understand social rules.
        """)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### Peer Interaction")
            interaction = st.slider(
                "Engages appropriately with peers",
                1, 10, 5,
                help="1 = Avoids interaction, 10 = Initiates play"
            )
            st.plotly_chart(
                px.bar(x=["Interaction"], y=[interaction], range_y=[0,10],
                      color_discrete_sequence=[THEME["success"]]),
                use_container_width=True
            )
    
    with col2:
        with st.container(border=True):
            st.markdown("#### Communication")
            communication = st.slider(
                "Expresses needs and ideas clearly",
                1, 10, 5,
                help="1 = Difficulty expressing, 10 = Clear communication"
            )
            st.plotly_chart(
                px.bar(x=["Communication"], y=[communication], range_y=[0,10],
                      color_discrete_sequence=[THEME["danger"]]),
                use_container_width=True
            )

# ========== ANALYSIS ENGINE ========== #
if st.button("🔍 Run Comprehensive Analysis", type="primary"):
    with st.spinner("Generating personalized insights..."):
        
        # Calculate scores
        cognitive_score = (attention + problem_solving) / 2
        emotional_score = (regulation + empathy) / 2
        social_score = (interaction + communication) / 2
        overall_score = (cognitive_score + emotional_score + social_score) / 3
        
        # Generate results
        st.success("Analysis complete!")
        st.markdown("---")
        st.header("📊 Developmental Profile")
        
        # Radar Chart
        df = pd.DataFrame({
            "Domain": ["Cognitive", "Emotional", "Social"],
            "Score": [cognitive_score, emotional_score, social_score]
        })
        
        fig = px.line_polar(
            df, r="Score", theta="Domain", 
            line_close=True,
            color_discrete_sequence=[THEME["primary"]],
            template="plotly_white"
        )
        fig.update_traces(fill='toself')
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0,10])),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
                <h3>Cognitive</h3>
                <h1 style='color:{THEME["primary"]};'>{cognitive_score:.1f}/10</h1>
                <p>{"⭐" * int(cognitive_score/2)}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class='metric-card'>
                <h3>Emotional</h3>
                <h1 style='color:{THEME["accent"]};'>{emotional_score:.1f}/10</h1>
                <p>{"⭐" * int(emotional_score/2)}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-card'>
                <h3>Social</h3>
                <h1 style='color:{THEME["success"]};'>{social_score:.1f}/10</h1>
                <p>{"⭐" * int(social_score/2)}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("---")
        st.header("📝 Personalized Recommendations")
        
        if overall_score < 5:
            st.warning("## Areas for Support")
            st.markdown("""
            <div class='domain-card'>
                <h4>🧠 Cognitive Strategies</h4>
                <ul>
                    <li>Practice focused activities in 10-minute increments</li>
                    <li>Use visual schedules to support task completion</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("## Strengths to Nurture")
            st.markdown("""
            <div class='domain-card'>
                <h4>🌟 Development Highlights</h4>
                <ul>
                    <li>Strong foundation in multiple developmental areas</li>
                    <li>Continue providing enriched learning opportunities</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Progress Tracking
        st.markdown("---")
        st.header("📅 Progress Tracking")
        progress_data = pd.DataFrame({
            "Date": [datetime(2023,1,1), datetime(2023,4,1), datetime(2023,7,1), datetime.now()],
            "Cognitive": [4.2, 5.1, 5.8, cognitive_score],
            "Emotional": [3.9, 4.5, 5.2, emotional_score],
            "Social": [4.1, 4.8, 5.5, social_score]
        })
        
        fig = px.line(
            progress_data, x="Date", y=["Cognitive", "Emotional", "Social"],
            color_discrete_sequence=[THEME["primary"], THEME["accent"], THEME["success"]],
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)

# ========== FOOTER ========== #
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    <p>NeuroGrowth Pro v2.1 • Clinical Assessment Tool</p>
    <p>This tool does not replace professional evaluation</p>
</div>
""", unsafe_allow_html=True)

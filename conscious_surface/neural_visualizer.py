import streamlit as st
import plotly.express as px

def plot_reasoning_path(phase_data):
    # Visualizes the 'effort' distribution across framework phases
    fig = px.bar(x=[p[0] for p in phase_data], y=[p[1] for p in phase_data], 
                 labels={'x': 'Cognitive Phase', 'y': 'Duration (ms)'},
                 title="Internal Reasoning Effort Distribution")
    st.plotly_chart(fig)

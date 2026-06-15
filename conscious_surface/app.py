import streamlit as st
from framework_manager import FrameworkManager
from thought_matrix import ThoughtMatrix
from telemetry_bridge import TelemetryBridge
import dashboard_charts
import cognitive_core # Validating Rust bridge is active

st.set_page_config(page_title="S3lf-c0n8ci0us Engine", page_icon="🧠", layout="wide")
st.title("🧠 S3lf-c0n8ci0us Auto-Cognitive Engine")
st.caption(f"Rust Core Bridge Status: ACTIVE")
st.write("---")

fm = FrameworkManager()
framework_files = fm.get_available_frameworks()

# Sidebar
st.sidebar.header("Cognitive Settings")
selected_file = st.sidebar.selectbox("Force Brain Frame", framework_files)
framework_data = fm.load_framework(selected_file)

st.sidebar.subheader(f"Active: {framework_data['name']}")
st.sidebar.caption(framework_data['description'])

# Main UI
user_query = st.text_area("Input complex engineering crisis or bottleneck here:")

if st.button("Initialize Reasoning Run"):
    if user_query:
        matrix = ThoughtMatrix()
        telemetry = TelemetryBridge()
        
        # UI placeholders
        chart_placeholder = st.empty()
        text_placeholder = st.empty()
        full_text = ""
        
        with st.spinner("Aligning neural processing constraints..."):
            # The thought matrix now yields tuples: (text_chunk, execution_ms)
            for chunk_data in matrix.execute_cognitive_loop(user_query, framework_data):
                text_chunk, exec_ms = chunk_data
                full_text += text_chunk
                text_placeholder.markdown(full_text)
                
                # Log telemetry and update charts live
                telemetry.log_latency_delta(text_chunk, exec_ms)
                with chart_placeholder.container():
                    dashboard_charts.render_cognitive_metrics(telemetry.metrics_history)
    else:
        st.error("Please provide an engineering input query to begin.")

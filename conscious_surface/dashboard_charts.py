import streamlit as st

def render_cognitive_metrics(telemetry_snapshots):
    if not telemetry_snapshots:
        return
        
    # Isolate recent metrics
    latest = telemetry_snapshots[-1]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Rust Core Latency Delta", value=f"{latest['latency_ms']:.2f} ms")
    with col2:
        st.metric(label="Processing Throughput", value=f"{latest['throughput_tps']:.1f} tokens/sec")
        
    # Render mini structural chart line history
    chart_data = [snapshot["throughput_tps"] for snapshot in telemetry_snapshots]
    st.caption("Auto-Cognitive Processing Velocity (Tokens/Sec)")
    st.line_chart(chart_data, height=120, use_container_width=True)

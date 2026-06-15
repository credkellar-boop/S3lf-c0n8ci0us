import streamlit as st
from ingestion_bridge import DataIngestor

def render_upload_zone():
    st.sidebar.markdown("---")
    st.sidebar.subheader("Context Injection")
    uploaded_file = st.sidebar.file_uploader("Attach Logs or Code (.txt, .log, .py)", type=["txt", "log", "py", "rs"])
    
    if uploaded_file:
        ingestor = DataIngestor()
        with st.sidebar.status("Rust parsing file..."):
            parsed_context = ingestor.process_uploaded_file(uploaded_file)
            st.sidebar.success(f"Ingested {len(parsed_context)} chars.")
            return parsed_context
    return None

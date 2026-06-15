import streamlit as st
import json
import os
from thought_matrix import ThoughtMatrix

st.set_page_config(page_title="S3lf-c0n8ci0us Engine", page_icon="🧠", layout="wide")
st.title("🧠 S3lf-c0n8ci0us Auto-Cognitive Engine")
st.write("---")

# Setup framework paths
LIB_DIR = os.path.join(os.path.dirname(__file__), "../subconscious_lib")
frameworks = ["systems_analysis.json", "root_cause.json"]

# Sidebar Selection
st.sidebar.header("Cognitive Framework Settings")
selected_file = st.sidebar.selectbox("Force Brain Frame", frameworks)

# Load framework text data safely
with open(os.path.join(LIB_DIR, selected_file), "r") as f:
    framework_data = json.load(f)

st.sidebar.subheader(f"Active Template: {framework_data['name']}")
st.sidebar.caption(framework_data['description'])

# User Interaction Zone
user_query = st.text_area("Input complex engineering crisis or bottleneck here:")
if st.button("Initialize Reasoning Run"):
    if user_query:
        matrix = ThoughtMatrix()
        with st.spinner("Aligning neural processing constraints..."):
            output_stream = matrix.execute_cognitive_loop(user_query, framework_data)
            
            if isinstance(output_stream, str):
                st.info(output_stream)
            else:
                placeholder = st.empty()
                full_text = ""
                for chunk in output_stream:
                    if chunk.choices[0].delta.content:
                        full_text += chunk.choices[0].delta.content
                        placeholder.markdown(full_text)
    else:
        st.error("Please provide an engineering input query to begin.")

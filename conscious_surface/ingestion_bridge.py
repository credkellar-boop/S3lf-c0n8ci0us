import os
import tempfile
import cognitive_core

class DataIngestor:
    def process_uploaded_file(self, uploaded_file):
        """Saves a streamlit file upload to a temp location, processes in Rust, and returns string."""
        if uploaded_file is None:
            return ""
            
        # Write Streamlit UploadedFile to a temporary disk location for Rust to read
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
            
        try:
            # Blast it through the Rust core
            sanitized_text = cognitive_core.rust_read_and_sanitize_file(tmp_path)
        finally:
            os.remove(tmp_path) # Clean up temp file
            
        return sanitized_text

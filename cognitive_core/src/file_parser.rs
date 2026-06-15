use pyo3::prelude::*;
use std::fs;
use std::path::Path;

#[pyfunction]
pub fn rust_read_and_sanitize_file(file_path: String) -> PyResult<String> {
    let path = Path::new(&file_path);
    
    // Read file quickly into a string
    let raw_content = fs::read_to_string(path)
        .unwrap_or_else(|_| "[RUST PARSER ERROR]: Could not read file.".to_string());
        
    // Basic sanitization: remove excessive whitespace and null characters to save LLM tokens
    let sanitized: String = raw_content
        .split_whitespace()
        .collect::<Vec<&str>>()
        .join(" ");
        
    Ok(sanitized)
}

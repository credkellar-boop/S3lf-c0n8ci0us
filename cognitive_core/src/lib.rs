use pyo3::prelude::*;

mod framework_router;
mod self_audit;

// --- Added RustMemoryBuffer so Python can import and initialize it ---
#[pyclass]
pub struct RustMemoryBuffer {
    capacity: usize,
}

#[pymethods]
impl RustMemoryBuffer {
    #[new]
    pub fn new(capacity: usize) -> Self {
        RustMemoryBuffer { capacity }
    }

    pub fn clear(&mut self) {
        // Add your specific memory clearing logic here in the future
    }
}
// ---------------------------------------------------------------------

#[pyfunction]
fn rust_audit_stream(text: String) -> PyResult<bool> {
    let mut auditor = self_audit::AuditLog::new();
    Ok(auditor.audit_text(&text))
}

#[pyfunction]
fn rust_route_input(user_input: String) -> PyResult<String> {
    // Removed the 'mut' here to clear your compiler warning
    let router = framework_router::Router::new(); 
    // Simplified routing signature for Python bridge
    match router.route_input(&user_input) {
        Some(f) => Ok(f.name.clone()),
        None => Ok("baseline".to_string()),
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn cognitive_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_audit_stream, m)?)?;
    m.add_function(wrap_pyfunction!(rust_route_input, m)?)?;
    
    // --- Register the class with the module so Python can see it ---
    m.add_class::<RustMemoryBuffer>()?;
    
    Ok(())
}

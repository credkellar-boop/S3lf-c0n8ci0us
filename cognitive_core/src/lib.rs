use pyo3::prelude::*;

mod framework_router;
mod self_audit;

#[pyclass]
pub struct RustMemoryBuffer {
    capacity: usize,
    // Internal storage placeholder for the contexts being added
    contexts: Vec<String>,
}

#[pymethods]
impl RustMemoryBuffer {
    #[new]
    pub fn new(capacity: usize) -> Self {
        RustMemoryBuffer { 
            capacity,
            contexts: Vec::new(),
        }
    }

    // This solves the AttributeError by exposing add_context to Python
    pub fn add_context(&mut self, context: String) {
        self.contexts.push(context);
    }

    pub fn clear(&mut self) {
        self.contexts.clear();
    }
}

#[pyfunction]
fn rust_audit_stream(text: String) -> PyResult<bool> {
    let mut auditor = self_audit::AuditLog::new();
    Ok(auditor.audit_text(&text))
}

#[pyfunction]
fn rust_route_input(user_input: String) -> PyResult<String> {
    let router = framework_router::Router::new(); 
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
    m.add_class::<RustMemoryBuffer>()?;
    Ok(())
}

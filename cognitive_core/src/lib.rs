use pyo3::prelude::*;

mod framework_router;
mod self_audit;

#[pyfunction]
fn rust_audit_stream(text: String) -> PyResult<bool> {
    let mut auditor = self_audit::AuditLog::new();
    Ok(auditor.audit_text(&text))
}

#[pyfunction]
fn rust_route_input(user_input: String) -> PyResult<String> {
    let mut router = framework_router::Router::new();
    // Simplified routing signature for Python bridge handoff
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
    Ok(())
}

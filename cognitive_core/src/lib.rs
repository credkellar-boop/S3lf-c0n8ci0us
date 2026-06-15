use pyo3::prelude::*;

mod framework_router;
mod self_audit;

#[pyclass]
pub struct RustMemoryBuffer {
    capacity: usize,
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

    // Explicitly enforce &mut self to mutate the instance Python is holding
    pub fn add_context(&mut self, context: String) {
        // Enforce FIFO capacity limits if your test pushes "Memory 3" and expects "Memory 1" to drop
        if self.contexts.len() >= self.capacity {
            self.contexts.remove(0);
        }
        self.contexts.push(context);
    }

    // Explicitly return a copy of the list to Python
    pub fn get_full_context(&self) -> PyResult<Vec<String>> {
        Ok(self.contexts.clone())
    }

    // Explicitly clear the vector data
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

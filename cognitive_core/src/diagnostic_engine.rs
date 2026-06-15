pub struct DiagnosticEngine {
    pub logs: Vec<(String, f64)>, // (PhaseName, DurationInMs)
}

impl DiagnosticEngine {
    pub fn record_phase_effort(&mut self, phase: String, duration: f64) {
        self.logs.push((phase, duration));
    }
}

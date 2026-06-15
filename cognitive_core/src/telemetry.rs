use std::time::Instant;

pub struct CoreTelemetry {
    run_start: Instant,
    last_checkpoint: Instant,
}

impl CoreTelemetry {
    pub fn start() -> Self {
        let now = Instant::now();
        Self { run_start: now, last_checkpoint: now }
    }

    pub fn mark_checkpoint(&mut self) -> f64 {
        let elapsed = self.last_checkpoint.elapsed().as_secs_f64() * 1000.0;
        self.last_checkpoint = Instant::now();
        elapsed // Returns duration in milliseconds
    }

    pub fn total_runtime(&self) -> f64 {
        self.run_start.elapsed().as_secs_f64()
    }
}

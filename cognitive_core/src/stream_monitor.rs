pub struct StreamMonitor {
    pub token_count: usize,
    pub start_time: std::time::Instant,
}

impl StreamMonitor {
    pub fn new() -> Self {
        Self {
            token_count: 0,
            start_time: std::time::Instant::now(),
        }
    }

    // Registers a newly generated text chunk and prints execution metrics
    pub fn track_chunk(&mut self, chunk: &str) {
        self.token_count += chunk.split_whitespace().count() + 1;
        let elapsed = self.start_time.elapsed().as_secs_f64();
        
        if elapsed > 0.0 {
            let tokens_per_sec = self.token_count as f64 / elapsed;
            print!("\r⚡ [S3lf-c0n8ci0us Core] Streaming: {:.2} tokens/sec", tokens_per_sec);
        }
    }
}

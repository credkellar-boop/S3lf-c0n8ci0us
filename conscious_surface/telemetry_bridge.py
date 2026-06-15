import time

class TelemetryBridge:
    def __init__(self):
        self.metrics_history = []

    def log_latency_delta(self, token_chunk, execution_ms):
        chunk_size = len(token_chunk.split()) if token_chunk.strip() else 1
        tokens_per_sec = chunk_size / (execution_ms / 1000.0) if execution_ms > 0 else 0
        
        snapshot = {
            "timestamp": time.time(),
            "latency_ms": execution_ms,
            "throughput_tps": min(tokens_per_sec, 150.0) # Cap outlier spikes
        }
        self.metrics_history.append(snapshot)
        return snapshot

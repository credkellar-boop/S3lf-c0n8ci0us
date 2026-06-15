import json
import os

class RecursiveOptimizer:
    def __init__(self, configuration_path: str = "assets/black_folder/config.json"):
        self.config_path = configuration_path
        self.performance_history = []

    def log_execution_metric(self, loss: float, execution_time: float):
        self.performance_history.append({"loss": loss, "time": execution_time})

    def self_optimize_hyperparameters(self):
        """Analyzes historical metrics to mutate its own architecture parameters."""
        if len(self.performance_history) < 10:
            return # Insufficient data to reason on self-modifications safely

        avg_loss = sum(entry["loss"] for entry in self.performance_history) / len(self.performance_history)
        
        if avg_loss > 0.1:
            # Shift optimization vectors via dynamic hyperparameter updates
            self.apply_mutation("learning_rate_scale", 0.95)

    def apply_mutation(self, key: str, multiplier: float):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                config = json.load(f)
        else:
            config = {"learning_rate_scale": 1.0, "depth_weight": 42}

        config[key] = config.get(key, 1.0) * multiplier

        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=4)

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::fs::File;
use std::io::Read;
use std::path::Path;

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct Step {
    pub phase: String,
    pub prompt_injection: String,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct AnalyticalFramework {
    pub name: String,
    pub description: String,
    pub steps: Vec<Step>,
}

pub struct Router {
    pub frameworks: HashMap<String, AnalyticalFramework>,
}

impl Router {
    pub fn new() -> Self {
        Self {
            frameworks: HashMap::new(),
        }
    }

    // High-speed file reading into memory
    pub fn load_framework<P: AsRef<Path>>(&mut self, path: P) -> Result<(), Box<dyn std::error::Error>> {
        let mut file = File::open(path)?;
        let mut contents = String::new();
        file.read_to_string(&mut contents)?;
        
        let framework: AnalyticalFramework = serde_json::from_str(&contents)?;
        self.frameworks.insert(framework.name.to_lowercase(), framework);
        Ok(())
    }

    // Evaluates user input keywords to inject the correct cognitive framework
    pub fn route_input(&self, user_input: &str) -> Option<&AnalyticalFramework> {
        let input_lower = user_input.to_lowercase();
        
        if input_lower.contains("bug") || input_lower.contains("architecture") || input_lower.contains("system") {
            return self.frameworks.get("systems_analysis");
        } else if input_lower.contains("why") || input_lower.contains("root") || input_lower.contains("fail") {
            return self.frameworks.get("root_cause");
        }
        
        // Default to foundational reasoning
        self.frameworks.get("first_principles")
    }
}

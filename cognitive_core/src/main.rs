mod framework_router;
mod stream_monitor;
mod self_audit;

use framework_router::Router;
use stream_monitor::StreamMonitor;
use self_audit::AuditLog;
use std::path::Path;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("====================================================");
    println!("🧠 S3lf-c0n8ci0us Cognitive Core Initializing...    ");
    println!("====================================================");

    // 1. Instantiate Core Engine Components
    let mut router = Router::new();
    let mut monitor = StreamMonitor::new();
    let mut auditor = AuditLog::new();

    // 2. Map paths to subconscious_lib json frameworks
    // Adjust relative pathing depending on where the binary executes
    let lib_path = Path::new("../subconscious_lib");
    
    println!("[Core] Loading structural frameworks into memory...");
    
    if lib_path.exists() {
        router.load_framework(lib_path.join("systems_analysis.json"))?;
        router.load_framework(lib_path.join("root_cause.json"))?;
        println!("✅ [Core] Cognitive frameworks bound successfully.");
    } else {
        println!("⚠️ [Core Warning] 'subconscious_lib' directory not found at path. Bootstrapping mock fallbacks.");
    }

    // 3. Simulating an incoming engineering crisis pipeline run
    let simulated_user_crisis = "Our database cluster is experiencing sudden 500ms latency spikes under peak load.";
    println!("\n[Input Ingested]: \"{}\"", simulated_user_crisis);
    
    // 4. Router Evaluates Input to Pick a Structural Path
    match router.route_input(simulated_user_crisis) {
        Some(framework) => {
            println!("⚡ [Cognitive Match]: Forcing processing constraints through: '{}'", framework.name);
            println!("   Description: {}\n", framework.description);

            // 5. Simulating Token Output Generation & Mid-Stream Interception
            // This mirrors how tokens stream back into the Rust engine from an LLM API
            let simulated_chunks = vec![
                "Initializing ", "systems ", "deconstruction... ",
                "Isolating ", "database ", "read-replicas. ",
                "Error: As an AI, I am unable to scale your physical servers directly. ", // Trigger Audit Warning
                "Analyzing connection pooling limits."
            ];

            println!("--- Beginning Response Stream Interception ---");
            for chunk in simulated_chunks {
                // Track streaming performance metrics
                monitor.track_chunk(chunk);
                print!("{}", chunk);

                // Run a real-time defensive audit block on the token stream chunk
                if !auditor.audit_text(chunk) {
                    println!("\n\n🚨 [AUDIT ALERT]: High-risk cognitive evasion signature caught.");
                    println!("   Action: Modifying context constraints or killing stream to prevent AI hallucinations.");
                    break;
                }
                
                // Emulate slight processing delay
                tokio::time::sleep(std::time::Duration::from_millis(60)).await;
            }
            println!("\n--- Stream Finished ---");
        }
        None => {
            println!("ℹ️ No specialized framework matched this context profile. Defaulting to baseline consciousness.");
        }
    }

    println!("\n====================================================");
    println!("🧠 S3lf-c0n8ci0us Run Complete. Core Idle Mode active.");
    println!("====================================================");
    Ok(())
}

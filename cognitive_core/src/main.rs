mod framework_router;

use framework_router::Router;

#[tokio::main]
async fn main() {
    println!("🧠 S3lf-c0n8ci0us Cognitive Core Initializing...");

    let mut router = Router::new();

    // In a real environment, these JSON files live in your subconscious_lib folder
    // For now, let's verify our routing architecture logic handles a simulated input:
    let simulated_user_crisis = "Our microservices architecture has a massive performance bottleneck.";
    
    println!("\n[User Input]: \"{}\"", simulated_user_crisis);
    
    // Check if a relevant framework matches the crisis profile
    match router.route_input(simulated_user_crisis) {
        Some(framework) => {
            println!("⚡ [Cognitive Match Found]: Executing the '{}' loop.", framework.name);
        }
        None => {
            println!("ℹ️ No specialized framework in memory. Defaulting to baseline consciousness.");
        }
    }
}

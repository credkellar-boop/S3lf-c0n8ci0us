#[cfg(test)]
mod tests {
    use crate::framework_router::{Router, AnalyticalFramework, Step};

    #[test]
    fn test_router_matches_keywords() {
        let mut router = Router::new();
        
        let mock_framework = AnalyticalFramework {
            name: "root_cause".to_string(),
            description: "Test".to_string(),
            steps: vec![],
        };
        
        router.frameworks.insert("root_cause".to_string(), mock_framework);
        
        // "why" should trigger root_cause based on our router logic
        let result = router.route_input("Tell me why this failed");
        
        assert!(result.is_some());
        assert_eq!(result.unwrap().name, "root_cause");
    }
}

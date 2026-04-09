MODEL_PRESETS: dict[str, dict] = {
    "budget": {
        "description": "Lowest cost, good for prototypes",
        "assignments": {
            "router": "gemini-2.5-flash",
            "architect": "gemini-2.5-flash",
            "coder": "gemini-2.5-flash",
            "tester": "gemini-2.5-flash",
            "devops": "gemini-2.5-flash",
            "security": "gemini-2.5-flash",
            "skill_extractor": "gemini-2.5-flash",
        },
        "estimated_cost_per_pipeline": "$0.01",
    },
    "auto": {
        "description": "Optimal quality/cost balance per agent",
        "assignments": {
            "router": "gemini-2.5-flash",
            "architect": "anthropic/claude-sonnet-4-20250514",
            "coder": "anthropic/claude-sonnet-4-20250514",
            "tester": "openai/gpt-4o-mini",
            "devops": "openai/gpt-4o-mini",
            "security": "anthropic/claude-sonnet-4-20250514",
            "skill_extractor": "openai/gpt-4o-mini",
        },
        "estimated_cost_per_pipeline": "$0.04",
    },
    "premium": {
        "description": "Best models everywhere, maximum quality",
        "assignments": {
            "router": "gemini-2.5-pro",
            "architect": "anthropic/claude-sonnet-4-20250514",
            "coder": "anthropic/claude-sonnet-4-20250514",
            "tester": "anthropic/claude-sonnet-4-20250514",
            "devops": "openai/gpt-4o",
            "security": "anthropic/claude-sonnet-4-20250514",
            "skill_extractor": "openai/gpt-4o-mini",
        },
        "estimated_cost_per_pipeline": "$0.08",
    },
}

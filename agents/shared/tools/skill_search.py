from shared.services.skill_resolution.engine import SkillResolutionEngine

_engine = SkillResolutionEngine()


async def search_skill(query: str, stack_tags: list[str] | None = None) -> str:
    """Search for current best practices and skills from trusted sources.

    Args:
        query: The topic to search for (e.g., "Clean Architecture .NET 9").
        stack_tags: Optional technology tags to narrow search (e.g., ["dotnet", "csharp"]).

    Returns:
        Extracted skill content with patterns, rules, and examples.
    """
    return await _engine.resolve(query, stack_tags or [])

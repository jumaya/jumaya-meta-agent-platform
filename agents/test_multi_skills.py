import asyncio
import time
from shared.services.skill_resolution.engine import SkillResolutionEngine


async def test():
    engine = SkillResolutionEngine()

    queries = [
        ("Angular 18 standalone components best practices", ["angular", "typescript"]),
        ("OWASP top 10 security vulnerabilities prevention", ["security", "owasp"]),
        ("Docker multi-stage build optimization", ["docker", "devops"]),
    ]

    for query, tags in queries:
        print(f"\n{'='*60}")
        print(f"Query: {query}")
        print(f"Tags: {tags}")
        start = time.time()

        skill = await engine.resolve(query=query, stack_tags=tags)

        elapsed = time.time() - start
        print(f"Tiempo: {elapsed:.1f}s")
        print(f"Resultado ({len(skill)} chars):")
        print(skill[:300])
        print("...")

    # Verificar cache total
    from shared.services.persistence.mongodb import get_database
    db = await get_database()
    count = await db.skill_cache.count_documents({})
    print(f"\n{'='*60}")
    print(f"Total skills en cache: {count}")
    print("DONE")


asyncio.run(test())
import asyncio
from shared.services.skill_resolution.web_search import DuckDuckGoSearchProvider


async def test():
    search = DuckDuckGoSearchProvider()

    print("Buscando 'Clean Architecture .NET 9'...")
    results = await search.search(
        query="Clean Architecture best practices",
        stack_tags=["dotnet", "csharp"],
        max_results=5,
    )

    print(f"Resultados: {len(results)}\n")
    for i, r in enumerate(results, 1):
        print(f"  {i}. {r['title']}")
        print(f"     {r['url']}")
        print()

    if results:
        print(f"Descargando contenido de: {results[0]['url']}")
        content = await search.fetch_content(results[0]["url"])
        print(f"Contenido: {len(content)} caracteres")
        print(content[:300])

    print("\nDONE")


asyncio.run(test())
import asyncio
from shared.services.skill_resolution.web_search import DuckDuckGoSearchProvider


async def test():
    search = DuckDuckGoSearchProvider()

    # Test 1: Buscar "Clean Architecture .NET 9"
    print("=" * 60)
    print("TEST 1: Buscando 'Clean Architecture .NET 9'")
    print("=" * 60)

    results = await search.search(
        query="Clean Architecture best practices",
        stack_tags=["dotnet", "csharp"],
        max_results=5,
    )

    print(f"\nResultados: {len(results)}\n")
    for i, r in enumerate(results, 1):
        print(f"  {i}. {r['title']}")
        print(f"     URL: {r['url']}")
        print(f"     Snippet: {r['snippet'][:100]}...")
        print()

    # Test 2: Fetch content de la primera URL
    if results:
        print("=" * 60)
        print(f"TEST 2: Descargando contenido de: {results[0]['url']}")
        print("=" * 60)

        try:
            content = await search.fetch_content(results[0]["url"])
            print(f"\nContenido extraido: {len(content)} caracteres")
            print(f"Primeros 500 chars:\n")
            print(content[:500])
        except Exception as e:
            print(f"\nError al descargar: {e}")
            if len(results) > 1:
                print(f"\nIntentando con segunda URL: {results[1]['url']}")
                content = await search.fetch_content(results[1]["url"])
                print(f"Contenido: {len(content)} caracteres")
                print(content[:500])

    print("\n" + "=" * 60)
    print("DONE")


asyncio.run(test())
namespace MetaAgent.Scaffolder.A2A;

public class AgentCardProvider
{
    private readonly string _baseUrl;

    public AgentCardProvider(IConfiguration configuration)
    {
        _baseUrl = configuration["BaseUrl"] ?? "http://scaffolder-svc:8002";
    }

    public object GetAgentCard() => new
    {
        name = "scaffolder",
        description = "Generates complete project structures and scaffolding for any technology stack",
        version = "1.0.0",
        url = _baseUrl,
        capabilities = new
        {
            streaming = false,
            pushNotifications = false
        },
        skills = new[]
        {
            new
            {
                id = "scaffold_dotnet",
                name = "Scaffold .NET Clean Architecture",
                description = "Generates a .NET 9 solution with Clean Architecture layers",
                tags = new[] { "dotnet", "csharp", "clean-architecture" }
            },
            new
            {
                id = "scaffold_angular",
                name = "Scaffold Angular Standalone",
                description = "Generates Angular 18 standalone components project structure",
                tags = new[] { "angular", "typescript", "frontend" }
            }
        }
    };
}

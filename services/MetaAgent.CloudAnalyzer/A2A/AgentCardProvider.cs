namespace MetaAgent.CloudAnalyzer.A2A;

public class AgentCardProvider
{
    private readonly string _baseUrl;

    public AgentCardProvider(IConfiguration configuration)
    {
        _baseUrl = configuration["BaseUrl"] ?? "http://cloud-analyzer-svc:8006";
    }

    public object GetAgentCard() => new
    {
        name = "cloud_analyzer",
        description = "Analyzes architecture profiles and estimates monthly cloud hosting costs across Azure, AWS, and Hostinger",
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
                id = "estimate_costs",
                name = "Estimate Cloud Costs",
                description = "Calculates monthly cost estimates across cloud providers for a given architecture",
                tags = new[] { "cloud", "cost", "azure", "aws", "hostinger" }
            }
        }
    };
}

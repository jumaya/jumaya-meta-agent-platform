namespace MetaAgent.CloudAnalyzer.Providers;

public class AzurePricingProvider(IHttpClientFactory httpClientFactory, ILogger<AzurePricingProvider> logger) : ICloudPricingProvider
{
    public string ProviderName => "Azure";

    public async Task<PricingResult> GetPricingAsync(ArchitectureProfile profile)
    {
        var breakdown = new Dictionary<string, decimal>();

        // Azure Container Apps for microservices
        decimal appCost = profile.MicroserviceCount * 15m;
        breakdown["Container Apps"] = appCost;

        if (profile.RequiresDatabase)
        {
            breakdown["Azure SQL / Cosmos DB"] = profile.ExpectedUsers > 10000 ? 150m : 50m;
        }

        if (profile.RequiresCdn)
        {
            breakdown["Azure CDN"] = 10m;
        }

        if (profile.RequiresCache)
        {
            breakdown["Azure Cache for Redis"] = 30m;
        }

        breakdown["Load Balancer"] = 20m;
        breakdown["Storage & Monitoring"] = 15m;

        var total = breakdown.Values.Sum();

        logger.LogDebug("Azure estimate: ${Total}/month", total);

        return await Task.FromResult(new PricingResult(
            Provider: ProviderName,
            MonthlyEstimateUsd: total,
            Tier: total < 100 ? "Basic" : total < 500 ? "Standard" : "Premium",
            Breakdown: breakdown));
    }
}

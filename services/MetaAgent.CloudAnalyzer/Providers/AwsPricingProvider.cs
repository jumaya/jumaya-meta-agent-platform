namespace MetaAgent.CloudAnalyzer.Providers;

public class AwsPricingProvider(ILogger<AwsPricingProvider> logger) : ICloudPricingProvider
{
    public string ProviderName => "AWS";

    public async Task<PricingResult> GetPricingAsync(ArchitectureProfile profile)
    {
        var breakdown = new Dictionary<string, decimal>();

        // ECS Fargate for containers
        decimal appCost = profile.MicroserviceCount * 12m;
        breakdown["ECS Fargate"] = appCost;

        if (profile.RequiresDatabase)
        {
            breakdown["RDS / DynamoDB"] = profile.ExpectedUsers > 10000 ? 130m : 45m;
        }

        if (profile.RequiresCdn)
        {
            breakdown["CloudFront"] = 8m;
        }

        if (profile.RequiresCache)
        {
            breakdown["ElastiCache"] = 25m;
        }

        breakdown["ALB"] = 18m;
        breakdown["S3 & CloudWatch"] = 12m;

        var total = breakdown.Values.Sum();

        logger.LogDebug("AWS estimate: ${Total}/month", total);

        return await Task.FromResult(new PricingResult(
            Provider: ProviderName,
            MonthlyEstimateUsd: total,
            Tier: total < 100 ? "Basic" : total < 500 ? "Standard" : "Premium",
            Breakdown: breakdown));
    }
}

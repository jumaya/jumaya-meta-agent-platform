namespace MetaAgent.CloudAnalyzer.Providers;

public class HostingerPricingProvider(ILogger<HostingerPricingProvider> logger) : ICloudPricingProvider
{
    public string ProviderName => "Hostinger";

    public async Task<PricingResult> GetPricingAsync(ArchitectureProfile profile)
    {
        var breakdown = new Dictionary<string, decimal>();

        // Hostinger VPS plans
        if (profile.MicroserviceCount <= 2 && profile.ExpectedUsers <= 5000)
        {
            breakdown["VPS KVM 2"] = 7.99m;
        }
        else if (profile.MicroserviceCount <= 5 && profile.ExpectedUsers <= 20000)
        {
            breakdown["VPS KVM 4"] = 15.99m;
        }
        else
        {
            breakdown["VPS KVM 8"] = 29.99m;
        }

        if (profile.RequiresDatabase)
        {
            breakdown["Managed Database"] = 9.99m;
        }

        if (profile.RequiresCdn)
        {
            breakdown["Cloudflare CDN (free tier)"] = 0m;
        }

        breakdown["Domain & SSL"] = 2m;

        var total = breakdown.Values.Sum();

        logger.LogDebug("Hostinger estimate: ${Total}/month", total);

        return await Task.FromResult(new PricingResult(
            Provider: ProviderName,
            MonthlyEstimateUsd: total,
            Tier: "VPS",
            Breakdown: breakdown));
    }
}

using MetaAgent.CloudAnalyzer.Providers;

namespace MetaAgent.CloudAnalyzer.Analysis;

public class CostProjectionEngine(IEnumerable<ICloudPricingProvider> providers)
{
    public async Task<IEnumerable<object>> CalculateAsync(ArchitectureProfile profile)
    {
        var tasks = providers.Select(async p =>
        {
            var result = await p.GetPricingAsync(profile);
            return (object)new
            {
                provider = result.Provider,
                monthly_usd = Math.Round(result.MonthlyEstimateUsd, 2),
                tier = result.Tier,
                breakdown = result.Breakdown
            };
        });

        return await Task.WhenAll(tasks);
    }
}

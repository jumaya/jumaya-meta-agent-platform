namespace MetaAgent.CloudAnalyzer.Providers;

public record ArchitectureProfile(
    string Pattern,
    int ExpectedUsers,
    int MicroserviceCount,
    bool RequiresDatabase,
    bool RequiresCdn,
    bool RequiresCache);

public record PricingResult(
    string Provider,
    decimal MonthlyEstimateUsd,
    string Tier,
    Dictionary<string, decimal> Breakdown);

public interface ICloudPricingProvider
{
    string ProviderName { get; }
    Task<PricingResult> GetPricingAsync(ArchitectureProfile profile);
}

using System.Text.Json;
using MetaAgent.CloudAnalyzer.Providers;

namespace MetaAgent.CloudAnalyzer.Analysis;

public class ArchitectureCostMapper
{
    public ArchitectureProfile MapFromRequest(JsonElement request)
    {
        var pattern = GetString(request, "architecture_pattern", "monolith");
        var users = GetInt(request, "expected_users", 1000);
        var services = GetInt(request, "microservice_count",
            pattern.Contains("microservice", StringComparison.OrdinalIgnoreCase) ? 5 : 1);

        return new ArchitectureProfile(
            Pattern: pattern,
            ExpectedUsers: users,
            MicroserviceCount: services,
            RequiresDatabase: GetBool(request, "requires_database", true),
            RequiresCdn: GetBool(request, "requires_cdn", false),
            RequiresCache: GetBool(request, "requires_cache",
                users > 5000));
    }

    private static string GetString(JsonElement el, string key, string defaultValue) =>
        el.TryGetProperty(key, out var prop) ? prop.GetString() ?? defaultValue : defaultValue;

    private static int GetInt(JsonElement el, string key, int defaultValue) =>
        el.TryGetProperty(key, out var prop) && prop.TryGetInt32(out var val) ? val : defaultValue;

    private static bool GetBool(JsonElement el, string key, bool defaultValue) =>
        el.TryGetProperty(key, out var prop) ? prop.GetBoolean() : defaultValue;
}

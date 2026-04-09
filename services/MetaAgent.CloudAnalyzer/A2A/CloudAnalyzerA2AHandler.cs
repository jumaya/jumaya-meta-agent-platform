using System.Text.Json;
using MetaAgent.CloudAnalyzer.Analysis;

namespace MetaAgent.CloudAnalyzer.A2A;

public class CloudAnalyzerA2AHandler(
    CostProjectionEngine costEngine,
    ArchitectureCostMapper costMapper,
    ILogger<CloudAnalyzerA2AHandler> logger)
{
    public async Task HandleAsync(HttpContext context)
    {
        using var reader = new StreamReader(context.Request.Body);
        var body = await reader.ReadToEndAsync();
        var request = JsonSerializer.Deserialize<JsonElement>(body);

        var architectureProfile = costMapper.MapFromRequest(request);
        logger.LogInformation("Analyzing costs for architecture: {Pattern}", architectureProfile.Pattern);

        var projections = await costEngine.CalculateAsync(architectureProfile);

        context.Response.ContentType = "application/json";
        await context.Response.WriteAsJsonAsync(new
        {
            status = "success",
            architecture = architectureProfile.Pattern,
            monthly_estimates = projections
        });
    }
}

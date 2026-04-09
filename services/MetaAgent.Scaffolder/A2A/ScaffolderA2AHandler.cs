using System.Text.Json;
using MetaAgent.Scaffolder.Templates;

namespace MetaAgent.Scaffolder.A2A;

public class ScaffolderA2AHandler(IEnumerable<IProjectTemplate> templates, ILogger<ScaffolderA2AHandler> logger)
{
    public async Task HandleAsync(HttpContext context)
    {
        using var reader = new StreamReader(context.Request.Body);
        var body = await reader.ReadToEndAsync();
        var request = JsonSerializer.Deserialize<JsonElement>(body);

        var stack = request.TryGetProperty("stack", out var stackProp)
            ? stackProp.GetString() ?? "dotnet"
            : "dotnet";

        var projectContext = request.TryGetProperty("context", out var ctxProp)
            ? ctxProp
            : default;

        logger.LogInformation("Scaffolding project for stack: {Stack}", stack);

        var template = templates.FirstOrDefault(t => t.Supports(stack))
            ?? templates.First();

        var files = await template.GenerateAsync(projectContext);

        context.Response.ContentType = "application/json";
        await context.Response.WriteAsJsonAsync(new
        {
            status = "success",
            files_generated = files.Length,
            files = files.Select(f => new { f.Path, preview = f.Content[..Math.Min(200, f.Content.Length)] })
        });
    }
}

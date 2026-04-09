using System.Text.Json;

namespace MetaAgent.Scaffolder.Templates;

public record FileResult(string Path, string Content);

public interface IProjectTemplate
{
    bool Supports(string stack);
    Task<FileResult[]> GenerateAsync(JsonElement context);
}

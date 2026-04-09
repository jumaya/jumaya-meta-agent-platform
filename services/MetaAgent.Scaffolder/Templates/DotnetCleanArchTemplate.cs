using System.Text.Json;
using MetaAgent.Scaffolder.Generators;

namespace MetaAgent.Scaffolder.Templates;

public class DotnetCleanArchTemplate(
    SolutionGenerator solutionGen,
    ProjectGenerator projectGen,
    ConfigGenerator configGen) : IProjectTemplate
{
    public bool Supports(string stack) =>
        stack.Contains("dotnet", StringComparison.OrdinalIgnoreCase) ||
        stack.Contains("csharp", StringComparison.OrdinalIgnoreCase);

    public async Task<FileResult[]> GenerateAsync(JsonElement context)
    {
        var projectName = context.TryGetProperty("name", out var nameProp)
            ? nameProp.GetString() ?? "MyApp"
            : "MyApp";

        var files = new List<FileResult>
        {
            new($"{projectName}.sln", solutionGen.Generate(projectName)),
            new($"src/{projectName}.Domain/{projectName}.Domain.csproj",
                projectGen.GenerateDomain(projectName)),
            new($"src/{projectName}.Application/{projectName}.Application.csproj",
                projectGen.GenerateApplication(projectName)),
            new($"src/{projectName}.Infrastructure/{projectName}.Infrastructure.csproj",
                projectGen.GenerateInfrastructure(projectName)),
            new($"src/{projectName}.API/{projectName}.API.csproj",
                projectGen.GenerateApi(projectName)),
            new($"src/{projectName}.API/Program.cs",
                configGen.GenerateProgram(projectName)),
            new($"src/{projectName}.API/appsettings.json",
                configGen.GenerateAppSettings()),
            new($"src/{projectName}.API/Dockerfile",
                configGen.GenerateDockerfile(projectName)),
        };

        return await Task.FromResult(files.ToArray());
    }
}

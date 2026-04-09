namespace MetaAgent.Scaffolder.Generators;

public class SolutionGenerator
{
    public string Generate(string projectName)
    {
        var guid1 = Guid.NewGuid().ToString().ToUpper();
        var guid2 = Guid.NewGuid().ToString().ToUpper();
        var guid3 = Guid.NewGuid().ToString().ToUpper();
        var guid4 = Guid.NewGuid().ToString().ToUpper();

        return $"""
            Microsoft Visual Studio Solution File, Format Version 12.00
            # Visual Studio Version 17
            VisualStudioVersion = 17.9.34622.214
            Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{projectName}.Domain", "src\{projectName}.Domain\{projectName}.Domain.csproj", "{{{guid1}}}"
            EndProject
            Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{projectName}.Application", "src\{projectName}.Application\{projectName}.Application.csproj", "{{{guid2}}}"
            EndProject
            Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{projectName}.Infrastructure", "src\{projectName}.Infrastructure\{projectName}.Infrastructure.csproj", "{{{guid3}}}"
            EndProject
            Project("{{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}}") = "{projectName}.API", "src\{projectName}.API\{projectName}.API.csproj", "{{{guid4}}}"
            EndProject
            Global
            	GlobalSection(SolutionConfigurationPlatforms) = preSolution
            		Debug|Any CPU = Debug|Any CPU
            		Release|Any CPU = Release|Any CPU
            	EndGlobalSection
            EndGlobal
            """;
    }
}

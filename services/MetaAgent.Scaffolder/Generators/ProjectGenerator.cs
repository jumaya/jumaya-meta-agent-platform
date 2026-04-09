namespace MetaAgent.Scaffolder.Generators;

public class ProjectGenerator
{
    public string GenerateDomain(string projectName) => $"""
        <Project Sdk="Microsoft.NET.Sdk">
          <PropertyGroup>
            <TargetFramework>net9.0</TargetFramework>
            <Nullable>enable</Nullable>
            <ImplicitUsings>enable</ImplicitUsings>
          </PropertyGroup>
        </Project>
        """;

    public string GenerateApplication(string projectName) => $"""
        <Project Sdk="Microsoft.NET.Sdk">
          <PropertyGroup>
            <TargetFramework>net9.0</TargetFramework>
            <Nullable>enable</Nullable>
            <ImplicitUsings>enable</ImplicitUsings>
          </PropertyGroup>
          <ItemGroup>
            <PackageReference Include="MediatR" Version="12.4.0" />
            <PackageReference Include="FluentValidation" Version="11.10.0" />
            <ProjectReference Include="..\{projectName}.Domain\{projectName}.Domain.csproj" />
          </ItemGroup>
        </Project>
        """;

    public string GenerateInfrastructure(string projectName) => $"""
        <Project Sdk="Microsoft.NET.Sdk">
          <PropertyGroup>
            <TargetFramework>net9.0</TargetFramework>
            <Nullable>enable</Nullable>
            <ImplicitUsings>enable</ImplicitUsings>
          </PropertyGroup>
          <ItemGroup>
            <PackageReference Include="Microsoft.EntityFrameworkCore" Version="9.0.0" />
            <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="9.0.0" />
            <ProjectReference Include="..\{projectName}.Application\{projectName}.Application.csproj" />
          </ItemGroup>
        </Project>
        """;

    public string GenerateApi(string projectName) => $"""
        <Project Sdk="Microsoft.NET.Sdk.Web">
          <PropertyGroup>
            <TargetFramework>net9.0</TargetFramework>
            <Nullable>enable</Nullable>
            <ImplicitUsings>enable</ImplicitUsings>
          </PropertyGroup>
          <ItemGroup>
            <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="9.0.0" />
            <PackageReference Include="Swashbuckle.AspNetCore" Version="6.9.0" />
            <ProjectReference Include="..\{projectName}.Application\{projectName}.Application.csproj" />
            <ProjectReference Include="..\{projectName}.Infrastructure\{projectName}.Infrastructure.csproj" />
          </ItemGroup>
        </Project>
        """;
}

namespace MetaAgent.Scaffolder.Generators;

public class ConfigGenerator
{
    public string GenerateProgram(string projectName) => $"""
        var builder = WebApplication.CreateBuilder(args);

        builder.Services.AddEndpointsApiExplorer();
        builder.Services.AddSwaggerGen();
        builder.Services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(
            typeof({projectName}.Application.AssemblyReference).Assembly));

        var app = builder.Build();

        if (app.Environment.IsDevelopment())
        {{
            app.UseSwagger();
            app.UseSwaggerUI();
        }}

        app.UseHttpsRedirection();
        app.MapGet("/health", () => Results.Ok(new {{ status = "healthy" }}));

        app.Run();
        """;

    public string GenerateAppSettings() => """
        {
          "Logging": {
            "LogLevel": {
              "Default": "Information",
              "Microsoft.AspNetCore": "Warning"
            }
          },
          "AllowedHosts": "*",
          "ConnectionStrings": {
            "DefaultConnection": ""
          }
        }
        """;

    public string GenerateDockerfile(string projectName) => $"""
        FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
        WORKDIR /src

        COPY ["{projectName}.API/{projectName}.API.csproj", "{projectName}.API/"]
        COPY ["{projectName}.Application/{projectName}.Application.csproj", "{projectName}.Application/"]
        COPY ["{projectName}.Domain/{projectName}.Domain.csproj", "{projectName}.Domain/"]
        COPY ["{projectName}.Infrastructure/{projectName}.Infrastructure.csproj", "{projectName}.Infrastructure/"]
        RUN dotnet restore "{projectName}.API/{projectName}.API.csproj"

        COPY . .
        WORKDIR "/src/{projectName}.API"
        RUN dotnet build -c Release -o /app/build

        FROM build AS publish
        RUN dotnet publish -c Release -o /app/publish /p:UseAppHost=false

        FROM mcr.microsoft.com/dotnet/aspnet:9.0 AS final
        WORKDIR /app
        EXPOSE 8080
        COPY --from=publish /app/publish .
        ENTRYPOINT ["dotnet", "{projectName}.API.dll"]
        """;
}

using MetaAgent.CloudAnalyzer.A2A;
using MetaAgent.CloudAnalyzer.Analysis;
using MetaAgent.CloudAnalyzer.Providers;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddHttpClient();
builder.Services.AddSingleton<ICloudPricingProvider, AzurePricingProvider>();
builder.Services.AddSingleton<ICloudPricingProvider, AwsPricingProvider>();
builder.Services.AddSingleton<ICloudPricingProvider, HostingerPricingProvider>();
builder.Services.AddSingleton<CostProjectionEngine>();
builder.Services.AddSingleton<ArchitectureCostMapper>();
builder.Services.AddSingleton<AgentCardProvider>();
builder.Services.AddSingleton<CloudAnalyzerA2AHandler>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapGet("/health", () => Results.Ok(new { status = "healthy", service = "MetaAgent.CloudAnalyzer" }));

app.MapGet("/.well-known/agent.json", (AgentCardProvider provider) =>
    Results.Json(provider.GetAgentCard()));

app.MapPost("/a2a", async (CloudAnalyzerA2AHandler handler, HttpContext ctx) =>
    await handler.HandleAsync(ctx));

app.Run();

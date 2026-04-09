using MetaAgent.Scaffolder.A2A;
using MetaAgent.Scaffolder.Templates;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddSingleton<IProjectTemplate, DotnetCleanArchTemplate>();
builder.Services.AddSingleton<IProjectTemplate, AngularStandaloneTemplate>();
builder.Services.AddSingleton<AgentCardProvider>();
builder.Services.AddSingleton<ScaffolderA2AHandler>();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.MapGet("/health", () => Results.Ok(new { status = "healthy", service = "MetaAgent.Scaffolder" }));

app.MapGet("/.well-known/agent.json", (AgentCardProvider provider) =>
    Results.Json(provider.GetAgentCard()));

app.MapPost("/a2a", async (ScaffolderA2AHandler handler, HttpContext ctx) =>
    await handler.HandleAsync(ctx));

app.Run();

using System.Text.Json;

namespace MetaAgent.Scaffolder.Templates;

public class AngularStandaloneTemplate : IProjectTemplate
{
    public bool Supports(string stack) =>
        stack.Contains("angular", StringComparison.OrdinalIgnoreCase);

    public async Task<FileResult[]> GenerateAsync(JsonElement context)
    {
        var projectName = context.TryGetProperty("name", out var nameProp)
            ? nameProp.GetString() ?? "my-app"
            : "my-app";

        var kebabName = ToKebabCase(projectName);

        var files = new[]
        {
            new FileResult("package.json", GeneratePackageJson(kebabName)),
            new FileResult("angular.json", GenerateAngularJson(kebabName)),
            new FileResult("tsconfig.json", GenerateTsConfig()),
            new FileResult($"src/app/app.component.ts", GenerateAppComponent(projectName)),
            new FileResult($"src/app/app.routes.ts", GenerateAppRoutes()),
            new FileResult($"src/app/app.config.ts", GenerateAppConfig()),
            new FileResult($"src/main.ts", GenerateMain()),
            new FileResult($"src/index.html", GenerateIndexHtml(kebabName)),
        };

        return await Task.FromResult(files);
    }

    private static string ToKebabCase(string name) =>
        string.Concat(name.Select((c, i) =>
            i > 0 && char.IsUpper(c) ? $"-{char.ToLower(c)}" : char.ToLower(c).ToString()));

    private static string GeneratePackageJson(string name) => $$"""
        {
          "name": "{{name}}",
          "version": "0.0.0",
          "scripts": {
            "ng": "ng",
            "start": "ng serve",
            "build": "ng build",
            "test": "ng test"
          },
          "dependencies": {
            "@angular/animations": "^18.0.0",
            "@angular/common": "^18.0.0",
            "@angular/compiler": "^18.0.0",
            "@angular/core": "^18.0.0",
            "@angular/forms": "^18.0.0",
            "@angular/platform-browser": "^18.0.0",
            "@angular/platform-browser-dynamic": "^18.0.0",
            "@angular/router": "^18.0.0",
            "rxjs": "~7.8.0",
            "zone.js": "~0.14.3"
          },
          "devDependencies": {
            "@angular-devkit/build-angular": "^18.0.0",
            "@angular/cli": "^18.0.0",
            "@angular/compiler-cli": "^18.0.0",
            "typescript": "~5.4.2"
          }
        }
        """;

    private static string GenerateAngularJson(string name) => $$"""
        {
          "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
          "version": 1,
          "newProjectRoot": "projects",
          "projects": {
            "{{name}}": {
              "projectType": "application",
              "architect": {
                "build": {
                  "builder": "@angular-devkit/build-angular:application",
                  "options": {
                    "outputPath": "dist/{{name}}",
                    "index": "src/index.html",
                    "browser": "src/main.ts",
                    "polyfills": ["zone.js"]
                  }
                }
              }
            }
          }
        }
        """;

    private static string GenerateTsConfig() => """
        {
          "compileOnSave": false,
          "compilerOptions": {
            "outDir": "./dist/out-tsc",
            "strict": true,
            "noImplicitOverride": true,
            "noPropertyAccessFromIndexSignature": true,
            "noImplicitReturns": true,
            "noFallthroughCasesInSwitch": true,
            "esModuleInterop": true,
            "skipLibCheck": true,
            "isolatedModules": true,
            "experimentalDecorators": true,
            "moduleResolution": "bundler",
            "importHelpers": true,
            "target": "ES2022",
            "module": "ES2022",
            "lib": ["ES2022", "dom"]
          },
          "angularCompilerOptions": {
            "enableI18nLegacyMessageIdFormat": false,
            "strictInjectionParameters": true,
            "strictInputAccessModifiers": true,
            "strictTemplates": true
          }
        }
        """;

    private static string GenerateAppComponent(string name) => $$"""
        import { Component } from '@angular/core';
        import { RouterOutlet } from '@angular/router';

        @Component({
          selector: 'app-root',
          standalone: true,
          imports: [RouterOutlet],
          template: `
            <h1>Welcome to {{name}}</h1>
            <router-outlet />
          `,
        })
        export class AppComponent {
          title = '{{name}}';
        }
        """;

    private static string GenerateAppRoutes() => """
        import { Routes } from '@angular/router';

        export const routes: Routes = [];
        """;

    private static string GenerateAppConfig() => """
        import { ApplicationConfig } from '@angular/core';
        import { provideRouter } from '@angular/router';
        import { routes } from './app.routes';

        export const appConfig: ApplicationConfig = {
          providers: [provideRouter(routes)]
        };
        """;

    private static string GenerateMain() => """
        import { bootstrapApplication } from '@angular/platform-browser';
        import { appConfig } from './app/app.config';
        import { AppComponent } from './app/app.component';

        bootstrapApplication(AppComponent, appConfig)
          .catch((err) => console.error(err));
        """;

    private static string GenerateIndexHtml(string name) => $$"""
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <title>{{name}}</title>
          <base href="/">
          <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
          <app-root></app-root>
        </body>
        </html>
        """;
}

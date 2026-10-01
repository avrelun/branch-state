import { defineConfig } from 'orval';

export default defineConfig({
  health: {
    input: { target: './openapi/health.json' },
    output: {
      mode: 'single',
      client: 'angular',
      target: './libs/api-client/src/lib/generated/health.ts',
      schemas: {
        type: 'zod',
        path: './libs/api-client/src/lib/generated/model',
      },
      formatter: 'prettier',
      override: {
        angular: {
          provideIn: 'root',
          retrievalClient: 'httpClient',
          runtimeValidation: true,
          baseUrl: { apiId: 'branchstate' },
        },
      },
    },
  },
});

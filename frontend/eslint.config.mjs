import nx from '@nx/eslint-plugin';

export default [
  ...nx.configs['flat/base'],
  ...nx.configs['flat/typescript'],
  ...nx.configs['flat/javascript'],
  {
    files: ['libs/api-client/src/lib/generated/**/*.ts'],
    rules: { '@typescript-eslint/no-inferrable-types': 'off' },
  },
  {
    ignores: [
      '**/dist/**',
      '**/node_modules/**',
      '.nx/**',
      '.angular/**',
      'coverage/**',
    ],
  },
  {
    files: ['**/*.ts', '**/*.js', '**/*.mjs'],
    rules: {
      '@nx/enforce-module-boundaries': [
        'error',
        {
          enforceBuildableLibDependency: true,
          allow: ['^.*/eslint(\\.base)?\\.config\\.[cm]?[jt]s$'],
          depConstraints: [
            {
              sourceTag: 'type:app',
              onlyDependOnLibsWithTags: [
                'type:feature',
                'type:ui',
                'type:data-access',
                'type:domain',
                'type:platform',
                'type:api-client',
              ],
            },
            {
              sourceTag: 'type:feature',
              onlyDependOnLibsWithTags: [
                'type:ui',
                'type:data-access',
                'type:domain',
              ],
            },
            {
              sourceTag: 'type:ui',
              onlyDependOnLibsWithTags: ['type:ui', 'type:domain'],
            },
            {
              sourceTag: 'type:data-access',
              onlyDependOnLibsWithTags: [
                'type:domain',
                'type:api-client',
                'type:platform',
              ],
            },
            {
              sourceTag: 'type:domain',
              onlyDependOnLibsWithTags: ['type:domain'],
              bannedExternalImports: [
                '@angular/*',
                'rxjs',
                'axios',
                'ky',
                'node:http',
                'node:https',
              ],
            },
            {
              sourceTag: 'type:api-client',
              onlyDependOnLibsWithTags: ['type:api-client', 'type:platform'],
            },
            {
              sourceTag: 'type:platform',
              onlyDependOnLibsWithTags: ['type:platform'],
            },
            {
              sourceTag: 'scope:platform',
              onlyDependOnLibsWithTags: ['scope:platform', 'scope:shared'],
            },
          ],
        },
      ],
    },
  },
];

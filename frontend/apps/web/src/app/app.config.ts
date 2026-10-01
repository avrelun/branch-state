import { provideHttpClient } from '@angular/common/http';
import {
  ApplicationConfig,
  provideBrowserGlobalErrorListeners,
} from '@angular/core';
import { provideBranchstateBaseUrl } from '@branchstate/api-client';
import { RUNTIME_CONFIG, RuntimeConfig } from '@branchstate/platform';

export function createAppConfig(config: RuntimeConfig): ApplicationConfig {
  return {
    providers: [
      provideBrowserGlobalErrorListeners(),
      provideHttpClient(),
      { provide: RUNTIME_CONFIG, useValue: config },
      provideBranchstateBaseUrl(config.apiBaseUrl),
    ],
  };
}

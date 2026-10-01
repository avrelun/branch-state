import { InjectionToken } from '@angular/core';

export interface RuntimeConfig {
  readonly apiBaseUrl: string;
}

export const RUNTIME_CONFIG = new InjectionToken<RuntimeConfig>(
  'Branchstate runtime configuration',
);

export function parseRuntimeConfig(value: unknown): RuntimeConfig {
  if (typeof value !== 'object' || value === null || Array.isArray(value)) {
    throw new Error('Runtime configuration must be a JSON object.');
  }

  const apiBaseUrl = (value as Record<string, unknown>)['apiBaseUrl'];
  const invalid = () =>
    new Error(
      'Runtime configuration apiBaseUrl must be a root-relative path or an HTTP(S) URL without credentials, a query, or a fragment.',
    );

  if (
    typeof apiBaseUrl !== 'string' ||
    apiBaseUrl.length === 0 ||
    /[\s\\?#]/u.test(apiBaseUrl) ||
    apiBaseUrl
      .split('')
      .some(
        (character) =>
          character.charCodeAt(0) < 32 || character.charCodeAt(0) === 127,
      ) ||
    /%(?![0-9a-f]{2})/i.test(apiBaseUrl)
  ) {
    throw invalid();
  }

  if (apiBaseUrl.startsWith('/')) {
    if (apiBaseUrl.startsWith('//')) {
      throw invalid();
    }

    return { apiBaseUrl: apiBaseUrl.replace(/\/+$/, '') };
  }

  if (!/^https?:\/\/[^/@]+(?:\/|$)/i.test(apiBaseUrl)) {
    throw invalid();
  }

  let url: URL;
  try {
    url = new URL(apiBaseUrl);
  } catch {
    throw invalid();
  }

  if (url.username || url.password || !url.hostname) {
    throw invalid();
  }

  return { apiBaseUrl: url.origin + url.pathname.replace(/\/+$/, '') };
}

export async function loadRuntimeConfig(): Promise<RuntimeConfig> {
  let response: Response;
  try {
    response = await fetch('/config.json', {
      cache: 'no-store',
      credentials: 'same-origin',
    });
  } catch {
    throw new Error('Unable to fetch runtime configuration from /config.json.');
  }

  if (!response.ok) {
    throw new Error(
      `Runtime configuration request failed (HTTP ${response.status}).`,
    );
  }

  let value: unknown;
  try {
    value = await response.json();
  } catch {
    throw new Error('Runtime configuration is not valid JSON.');
  }

  return parseRuntimeConfig(value);
}

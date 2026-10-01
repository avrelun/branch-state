import { loadRuntimeConfig, parseRuntimeConfig } from '@branchstate/platform';

describe('Runtime configuration', () => {
  afterEach(() => vi.unstubAllGlobals());

  it.each([
    ['/api/', '/api'],
    ['/', ''],
    ['https://API.example:8443/api/', 'https://api.example:8443/api'],
    ['http://127.0.0.1:8000/', 'http://127.0.0.1:8000'],
  ])('accepts and normalizes the API base URL %s', (input, expected) => {
    expect(parseRuntimeConfig({ apiBaseUrl: input })).toEqual({
      apiBaseUrl: expected,
    });
  });

  it.each([
    '//backend.example/api',
    'javascript:alert(1)',
    'https://user:password@backend.example/api',
    '/api?token=secret',
    '/api#fragment',
    '/api\\other',
    '/api/%invalid',
    '',
  ])('rejects the unsafe API base URL %s', (apiBaseUrl) => {
    expect(() => parseRuntimeConfig({ apiBaseUrl })).toThrow('apiBaseUrl');
  });

  it.each([
    { description: 'null', value: null },
    { description: 'an array', value: [] },
    { description: 'a bare URL', value: 'https://backend.example' },
    { description: 'a missing API base URL', value: {} },
    { description: 'a numeric API base URL', value: { apiBaseUrl: 123 } },
  ])('rejects malformed runtime configuration: $description', ({ value }) => {
    expect(() => parseRuntimeConfig(value)).toThrow();
  });

  it('loads deployment configuration from the current origin without a stale cache', async () => {
    const fetchConfig = vi
      .fn<typeof fetch>()
      .mockResolvedValue(
        Response.json({ apiBaseUrl: 'https://backend.example/api/' }),
      );
    vi.stubGlobal('fetch', fetchConfig);

    await expect(loadRuntimeConfig()).resolves.toEqual({
      apiBaseUrl: 'https://backend.example/api',
    });
    expect(fetchConfig).toHaveBeenCalledExactlyOnceWith('/config.json', {
      cache: 'no-store',
      credentials: 'same-origin',
    });
  });

  it('reports an unavailable configuration endpoint', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn<typeof fetch>().mockRejectedValue(new TypeError('Network failure')),
    );

    await expect(loadRuntimeConfig()).rejects.toThrow(
      'Unable to fetch runtime configuration from /config.json.',
    );
  });

  it('rejects an HTTP failure before treating the response as configuration', async () => {
    vi.stubGlobal(
      'fetch',
      vi
        .fn<typeof fetch>()
        .mockResolvedValue(
          new Response('Service unavailable', { status: 503 }),
        ),
    );

    await expect(loadRuntimeConfig()).rejects.toThrow('HTTP 503');
  });

  it('rejects invalid JSON instead of silently using a default API origin', async () => {
    vi.stubGlobal(
      'fetch',
      vi.fn<typeof fetch>().mockResolvedValue(
        new Response('{"apiBaseUrl":', {
          headers: { 'Content-Type': 'application/json' },
        }),
      ),
    );

    await expect(loadRuntimeConfig()).rejects.toThrow(
      'Runtime configuration is not valid JSON.',
    );
  });

  it('validates the downloaded API origin before accepting configuration', async () => {
    vi.stubGlobal(
      'fetch',
      vi
        .fn<typeof fetch>()
        .mockResolvedValue(Response.json({ apiBaseUrl: '//backend.example' })),
    );

    await expect(loadRuntimeConfig()).rejects.toThrow('apiBaseUrl');
  });
});

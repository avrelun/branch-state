import {
  HttpTestingController,
  provideHttpClientTesting,
} from '@angular/common/http/testing';
import { TestBed } from '@angular/core/testing';
import { App } from './app';
import { createAppConfig } from './app.config';

describe('Workspace connection', () => {
  let http: HttpTestingController;

  afterEach(() => http.verify());

  function renderApp(apiBaseUrl = '/api') {
    TestBed.configureTestingModule({
      imports: [App],
      providers: [
        ...createAppConfig({ apiBaseUrl }).providers,
        provideHttpClientTesting(),
      ],
    });

    http = TestBed.inject(HttpTestingController);
    const fixture = TestBed.createComponent(App);
    fixture.detectChanges();
    const page = fixture.nativeElement as HTMLElement;
    const button = page.querySelector('button') as HTMLButtonElement;

    return { fixture, page, button };
  }

  it('shows loading and prevents another check while the request is pending', () => {
    const { page, button } = renderApp();
    const request = http.expectOne('/api/health');

    expect(request.request.method).toBe('GET');
    expect(page.querySelector('.state-title')?.textContent).toBe(
      'Checking connection…',
    );
    expect(page.querySelector('section')?.getAttribute('aria-busy')).toBe(
      'true',
    );
    expect(button.disabled).toBe(true);

    button.click();
    http.expectNone('/api/health');
    request.flush({ status: 'ok' });
  });

  it('shows that the service is connected after a valid response', () => {
    const { fixture, page, button } = renderApp();

    http.expectOne('/api/health').flush({ status: 'ok' });
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe('Connected');
    expect(page.querySelector('section')?.getAttribute('aria-busy')).toBe(
      'false',
    );
    expect(button.disabled).toBe(false);
    expect(button.textContent).toContain('Check connection');
  });

  it('offers a retry when the service returns an HTTP error', () => {
    const { fixture, page, button } = renderApp();

    http.expectOne('/api/health').flush(null, {
      status: 503,
      statusText: 'Service Unavailable',
    });
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe(
      'Connection unavailable',
    );
    expect(page.querySelector('.state-detail')?.textContent).toContain(
      'The service is unavailable.',
    );
    expect(button.disabled).toBe(false);
    expect(button.textContent).toContain('Try again');
  });

  it('explains when the service cannot be reached', () => {
    const { fixture, page } = renderApp();

    http.expectOne('/api/health').error(new ProgressEvent('error'));
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe(
      'Connection unavailable',
    );
    expect(page.querySelector('.state-detail')?.textContent).toContain(
      'Unable to reach the service.',
    );
  });

  it('rejects a malformed successful response through the generated validation', () => {
    const { fixture, page } = renderApp();

    http.expectOne('/api/health').flush({ status: 'wrong' });
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe(
      'Connection unavailable',
    );
    expect(page.querySelector('.state-detail')?.textContent).toContain(
      'The service returned an unexpected response.',
    );
  });

  it('returns to loading on retry and recovers after the service becomes available', () => {
    const { fixture, page, button } = renderApp();

    http.expectOne('/api/health').flush(null, {
      status: 503,
      statusText: 'Service Unavailable',
    });
    fixture.detectChanges();
    button.click();
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe(
      'Checking connection…',
    );
    expect(button.disabled).toBe(true);

    http.expectOne('/api/health').flush({ status: 'ok' });
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe('Connected');
    expect(button.disabled).toBe(false);
  });

  it('uses the API origin from runtime configuration without rebuilding the page', () => {
    const { fixture, page } = renderApp('https://backend.example/api/');

    http
      .expectOne('https://backend.example/api/health')
      .flush({ status: 'ok' });
    fixture.detectChanges();

    expect(page.querySelector('.state-title')?.textContent).toBe('Connected');
  });

  it('cancels a pending request when the page is destroyed', () => {
    const { fixture } = renderApp();
    const request = http.expectOne('/api/health');

    expect(request.cancelled).toBe(false);
    fixture.destroy();

    expect(request.cancelled).toBe(true);
  });
});

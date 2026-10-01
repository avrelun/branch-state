import { HttpErrorResponse } from '@angular/common/http';
import {
  ChangeDetectionStrategy,
  Component,
  DestroyRef,
  inject,
  signal,
} from '@angular/core';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { BranchstateService } from '@branchstate/api-client';
import { ZodError } from 'zod';

type ConnectionState =
  | { kind: 'loading' }
  | { kind: 'success' }
  | { kind: 'error'; message: string };

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class App {
  readonly state = signal<ConnectionState>({ kind: 'loading' });
  private readonly api = inject(BranchstateService);
  private readonly destroyRef = inject(DestroyRef);

  constructor() {
    this.checkConnection();
  }

  checkConnection(): void {
    this.state.set({ kind: 'loading' });
    this.api
      .getHealth({ timeout: 10_000 })
      .pipe(takeUntilDestroyed(this.destroyRef))
      .subscribe({
        next: () => this.state.set({ kind: 'success' }),
        error: (error: unknown) =>
          this.state.set({
            kind: 'error',
            message:
              error instanceof ZodError
                ? 'The service returned an unexpected response. Try again.'
                : error instanceof HttpErrorResponse && error.status === 0
                  ? 'Unable to reach the service. Check that it is running and try again.'
                  : 'The service is unavailable. Please try again.',
          }),
      });
  }
}

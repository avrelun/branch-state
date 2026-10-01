import { bootstrapApplication } from '@angular/platform-browser';
import { loadRuntimeConfig } from '@branchstate/platform';
import { createAppConfig } from './app/app.config';
import { App } from './app/app';

loadRuntimeConfig()
  .then((config) => bootstrapApplication(App, createAppConfig(config)))
  .catch(() => {
    const title = document.createElement('h1');
    title.textContent = "Branchstate couldn't start.";
    const message = document.createElement('p');
    message.textContent = 'Try reloading this page.';
    const alert = document.createElement('main');
    alert.setAttribute('role', 'alert');
    alert.append(title, message);
    document.querySelector('app-root')?.replaceChildren(alert);
  });

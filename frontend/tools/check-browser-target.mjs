import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';

const requireFromBuild = createRequire(
  import.meta.resolve('@angular/build/package.json'),
);
const browserslist = requireFromBuild('browserslist');
const workspaceRoot = fileURLToPath(new URL('../', import.meta.url));
const browsers = browserslist(undefined, { path: workspaceRoot });

if (
  browsers.length === 0 ||
  browsers.some((browser) => {
    const [name, version] = browser.split(' ');
    return name !== 'chrome' || Number(version) < 155;
  })
) {
  throw new Error(
    'Browser targets must resolve to a nonempty list of Chrome versions >=155. Check .browserslistrc and the installed browser data.',
  );
}

console.log(`Browser targets: ${browsers.join(', ')}`);

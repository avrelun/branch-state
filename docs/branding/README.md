# Branchstate identity

The mark represents branching histories with square nodes and two contrasting paths. These are product-owned assets; no external branding service or repository is required to render the project README.

- `mark.svg`: editable vector original, 512 × 512 view box.
- `icon.png`: 1024 × 1024 export for project icons.
- `social-preview.svg`: editable 1280 × 640 composition.
- `social-preview.png`: 1280 × 640 GitHub social preview upload.

Palette: charcoal `#282828`, cream `#ebdbb2`, olive `#b8bb26`, mustard `#d79921`, muted cream `#bdae93`. SVGs contain geometry and, in the preview, editable text using the renderer's sans-serif font. They contain no embedded raster images, scripts, external fonts or external image references.

Source: project-specific geometric artwork prepared with the maintainer; the product mark was already used for its Jira space. No stock assets or external logos were imported. Files are covered by the repository MIT license; no claim of trademark clearance is made.

PNG exports were produced with `rsvg-convert`. To regenerate from the repository root:

```sh
rsvg-convert -w 1024 -h 1024 -o docs/branding/icon.png docs/branding/mark.svg
rsvg-convert -w 1280 -h 640 -o docs/branding/social-preview.png docs/branding/social-preview.svg
```

In GitHub repository Settings > General > Social preview, upload `social-preview.png`. Committing the image does not set this field automatically.

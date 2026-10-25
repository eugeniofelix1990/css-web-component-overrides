<div align="center">

# Web Component Contraction

**A small CSS pattern for re-labelling a third-party button and making its host shrink to the new content, without the "phantom width" left behind by the original text.**

[![CI/CD Pipeline](https://github.com/eugeniofelix1990/advanced-css-web-component-overrides/actions/workflows/tests.yml/badge.svg)](https://github.com/eugeniofelix1990/advanced-css-web-component-overrides/actions/workflows/tests.yml)
[![Live demo](https://img.shields.io/badge/live%20demo-GitHub%20Pages-blue)](https://eugeniofelix1990.github.io/css-web-component-overrides/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**[Live demo](https://eugeniofelix1990.github.io/css-web-component-overrides/)**

![Demo: naive attempt vs. contracted result](docs/images/demo.png)

</div>

Includes a live demo and automated layout and accessibility checks. Open [`demo/index.html`](demo/index.html) to see both versions side by side: a naive attempt and the contracted result.

## Contents

- [The problem](#the-problem)
- [Quick start](#quick-start)
- [The pattern](#the-pattern)
- [Configuration](#configuration)
- [Accessibility](#accessibility)
- [Tests](#tests)
- [CI/CD](#cicd)
- [Design notes](#design-notes)
- [Debugging](#debugging)
- [Browser support](#browser-support)
- [Limitations](#limitations)
- [Project structure](#project-structure)
- [License](#license)

## The problem

You can't edit the markup of a component you don't own, so you hide its label with CSS and inject your own. The pill, however, keeps the width of the *original* content, and `width: fit-content` just hugs the invisible text.

```css
/* Naive: looks right, but the original text still occupies space */
.label        { color: transparent; font-size: 0; }
.label::after { content: "New label"; color: #fff; font-size: 14px; }
x-action-button { width: fit-content; }
```

This leaves an unwanted **"phantom width"** layout artifact.

## Quick start

1. Clone the repository or copy [`src/contract-web-component.css`](src/contract-web-component.css) into your project.
2. Replace `x-action-button` with your target component's tag name.
3. Adjust the inner class selectors (`.mdc-button`, `.mdc-button__label`) to match the third-party markup.
4. Link the stylesheet:

```html
<link rel="stylesheet" href="path/to/contract-web-component.css">
```

## The pattern

The solution relies on six core CSS steps:

| # | Step | What it does |
|---|------|--------------|
| 1 | **Design tokens** | Custom properties for label, color, padding, gap and SVG mask. |
| 2 | **Host sizing** | `width: max-content !important` and `flex: 0 0 auto !important` eliminate phantom width and allow precise shrinking. |
| 3 | **Inner button reset** | Clears minimum-width constraints and applies symmetric padding. |
| 4 | **Label setup** | Establishes a flex container with a zero font-size fallback for text nodes. |
| 5 | **Native element layout removal** | Hides native child nodes completely with `display: none !important`. |
| 6 | **Pseudo-element injection** | Renders the SVG icon via mask (`::before`) and the custom text via `content` (`::after`). |

## Configuration

Customize the tokens in `:root`:

```css
:root {
  --wc-label: "Your Label";
  --wc-fg: #ffffff;
  --wc-pad-x: 14px;
  --wc-gap: 6px;
  --wc-icon: url("data:image/svg+xml,...");
}
```

| Token | Purpose |
|-------|---------|
| `--wc-label` | Replacement label text |
| `--wc-fg` | Foreground (text and icon) color |
| `--wc-pad-x` | Horizontal padding |
| `--wc-gap` | Gap between icon and label |
| `--wc-icon` | SVG icon used as a mask |

## Accessibility

- Uses CSS masks (`-webkit-mask` / `mask`) that respect layout flow and high-contrast modes.
- Preserves semantic roles while visually overriding presentation.
- Verified via automated E2E tests for layout and contrast standards.

## Tests

Automated end-to-end and accessibility tests are located in [`tests/`](tests/).

```bash
pytest
```

You can also run the Playwright test suites directly to validate layout boundaries and visual states.

## CI/CD

The GitHub Actions workflow ([`.github/workflows/tests.yml`](.github/workflows/tests.yml)) automatically executes the test suites and deploys the live demo to GitHub Pages on every push to `main`.

## Design notes

- **`max-content` vs. `fit-content`:** `max-content` prevents clamping to the available container space prematurely, ensuring proper shrink-wrapping.
- **Isolation:** keeps structural overrides cleanly decoupled from application logic.

## Debugging

If the host does not shrink:

- Verify that native children (`.mdc-button__label > *`) have `display: none !important` applied.
- Ensure the host selectors match the exact web component tag name.

## Browser support

Modern browsers supporting CSS Custom Properties, Flexbox and CSS Masks (Chrome, Firefox, Safari, Edge).

## Limitations

> [!WARNING]
> This pattern relies on internal class selectors (`.mdc-button`) of the target third-party component. Library updates may require selector adjustments.

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── tests.yml
├── demo/
│   └── index.html
├── docs/
│   └── images/
│       └── demo.png
├── src/
│   └── contract-web-component.css
├── tests/
├── .gitignore
├── LICENSE
├── README.md
└── requirements-dev.txt
```

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

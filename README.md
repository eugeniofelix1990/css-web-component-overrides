[![CI/CD Pipeline](https://github.com/eugeniofelix1990/advanced-css-web-component-overrides/actions/workflows/tests.yml/badge.svg)](https://github.com/eugeniofelix1990/advanced-css-web-component-overrides/actions/workflows/tests.yml)[![Live demo](https://img.shields.io/badge/live%20demo-GitHub%20Pages-blue)](https://eugeniofelix1990.github.io/css-web-component-overrides/)

**Live demo:** https://eugeniofelix1990.github.io/css-web-component-overrides/

# Web Component Contraction

A small CSS pattern for **re-labelling a third-party button and making its host shrink to the new content**, without the "phantom width" left behind by the original text. Includes a live demo and automated layout and accessibility checks.

![demo](docs/images/demo.png)

Open [`demo/index.html`](demo/index.html) to see both versions side by side: a naive attempt and the contracted result.

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

You can't edit the markup of a component you don't own, so you hide its label with CSS and inject your own. The pill, however, keeps the width of the *original* content, and `width: fit-content` just hugs invisible text.

```css
/* Naive: looks right, but the original text still occupies space */
.label        { color: transparent; font-size: 0; }
.label::after { content: "New label"; color: #fff; font-size: 14px; }
host          { width: fit-content; }

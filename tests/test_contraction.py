"""Layout regression tests for the contraction pattern.

Setup:
    pip install pytest-playwright
    playwright install chromium
Run:
    pytest
"""
from pathlib import Path

from playwright.sync_api import Locator, Page, expect

DEMO = Path(__file__).resolve().parents[1] / "demo" / "index.html"
VENDOR_MIN_WIDTH = 240  # min-width the mock vendor styles give the host


def width(locator: Locator) -> float:
    box = locator.bounding_box()
    assert box is not None, "element has no layout box"
    return box["width"]


def test_host_hugs_its_content(page: Page):
    page.goto(DEMO.as_uri())

    host = page.locator("x-action-button")
    button = host.locator(".mdc-button")
    naive_button = page.locator("x-action-button-naive .mdc-button")
    expect(host).to_be_visible()

    # 1. The host wraps the visible pill, with no extra space around it.
    assert abs(width(host) - width(button)) <= 1

    # 2. The vendor's min-width no longer applies.
    assert width(host) < VENDOR_MIN_WIDTH

    # 3. Clearly narrower than the naive version, which keeps the width of
    #    the hidden original text.
    assert width(button) < width(naive_button) * 0.6


def test_button_keeps_an_accessible_name(page: Page):
    page.goto(DEMO.as_uri())

    # Resolved by the browser's accessibility tree, so it also sees
    # generated (::after) content, unlike innerText.
    # Restricted to the contracted host component to avoid strict mode violations with the naive demo element.
    contracted_button = page.locator("x-action-button").get_by_role("button", name="Custom label", exact=True)
    expect(contracted_button).to_be_visible()

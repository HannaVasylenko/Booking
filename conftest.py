import pytest
from playwright.async_api import async_playwright


@pytest.fixture(scope="function")
async def setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1519, "height": 711})
        await page.goto("https://www.booking.com/")
        await page.get_by_label("Dismiss sign-in info.").click()
        yield page
        await browser.close()

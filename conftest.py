import pytest
from playwright.async_api import async_playwright, expect


@pytest.mark.browser_context_args(timezone_id="America/New_York", locale="en-US")
@pytest.fixture(scope="function")
async def setup():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1519, "height": 711})
        await page.goto("https://www.booking.com/")
        try:
            await page.get_by_label("Dismiss sign-in info.").click()
        except TimeoutError:
            pass
        yield page
        await browser.close()

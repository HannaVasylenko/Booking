import pytest
from playwright.async_api import Page, expect
from models.main_page import MainPage


@pytest.mark.asyncio
async def test_select_countries_link(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.select_link()
    await expect(setup.locator(".header_link")).to_have_text("Most Popular Countries/Regions")
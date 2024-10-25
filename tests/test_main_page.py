import pytest
from playwright.async_api import Page, expect
from models.main_page import MainPage


@pytest.mark.asyncio
async def test_select_countries_link(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.select_countries_link()
    await expect(setup.locator(".header_link")).to_have_text("Most Popular Countries/Regions")


@pytest.mark.asyncio
async def test_open_sign_in_page(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.click_on_sign_in()
    await expect(setup.locator(".page-header>h1")).to_have_text("Sign in or create an account")


@pytest.mark.asyncio
async def test_select_tab_link(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.select_tab(main_page.flights_tab)
    await expect(setup.locator(".Frame-module__margin-top_6___qBVzW h1")).to_have_text("Compare and book flights with ease")

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
    await main_page.select_tab("flights")
    await expect(setup.locator("#basiclayout h1")).to_have_text("Compare and book flights with ease")


@pytest.mark.asyncio
async def test_select_localization(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.select_currency("U.S. Dollar")
    await main_page.select_language("English (UK)")
    await expect(setup.locator("[aria-controls='header_currency_picker'] span")).to_have_text("USD")
    await expect(setup.locator("[aria-controls='header_language_picker']")).to_have_attribute("aria-label", "Language: English (UK)")


@pytest.mark.asyncio
async def test_add_list_popular_places_after_click_on(setup: Page) -> None:
    main_page = MainPage(setup)
    default_list_of_places = await main_page.count_list_popular_places()
    await main_page.click_slinks_show_more_btn()
    list_of_places_after__click_on_show_more_btn = await main_page.count_list_popular_places()
    assert list_of_places_after__click_on_show_more_btn == default_list_of_places + 25, "The user did not click on the Show more button"


@pytest.mark.asyncio
async def test_show_language_tooltip(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.show_language_tooltip()
    await expect(setup.locator("[aria-controls='header_language_picker']")).to_have_attribute("aria-describedby", ":r6:")
    await expect(setup.locator("//div[@id=':r6:']/div")).to_be_visible()


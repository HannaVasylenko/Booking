import pytest
from playwright.async_api import Page, expect
from models.main_page import MainPage
from models.search_result_page import SearchResultPage


@pytest.mark.asyncio
async def test_select_stays(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.input_place("poland")
    await main_page.select_nth_place_from_examples(0)
    await main_page.select_check_in_date()
    await main_page.select_check_out_date()
    await main_page.input_values_in_occupancy_popup()
    await main_page.submit_stays_search()
    await expect(setup.locator("input[name='Pet friendly']")).to_be_visible()
    await expect(setup.get_by_label("Search results updated.")).to_contain_text("Poland")


@pytest.mark.asyncio
async def test_filters(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.input_place("poland")
    await main_page.select_nth_place_from_examples(0)
    await main_page.select_check_in_date()
    await main_page.select_check_out_date()
    await main_page.submit_stays_search()
    search_result_page = SearchResultPage(setup)
    await search_result_page.select_checkbox()

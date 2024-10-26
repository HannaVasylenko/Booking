from operator import contains

import mouse
import pytest
from playwright.async_api import Page, expect
from models.main_page import MainPage
from models.search_result_page import SearchResultPage


@pytest.mark.asyncio
async def test_select_stays_list_by_check_in_out_date(setup: Page) -> None:
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
    await search_result_page.select_checkbox_property_type()
    await expect(setup.locator("//input[@name='Hotels']/..")).to_be_visible()
    await search_result_page.select_checkbox_property_rating("5 stars")
    await expect(setup.locator("//input[@name='5 stars']/..")).to_be_visible()


@pytest.mark.asyncio
async def test_layout_website(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.input_place("poland")
    await main_page.select_nth_place_from_examples(0)
    await main_page.select_check_in_date()
    await main_page.select_check_out_date()
    await main_page.submit_stays_search()
    search_result_page = SearchResultPage(setup)

    await search_result_page.select_grid_layout_website()
    if await search_result_page.grid_layout.is_visible():
        await expect(setup.locator("//span[text()='Grid']/..")).to_have_attribute("class", "a83ed08757 c21c56c305 bf0537ecb5 ab98298258 d8974fd49d bdad918c5d c3b4df07f9")
    elif await search_result_page.grid_layout2.is_visible():
        await expect(setup.locator("//label[text()='Grid']/..")).to_have_attribute("style", "--bui-segmented-control-active-scale-x: 49.7125px; --bui-segmented-control-active-transform-x: 51px;")
    elif await search_result_page.grid_layout3.is_visible():
        await expect(search_result_page.grid_layout3).to_have_attribute("class", "a83ed08757 c21c56c305 bf0537ecb5 d691166b09 ab98298258 d8974fd49d bdad918c5d c3b4df07f9")

    await search_result_page.select_list_layout_website()
    if await search_result_page.list_layout.is_visible():
        await expect(setup.locator("//span[text()='List']/..")).to_have_attribute("class", "a83ed08757 c21c56c305 bf0537ecb5 ab98298258 d8974fd49d bdad918c5d c3b4df07f9")
    elif await search_result_page.list_layout2.is_visible():
        await expect(setup.locator("//label[text()='List']/..")).to_have_attribute("class", "--bui-segmented-control-active-scale-x: 44.275px; --bui-segmented-control-active-transform-x: 3px;")
    elif await search_result_page.list_layout3.is_visible():
        await expect(search_result_page.list_layout3).to_have_attribute("class", "a83ed08757 c21c56c305 bf0537ecb5 d691166b09 ab98298258 d8974fd49d bdad918c5d c3b4df07f9")


@pytest.mark.asyncio
async def test_sticky_container_inner_appears(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.input_place("poland")
    await main_page.select_nth_place_from_examples(0)
    await main_page.select_check_in_date()
    await main_page.select_check_out_date()
    await main_page.submit_stays_search()
    search_result_page = SearchResultPage(setup)
    await search_result_page.hover_load_more_results_btn()
    await expect(setup.locator("[data-testid='sticky-container-inner']")).to_be_visible()


@pytest.mark.asyncio
async def test_select_stays_from_search_result_list(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.input_place("poland")
    await main_page.select_nth_place_from_examples(0)
    await main_page.select_check_in_date()
    await main_page.select_check_out_date()
    await main_page.submit_stays_search()
    search_result_page = SearchResultPage(setup)
    async with setup.expect_popup() as new_page_info:
        await search_result_page.select_title_stays("Hotel Szafir")
    new_page = await new_page_info.value
    await expect(new_page.locator("#hp_hotel_name h2")).to_have_text("Hotel Szafir")

# TODO complete test_filters test
# TODO edit expect 2 layout in test

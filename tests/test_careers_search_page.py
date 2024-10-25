import pytest
from playwright.async_api import Page, expect
from models.careers_search_result_page import CareersSearchPage
from models.main_page import MainPage


@pytest.mark.asyncio
async def test_select_careers(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.select_careers_link()
    careers_search_result_page = CareersSearchPage(setup)
    await careers_search_result_page.select_vacancy("manager", "Engineering Manager")
    async with setup.expect_popup() as new_page_info:
        await careers_search_result_page.submit_careers()
    new_page = await new_page_info.value
    list_vacancies_in_search = new_page.locator("a.job-title-link span") # mat-expansion-panel-header a.job-title-link span
    count = await list_vacancies_in_search.count()
    match_found = False
    for i in range(count):
        vacancy_text = await list_vacancies_in_search.nth(i).text_content()
        if "Engineering" in vacancy_text or "Manager" in vacancy_text:
            match_found = True
    assert match_found, "No vacancy contains 'Engineering' or 'Manager'."

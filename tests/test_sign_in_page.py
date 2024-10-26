import pytest
from playwright.async_api import Page, expect
from models.main_page import MainPage
from models.sign_in_page import SignInPage


@pytest.mark.asyncio
async def test_input_email_in_sign_in_page(setup: Page) -> None:
    main_page = MainPage(setup)
    await main_page.click_on_sign_in()
    sign_in_page = SignInPage(setup)
    await sign_in_page.type_in_email_field()
    await sign_in_page.click_on_continue_with_email_btn()
    await expect(setup.locator("#username-note")).to_have_text("Make sure the email address you entered is correct.")
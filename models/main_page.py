class MainPage:
    def __init__(self, page):
        self.page = page
        self.countries_link = page.get_by_role("link", name="Countries")
        self.sign_in_link = page.get_by_test_id("header-sign-in-button")
        self.header_countries_page = page.locator(".header_link")

    async def select_link(self):
        await self.countries_link.click()

    async def click_on_sign_in(self):
        await self.sign_in_link.click()
class MainPage:
    def __init__(self, page):
        self.page = page
        self.countries_link = page.get_by_role("link", name="Countries")
        self.header_countries_page = page.locator(".header_link")

    async def select_link(self):
        await self.countries_link.click()
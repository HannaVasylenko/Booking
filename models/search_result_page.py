class SearchResultPage:
    def __init__(self, page):
        self.page = page
        self.checkbox_property_type = page.locator("[id=\"filter_group_class_\\:r4f\\:\"]").get_by_text("5 stars")
        self.expand_city_btn = page.locator("[id=\"filter_group_uf_\\:r2e\\:\"]").get_by_test_id("filters-group-expand-collapse")
        self.checkbox_city = page.locator("[id=\"filter_group_uf_\\:r2e\\:\"]").get_by_text("Krakow")
        self.checkbox_stars = page.locator("[id=\"filter_group_class_\\:r4f\\:\"]").get_by_text("5 stars")
        self.list_layout = page.locator("//button//span[text()='List']")
        self.grid_layout = page.locator("//button//span[text()='Grid']")
        self.list_layout2 = page.locator("//label[text()='List']")
        self.grid_layout2 = page.locator("//label[text()='Grid']")
        self.list_layout3 = page.locator("//button[@aria-label='List']")
        self.grid_layout3 = page.locator("//button[@aria-label='Grid']")

    async def select_checkbox(self):
        await self.checkbox_property_type.click()

    async def select_grid_layout_website(self):
        if await self.grid_layout.is_visible():
            await self.grid_layout.click()
        elif await self.grid_layout2.is_visible():
            await self.grid_layout2.click()
        elif await self.grid_layout3.is_visible():
            await self.grid_layout3.click()

    async def select_list_layout_website(self):
        if await self.list_layout.is_visible():
            await self.list_layout.click()
        elif await self.list_layout2.is_visible():
            await self.list_layout2.click()
        elif await self.list_layout3.is_visible():
            await self.list_layout3.click()

    async def get_attribute(self, attribute: str):
        await self.page.locator(f"//button//span[text()='List']/parent::*").get_attribute({attribute})

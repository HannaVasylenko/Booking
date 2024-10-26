class SearchResultPage:
    def __init__(self, page):
        self.page = page

        self.checkbox_property_type_1 = page.locator("//legend[text()='Property Type']/ancestor::div[@id='filter_group_ht_id_:r1r:']//div[text()='Hotels']")
        self.checkbox_property_type_2 = page.locator("//legend[text()='Property Type']/ancestor::div[@id='filter_group_ht_id_:r2k:']//div[text()='Hotels']")
        self.checkbox_property_type_3 = page.locator("//div[@aria-label='Filters']//label[@for=':r2b:']//div[text()='Hotels']/..")

        self.checkbox_property_rating_1 = page.locator("")
        self.checkbox_property_rating_2 = page.locator("")
        self.checkbox_property_rating_3 = page.locator("")

        self.expand_city_btn = page.locator("[id=\"filter_group_uf_\\:r2e\\:\"]").get_by_test_id("filters-group-expand-collapse")
        self.checkbox_city = page.locator("[id=\"filter_group_uf_\\:r2e\\:\"]").get_by_text("Krakow")
        self.checkbox_stars = page.locator("[id=\"filter_group_class_\\:r4f\\:\"]").get_by_text("5 stars")
        self.list_layout = page.locator("//button//span[text()='List']")
        self.grid_layout = page.locator("//button//span[text()='Grid']")
        self.list_layout2 = page.locator("//label[text()='List']")
        self.grid_layout2 = page.locator("//label[text()='Grid']")
        self.list_layout3 = page.locator("//button[@aria-label='List']")
        self.grid_layout3 = page.locator("//button[@aria-label='Grid']")
        self.sticky_container_inner = page.locator("[data-testid='sticky-container-inner']")
        self.load_more_results_btn = page.locator("//span[text()='Load more results']")

    async def select_checkbox_property_type(self):
        if await self.checkbox_property_type_1.is_visible():
            await self.checkbox_property_type_1.click()
        elif await self.checkbox_property_type_2.is_visible():
            await self.checkbox_property_type_2.click()
        elif await self.checkbox_property_type_3.is_visible():
            await self.checkbox_property_type_3.click()

    async def select_checkbox_property_rating(self, rating_value):
        if await self.page.locator(f"//legend[text()='Property rating']/ancestor::div[@id='filter_group_class_:r2i:']//div[text()='{rating_value}']").is_visible():
            await self.page.locator(f"//legend[text()='Property rating']/ancestor::div[@id='filter_group_class_:r2i:']//div[text()='{rating_value}']").click()
        if await self.page.locator(f"//div[@aria-label='Filters']//label[@for=':r36:']//div[text()='{rating_value}']/..").is_visible():
            await self.page.locator(f"//div[@aria-label='Filters']//label[@for=':r36:']//div[text()='{rating_value}']/..").click()
        if await self.page.locator(f"//div[@aria-label='Filters']//label[@for=':r38:']//div[text()='{rating_value}']/..").is_visible():
            await self.page.locator(f"//div[@aria-label='Filters']//label[@for=':r38:']//div[text()='{rating_value}']/..").click()

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

    async def hover_load_more_results_btn(self):
        await self.page.wait_for_load_state("networkidle")
        await self.page.evaluate("window.scrollBy(0,2 * document.body.scrollHeight / 3)")

    async def select_title_stays(self, stays_name):
        await self.page.locator(f"//div[@data-testid='property-card']//h3//div[text()='{stays_name}']").click()

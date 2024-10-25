class SearchResultPage:
    def __init__(self, page):
        self.page = page
        self.checkbox_property_type = page.locator("[id=\"filter_group_ht_id_\\:r26\\:\"] label").filter(has_text="Hotels").locator("svg")
        self.checkbox = page.locator("div[id='filter_group_ht_id_:r2n:']")


    async def select_checkbox(self):
        await self.checkbox_property_type.click()


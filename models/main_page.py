from datetime import datetime, date, timedelta

class MainPage:
    def __init__(self, page):
        self.page = page
        self.countries_link = page.get_by_role("link", name="Countries")
        self.sign_in_link = page.get_by_test_id("header-sign-in-button")
        self.header_countries_page = page.locator(".header_link")
        self.stays_tab = page.locator("#accommodations")
        self.flights_tab = page.locator("#flights")
        self.car_rentals_tab = page.locator("#cars")
        self.attractions_tab = page.locator("#attractions")
        self.airport_taxis_tab = page.locator("#airport_taxis")
        self.careers_link = page.get_by_role("link", name="Careers")
        self.place_name = page.get_by_placeholder("Where are you going?")
        self.list_places_examples = page.locator("ul[role='group'] li")
        current_date = datetime.now()
        formatted_date = current_date.strftime("%d %B")
        self.check_in_date = page.get_by_label(formatted_date)
        check_out_date = current_date + timedelta(days=3)
        formatted_check_out_date = check_out_date.strftime("%d %B")
        self.check_out_date = page.get_by_label(formatted_check_out_date)
        self.search_btn = page.get_by_role("button", name="Search")
        self.occupancy_popup_expand_btn = page.get_by_test_id("occupancy-config")
        self.adults_add_btn = page.locator("input#group_adults ~ div>button~button")
        self.children_add_btn = page.locator("input#group_children ~ div>button~button")
        self.children_age_arrow_btn = page.locator("select[name='age']")
        self.currency_picker = page.get_by_test_id("header-currency-picker-trigger")
        self.language_picker = page.locator("[data-testid='header-language-picker-trigger']")
        self.slinks_show_more_btn = page.locator("//div[@class='slinks']//span[text()='Show more']")
        self.list_popular_places = page.locator("//div[@id='mainIndexInterlinkingTab-1']//div[@class='b817090550 b232a3502b']")
        self.language_tooltip_text = page.locator("//div[@id=':r6:']/div")

    async def select_countries_link(self):
        await self.countries_link.click()

    async def click_on_sign_in(self):
        await self.sign_in_link.click()

    async def select_careers_link(self):
        await self.careers_link.click()

    async def select_tab(self, tab_name: str):
        await self.page.locator(f"#{tab_name}").click()

    async def input_place(self, place: str):
        await self.place_name.click()
        await self.place_name.fill(place)

    async def select_nth_place_from_examples(self, n: int):
        await self.list_places_examples.nth(n).click()

    async def select_check_in_date(self):
        await self.check_in_date.click()

    async def select_check_out_date(self):
        await self.check_out_date.click()

    async def submit_stays_search(self):
        await self.search_btn.click()

    async def input_values_in_occupancy_popup(self):
        await self.occupancy_popup_expand_btn.click()
        await self.adults_add_btn.click()
        await self.children_add_btn.click()
        await self.page.get_by_test_id("kids-ages-select").get_by_role("combobox").select_option("9")
        await self.page.locator("label").filter(has_text="Traveling with pets?").locator("span").first.click()
        await self.page.get_by_role("button", name="Done").click()

    async def select_currency(self, currency: str):
        await self.currency_picker.click()
        await self.page.locator(f"//div[@id='header_currency_picker']//div[@data-testid='Suggested for you']//span[text()='{currency}']").click()

    async def select_language(self, language: str):
        await self.language_picker.click()
        await self.language_picker.click()
        await self.page.locator(f"//div[@data-testid='All languages']//span[text()='{language}']").click()

    async def click_slinks_show_more_btn(self):
        await self.slinks_show_more_btn.click()

    async def count_list_popular_places(self)-> int:
        return await self.list_popular_places.count()

    async def show_language_tooltip(self):
        await self.language_picker.hover()

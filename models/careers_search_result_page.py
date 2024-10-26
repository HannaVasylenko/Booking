class CareersSearchPage:
    def __init__(self, page):
        self.page = page
        self.careers_field = page.get_by_placeholder("Search for jobs by title or keyword")
        self.search_btn = page.get_by_role("button", name="Search")
        self.list_vacancies_in_search = page.locator("a.job-title-link span") # p.job-title span
        self.vacancy_title = page.locator(".header-section h1")

    async def select_vacancy(self, keyword: str, vacancy_name: str):
        await self.careers_field.fill(keyword)
        await self.page.get_by_role("option", name=vacancy_name, exact=True).click()

    async def submit_careers(self):
        await self.search_btn.click()

    async def select_nth_vacancy(self, n: int):
        await self.page.locator(f"a#link-job-{n} span").click()



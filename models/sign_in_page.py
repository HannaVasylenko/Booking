class SignInPage:
    def __init__(self, page):
        self.page = page
        self.email_field = page.get_by_placeholder("Enter your email address")
        self.continue_with_email_btn = page.get_by_role("button", name="Continue with email")

    async def type_in_email_field(self):
        await self.email_field.type("email")

    async def click_on_continue_with_email_btn(self):
        await self.continue_with_email_btn.click()
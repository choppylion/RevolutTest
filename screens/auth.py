from screens.base import ScreenWithPrevNext


class Authorization(ScreenWithPrevNext):

    common_digit_locator = "com.revolut.revolut.test:id/digit{}"
    forgot_locator = "com.revolut.revolut.test:id/button_forgot_text"
    delete_locator = "com.revolut.revolut.test:id/icon_delete"

    def proceed(self, password):
        for char in password:
            self.enter_digit(char)

    def enter_digit(self, char):
        digit = int(char)
        self.click(self.common_digit_locator.format(digit))

    def clear(self):
        self.click(self.delete_locator)

    def forgot(self):
        self.click(self.forgot_locator)


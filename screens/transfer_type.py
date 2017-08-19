from screens.base import BaseScreen


class TransferType(BaseScreen):

    titles = {
        "self": "To myself",
        "other": "To another person",
        "business": "To a business"
    }

    item_locator = "//android.widget.TextView[@text='{}']"

    back_locator = "com.revolut.revolut.test:id/back_button"
    next_locator = "com.revolut.revolut.test:id/button_next"

    def select(self, option):
        button = self.get_element_by_type(self.item_locator.format(
            self.titles[option]), "xpath")
        button.click()

    def accept(self):
        self.click(self.next_locator)

    def close(self):
        self.click(self.back_locator)

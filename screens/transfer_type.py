from screens.base import ScreenWithPrevNext


class TransferType(ScreenWithPrevNext):

    titles = {
        "self": "To myself",
        "other": "To another person",
        "business": "To a business"
    }

    item_locator = "//android.widget.TextView[@text='{}']"

    def select(self, option):
        button = self.get_element_by_type(self.item_locator.format(
            self.titles[option]), "xpath")
        button.click()

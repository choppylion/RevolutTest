from screens.base import BaseScreen


class Home(BaseScreen):

    transfer_locator = "com.revolut.revolut.test:id/button_transfer"

    transfer_item_locator = "//android.widget.TextView[@text='{}']"

    titles = {
        "send": "Send money",
        "request": "Request money",
        "split": "Split bill",
        "bank": "To bank account"
    }

    def transfer(self, destination):
        self.click(self.transfer_locator)

        button = self.get_element_by_type(self.transfer_item_locator.format(
            self.titles[destination]), "xpath")
        button.click()

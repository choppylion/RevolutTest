from screens.base import BaseScreen


class BankTransfer(BaseScreen):

    close_locator = "com.revolut.revolut.test:id/toolbar/"
    add_new_locator = "com.revolut.revolut.test:id/list_add_new_item_text"

    def add_new(self):
        self.click(self.add_new_locator)

    def close(self):
        self.click(self.close_locator)

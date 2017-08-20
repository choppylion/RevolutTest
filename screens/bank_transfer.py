from screens.base import BaseScreen


class BankTransfer(BaseScreen):

    close_locator = "com.revolut.revolut.test:id/toolbar/"
    add_new_locator = "com.revolut.revolut.test:id/list_add_new_item_text"


    item_name_currency_locator = "com.revolut.revolut.test:id/item_title" #{first_name} {last_name} ∙ {currency}
    item_iban_locator = "com.revolut.revolut.test:id/item_subtitle1"

    def add_new(self):
        self.click(self.add_new_locator)

    def close(self):
        self.click(self.close_locator)

    def is_beneficiary_present(self, first_name, last_name, currency, iban):
        self.is_present(
            "android.widget.TextView[@text='{first_name} {last_name} ∙ {currency']/../"
            "//android.widget.TextView[@text='{iban}']".format(first_name=first_name,
                                                               last_name=last_name,
                                                               currency=currency,
                                                               iban=iban)
        )

from screens.base import BaseScreen, ScreenWithPrevNext


class CountryCurrency(ScreenWithPrevNext):

    edit_country_locator = "com.revolut.revolut.test:id/edit_country"
    edit_currency_locator = "com.revolut.revolut.test:id/edit_currency"

    def select_country(self, country):
        self.click(self.edit_country_locator)
        SelectCountry(self.driver).select(country)

    def select_currency(self, currency):
        self.click(self.edit_currency_locator)
        SelectCurrency(self.driver).select(currency)

    @property
    def selected_country(self):
        return self.get_element(self.edit_country_locator).text()

    @property
    def selected_currency(self):
        return self.get_element(self.edit_currency_locator).text()


class SelectObject(BaseScreen):

    field_locator = "com.revolut.revolut.test:id/search_src_text"
    clear_field_locator = "com.revolut.revolut.test:id/search_close_btn"
    back_locator = "com.revolut.revolut.test:id/back_button"

    def select(self, item):
        self.send_keys(self.field_locator, item)
        item = self.get_element("//android.widget.TextView[@text='{}']".format(item))
        item.click()


class SelectCurrency(SelectObject):

    item_locator = "com.revolut.revolut.test:id/text_view_currency_description"


class SelectCountry(SelectObject):

    item_locator = "com.revolut.revolut.test:id/country_item"

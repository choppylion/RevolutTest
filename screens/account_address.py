from screens.base import ScreenWithPrevNext


class AccountAddress(ScreenWithPrevNext):

    zip_locator = "com.revolut.revolut.test:id/address_postal_code"
    line1_locator = "com.revolut.revolut.test:id/address_line_1"
    line2_locator = "com.revolut.revolut.test:id/address_line_2"
    city_locator = "com.revolut.revolut.test:id/address_city"
    region_locator = "com.revolut.revolut.test:id/address_region"

    def enter_zip(self, zip_code):
        self.send_keys(self.zip_locator, zip_code)

    def enter_line1(self, line1):
        self.send_keys(self.line1_locator, line1)

    def enter_line2(self, line2):
        self.send_keys(self.line2_locator, line2)

    def enter_city(self, city):
        self.send_keys(self.city_locator, city)

    def enter_region(self, region):
        self.send_keys(self.region_locator, region)

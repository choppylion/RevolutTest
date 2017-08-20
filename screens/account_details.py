from screens.base import ScreenWithPrevNext


class AccountDetails(ScreenWithPrevNext):

    first_name_locator = "com.revolut.revolut.test:id/first_name"
    last_name_locator = "com.revolut.revolut.test:id/last_name"
    iban_locator = "com.revolut.revolut.test:id/server_field_0"
    bic_swift_locator = "com.revolut.revolut.test:id/server_field_1"
    phone_locator = "com.revolut.revolut.test:id/mobile_phone"
    email_locator = "com.revolut.revolut.test:id/email"

    def enter_first_name(self, first_name):
        self.send_keys(self.first_name_locator, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.first_name_locator, last_name)

    def enter_iban(self, iban):
        self.send_keys(self.iban_locator, iban)

    def enter_swift(self, swift):
        self.send_keys(self.bic_swift_locator, swift)

    def enter_phone(self, phone=None):
        if phone is not None:
            self.send_keys(self.phone_locator, phone)

    def enter_email(self, email=None):
        if email is not None:
            self.send_keys(self.email_locator, email)

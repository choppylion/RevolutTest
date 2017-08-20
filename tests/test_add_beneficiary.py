import pytest

from screens.auth import Authorization
from screens.home import Home
from screens.bank_transfer import BankTransfer
from screens.transfer_type import TransferType
from screens.country_currency import CountryCurrency
from screens.account_details import AccountDetails
from screens.account_address import AccountAddress
from screens.confirm_screen import ConfirmScreen


@pytest.mark.usefixtures("driver", "config")
# @pytest.mark.parametrize()
class TestAddBenefeciary:

    def test_main_scenarion(self):
        # authorization
        auth = Authorization(self.driver)
        auth.proceed(self.config["password"])

        # transfer
        home = Home(self.driver)
        home.transfer("bank_account")

        # new beneficiary
        bank_transfer = BankTransfer(self.driver)
        bank_transfer.add_new()

        # tranfer type
        transfer_type = TransferType(self.driver)
        transfer_type.select(self.config["transfer_type"])
        transfer_type.next()

        # country and currency
        country_currency = CountryCurrency(self.driver)
        country_currency.select_country(self.config["country"])
        country_currency.select_currency(self.config["currency"])

        assert country_currency.selected_country is self.config["country"]
        assert country_currency.selected_currency is self.config["currency"]

        country_currency.next()

        # account details
        account_details = AccountDetails(self.driver)
        account_details.enter_first_name(self.config["first_name"])
        account_details.enter_last_name(self.config["last_name"])
        account_details.enter_iban(self.config["iban"])
        account_details.enter_swift(self.config["swift"])
        if self.config["phone"]:
            account_details.enter_phone(self.config["phone"])
        if self.config["email"]:
            account_details.enter_email(self.config["email"])

        account_details.next()

        #  account address
        account_address = AccountAddress(self.driver)
        account_address.enter_zip(self.config["zip"])
        account_address.enter_line1(self.config["line1"])
        account_address.enter_line2(self.config["line2"])
        account_address.enter_city(self.config["city"])
        account_address.enter_region(self.config["region"])

        # confirmation
        confirm_screen = ConfirmScreen(self.driver)

        assert confirm_screen.selected_name == (self.config["first_name"], self.config["last_name"])

        confirm_screen.next()

        # checking is beneficiary added
        assert bank_transfer.is_beneficiary_present(self.config["first_name"], self.config["last_name"],
                                                    self.config["currency"], self.config["iban"])

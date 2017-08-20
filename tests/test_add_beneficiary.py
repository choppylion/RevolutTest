import pytest

from conftest import import_test_data

from screens.auth import Authorization
from screens.home import Home
from screens.bank_transfer import BankTransfer
from screens.transfer_type import TransferType
from screens.country_currency import CountryCurrency
from screens.account_details import AccountDetails
from screens.account_address import AccountAddress
from screens.confirm_screen import ConfirmScreen


@pytest.mark.usefixtures("driver")
class TestAddBenefeciary:

    @pytest.mark.parametrize("config", import_test_data("main_scenario_person.csv"))
    def test_main_scenario_person(self, config):
        self.main_scenario(config)

    @pytest.mark.parametrize("config", import_test_data("main_scenario_business.csv"))
    def test_main_scenario_business(self, config):
        self.main_scenario(config)

    def main_scenario(self, config):
        auth_screen = self.auth()
        home_screen = self.home()
        bank_transfer_screen = self.bank_transfer()
        transfer_type_screen = self.transfer_type()
        transfer_type_screen.next()

        country_currency_screen = self.country_currency()
        assert country_currency_screen.selected_country == self.config["country"]
        assert country_currency_screen.selected_currency == self.config["currency"]
        country_currency_screen.next()

        account_details_screen = self.account_details()
        account_details_screen.next()
        account_address_screen = self.account_address()

        # confirmation
        confirm_screen = ConfirmScreen(self.driver)
        assert confirm_screen.selected_name == (self.config["first_name"], self.config["last_name"])
        confirm_screen.next()

        assert bank_transfer_screen.is_beneficiary_present(self.config["first_name"], self.config["last_name"],
                                                    self.config["currency"], self.config["iban"])

    def test_main_scenario_business(self):
        pass

    def auth(self):
        # authorization
        auth = Authorization(self.driver)
        auth.proceed(self.config["password"])
        return auth

    def home(self):
        # transfer
        home = Home(self.driver)
        home.transfer("bank_account")
        return home

    def bank_transfer(self):
        # new beneficiary
        bank_transfer = BankTransfer(self.driver)
        bank_transfer.add_new()
        return bank_transfer

    def transfer_type(self):
        # tranfer type
        transfer_type = TransferType(self.driver)
        transfer_type.select(self.config["transfer_type"])
        transfer_type.next()
        return transfer_type

    def country_currency(self):
        # country and currency
        country_currency = CountryCurrency(self.driver)
        country_currency.select_country(self.config["country"])
        country_currency.select_currency(self.config["currency"])
        return country_currency

    def account_details(self):
        # account details
        account_details = AccountDetails(self.driver)
        account_details.enter_iban(self.config["iban"])
        account_details.enter_swift(self.config["swift"])
        if self.config["phone"]:
            account_details.enter_phone(self.config["phone"])
        if self.config["email"]:
            account_details.enter_email(self.config["email"])

        if self.config["transfer_type"] == "business":
            account_details.enter_first_name(self.config["name"])
        elif self.config["transfer_type"] in ["self", "other"]:
            account_details.enter_first_name(self.config["first_name"])
            account_details.enter_last_name(self.config["last_name"])
        return account_details

    def account_address(self):
        #  account address
        if self.config["transfer_type"] in ["self", "other"]:
            account_address = AccountAddress(self.driver)
            account_address.enter_zip(self.config["zip"])
            account_address.enter_line1(self.config["line1"])
            account_address.enter_line2(self.config["line2"])
            account_address.enter_city(self.config["city"])
            account_address.enter_region(self.config["region"])
            return account_address

import pytest

from screens.auth import Authorization
from screens.home import Home
from screens.bank_transfer import BankTransfer
from screens.transfer_type import TransferType
from screens.country_currency import CountryCurrency
from screens.account_details import AccountDetails
from screens.last_screen import LastScreen


@pytest.mark.usefixtures("driver", "config")
# @pytest.mark.parametrize()
class TestAddBenefeciary:

    def test_auth(self):
        auth = Authorization(self.driver)
        auth.proceed(self.config["password"])
        assert True

    def test_select_transfer(self):
        home = Home(self.driver)
        home.transfer("bank_account")
        assert True

    def test_select_new(self):
        bank_transfer = BankTransfer(self.driver)
        bank_transfer.add_new()
        assert True

    def test_select_transfer_type(self):
        transfer_type = TransferType(self.driver)
        transfer_type.select(self.config["transfer_type"])
        transfer_type.accept()
        assert True

    def test_select_country_currency(self):
        country_currency = CountryCurrency(self.driver)
        country_currency.select(self.config["country"])
        country_currency.select(self.config["currency"])
        country_currency.accept()
        assert True
        assert True

    def test_enter_account_details(self):
        account_details = AccountDetails(self.driver)
        account_details.select(self.config[""])
        account_details.select(self.config[""])
        account_details.select(self.config[""])
        account_details.select(self.config[""])
        account_details.select(self.config[""])
        account_details.accept()
        assert True

    def test_confirm(self):
        last_screen = LastScreen(self.driver)
        last_screen.select(self.config[""])
        last_screen.accept()
        assert True
        assert True
        assert True
        assert True
        assert True
        assert True
        assert True

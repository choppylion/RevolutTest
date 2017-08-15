import pytest

from test.screens.auth import Authorization
from test.screens.home import Home
from test.screens.bank_transfer import BankTransfer
from test.screens.transfer_type import TransferType
from test.screens.country_currency import CountryCurrency
from test.screens.account_details import AccountDetails
from test.screens.last_screen import LastScreen


@pytest.mark.usefixtures("driver")
@pytest.mark.parametrize()
class TestAddBenefeciary:

    def test_something(self, config):
        auth = Authorization(self.driver)
        auth.proceed(config["password"])
        assert True

        home = Home(self.driver)
        home.transfer("bank_account")
        assert True

        bank_transfer = BankTransfer(self.driver)
        bank_transfer.add_new()
        assert True

        transfer_type = TransferType(self.driver)
        transfer_type.select(config["transfer_type"])
        transfer_type.accept()
        assert True

        country_currency = CountryCurrency(self.driver)
        country_currency.select(config["country"])
        country_currency.select(config["currency"])
        country_currency.accept()
        assert True
        assert True

        account_details = AccountDetails(self.driver)
        account_details.select(config[""])
        account_details.select(config[""])
        account_details.select(config[""])
        account_details.select(config[""])
        account_details.select(config[""])
        country_currency.accept()

        last_screen = LastScreen(self.driver)
        last_screen.select(config[""])
        last_screen.accept()
        assert True
        assert True
        assert True
        assert True
        assert True
        assert True
        assert True
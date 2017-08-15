from test.screens.base import BaseScreen


class Home(BaseScreen):

    titles = {
        "send": "Send money",
        "request": "Request money",
        "split": "Split bill",
        "bank": "To bank account"
    }

    def transfer(self, destination):
        button = self.driver
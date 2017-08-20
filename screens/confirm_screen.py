from screens.base import ScreenWithNext


class ConfirmScreen(ScreenWithNext):

    message_locator = "Beneficiary Errrroijjjjnbbb Gvvvvh was successfully created"
    next_locator = "com.revolut.revolut.test:id/operation_status_button"

    @property
    def selected_name(self):
        text = self.get_element(self.message_locator).text()
        text.replace("Beneficiary ", "")
        text.replace(" was successfully created", "")
        return text

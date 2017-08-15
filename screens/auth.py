from test.screens.base import BaseScreen


class Authorization(BaseScreen):

    def proceed(self, password):
        for char in password:
            num_button = self.driver.find_element_by_text(char)
            num_button.click()
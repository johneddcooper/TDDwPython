from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which works

        # She tries again to submit an empty list item

        # She recieves another error message

        # She can correct it by filling some text in
        self.fail('write me')

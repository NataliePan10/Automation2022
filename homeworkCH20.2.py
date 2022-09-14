



from webelements.UIElements import UIElement as Element
from selenium.webdriver.support.select import Select



class Checkbox(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)


    def select_checkbox(self):
        subscribe_checkbox = self.get_element()
        if not subscribe_checkbox_is_selected():
                subscribe_checkbox.click()







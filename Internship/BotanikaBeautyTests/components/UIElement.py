
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import datetime
from selenium.webdriver.support.color import Color


class UIElement:
    """
    This class is for any web element on the page, takes as parameters browser, method of locating element
    and locator itself
    """
    def __init__(self, browser, by, locator):
        self.driver = browser.get_driver()
        self.wait = browser.get_wd_wait()
        self._by = by
        self._locator = locator


    def save_screenshot(self):
        now = datetime.now()

        filename="../screenshots" + now.strftime("%d%m%Y_%H%M%S.png")
        self.driver.save_scfeenshots(filename)

    def get_element(self):
        """
        Locates web element on the page
        :return: WebElement object
        """
        try:
            return self.driver.find_element(self._by, self._locator)
        except NoSuchElementException:
            print("Wasn't able to find element by {} with locator={}".format(self._by, self._locator))
            raise

    def get_locator(self):
        return self._locator

    def wait_until_visible(self):
        """
        Waits until web element is visible
        :return: WebElement object
        """
        try:
            return self.wait.until(EC.visibility_of_element_located((self._by, self._locator)))
        except TimeoutException:
            print("Web element with locator {} by {} is not visible".format(self._locator, self._by))
            raise

    def wait_until_invisible(self):
        return self.wait.until(EC.invisibility_of_element_located(self._by,self._locator))




    def get_text(self, wait=True):
        """
        Gets the text of the web element
        :param wait: put False, if you don't want to wait until element will be visible
        :return: text of the WebElement
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()

        return element.text



    def get_attribute(self, attribute, wait=True):
        """
        Returns the attribute of web element (in html it will  be the attrbiute of the tag)
        :param attribute: name of the attribute to return
        :param wait: put False, if you don't want to wait until element will be visible
        :return: value of the attribute specified
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()
        return element.get_attribute(attribute)



    def click(self, xpath = None):
        """
        Waits until element will be clickable and clicks on it
        """
        #self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element())
        if xpath is None:
            locator = self._locator
        else:
            locator = xpath
        try:
            self.wait.until(EC.element_to_be_clickable((self._by, locator))).click()
        except TimeoutException:
            print("Web element with locator {} by {} is not clickable".format(self._locator, self._by))
            raise

    def enter_text(self, text, wait=False):
        """
        Sends keys to the input field
        :param text: text to type in
        :param wait: put True, if you want to wait until element will be visible
        """
        if wait:
            element = self.wait_until_visible()
        else:
            element = self.get_element()

        element.clear()
        element.send_keys(text)

    def submit(self):
        """
        Clicks on submit button of the form
        """
        try:
            self.wait.until(EC.element_to_be_clickable((self._by, self._locator))).submit()
        except TimeoutException:
            print("Web element with locator {} by {} is not clickable".format(self._locator, self._by))
            self.save_screenshots()
            raise


    def get_background_color(self):
        backround_color = self.get_element().value_of_css_property("background-color")
        return Color.from_string(backround_color)

    def get_font_style(self):
        return self.get_element().value_of_css_property("font-family")

    def scroll_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element())

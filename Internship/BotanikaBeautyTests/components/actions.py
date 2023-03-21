from selenium.webdriver.common.action_chains import ActionChains


class Actions:
    def __init__(self, browser):
        self.action_chains = ActionChains(browser.get_driver())

    def click(self, element = None, reset = True):
        if reset:
              self.action_chains.click(element.get_element()).perform()

        if element:
            self.action_chains.click(element.get_element()).perform()
        else:
            self.action_chains.click().perform()

    def click_and_hold(self,element = None, reset = True):
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.click_and_hold(element.get_element()).perform()
        else:
            self.action_chains.click_and_hold(element.get_element()).perform()

    def right_click(self, element = None, reset = True):
        if reset:
            self.action_chains.reset_actions()

            if element:
                self.action_chains.context_click(element.get_element()).perform()

            else:
                self.action_chains.context_click.perform()

    def double_click(self, element = None, reset = True):
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.double_click(element.get_element()).perform()

        else:
            self.action_chains.double_click().perform()


    def drag_and_drop(self, source, target, reset = True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.drag_and_drop(source.get_element(), target.get_element().perform())

    def drag_and_drop_by_offset(self, source, xoffset=0, yoffset=0, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.drag_and_drop_by_offset(source.get_element(), xoffset,yoffset).perform()

    def key_down(self, key, element = None, reset = True):
        if reset:
            self.action_chains.reset_actions()

        if element:
            self.action_chains.key_down(key, element.get_element()).perform()

        else:
            self.action_chains.key_down(key).perform

    def key_up(self, key, element=None, reset=True):
        if reset:
            self.action_chains.reset_actions()


        if element:
            self.action_chains.key_up(key, element.get_element()).perform()

        else:
            self.action_chains.key_up(key).perfrom()

    def move_mouse(self, xofffset, yoffset, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_by_offset(xofffset, yoffset).perform()

    def move_to_element(self, to_element, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_to_element(to_element.get_element()).perform()

    def move_to_element_with_offset(self, to_element, xoffset, yoffset, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.move_to_element_with_offset(to_element.get_element(), xoffset, yoffset).perform()

    def send_keys(self, keys_to_send, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.send_keys(keys_to_send).perform()
    def send_keys_to_element(self, element, keys_to_send, reset=True):
        if reset:
            self.action_chains.reset_actions()

        self.action_chains.send_keys_to_element(element.get_element(), keys_to_send).perform()







        




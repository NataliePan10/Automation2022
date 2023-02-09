from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
from webelements.actions import Actions
from webelements.dropdown import Dropdown
from webelements.browser import Browser
URL = "https://cleveronly.com/brainbucket"

class NavigationBar:
    def __init__(self, browser):
        self.actions = Actions(browser)

        self.desktops = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[1]")
        self.laptops = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[2]")
        self.components = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[3]")
        self.tablets = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[4]")
        self.software = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[5]")
        self.phones_and_pdas = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[6]")
        self.cameras = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[7]")
        self.mp3_players = Element(browser, By.XPATH, "//ul[@class='nav navbar-nav']/li[8]")

        #Dropdowns
        self.dropdown_list_xpath = "//div[@class='dropdown-menu']"
        self.desktops_dropdown = Dropdown(browser, By.XPATH, self.desktops.get_locator() + self.dropdown_list_xpath)
        self.laptops_dropdown = Dropdown(browser, By.XPATH, self.laptops.get_locator() + self.dropdown_list_xpath)
        self.components = Dropdown(browser, By.XPATH, self.components.get_locator() + self.dropdown_list_xpath)
        self.tablets = Dropdown(browser, By.XPATH, self.tablets.get_locator() + self.dropdown_list_xpath)
        self.software = Dropdown(browser, By.XPATH, self.software.get_locator() + self.dropdown_list_xpath)
        self.phones_and_pdas = Dropdown(browser, By.XPATH, self.phones_and_pdas.get_locator() + self.dropdown_list_xpath)
        self.cameras = Dropdown(browser, By.XPATH, self.cameras.get_locator() + self.dropdown_list_xpath)
        self.mp3_players = Dropdown(browser, By.XPATH, self.mp3_players.get_locator() + self.dropdown_list_xpath)


    def show_all_desktops(self):
        self.actions.move_to_element(self.desktops)
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(),'Show All Desktops')]")

    def show_pcs(self):
        self.actions.move_to_element(self.desktops)
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(),'PC')]")


    def show_mac_desktops(self):
        self.actions.move_to_element(self.desktops)
        self.desktops_dropdown.select_by_option_xpath("//a[contains(text(),'Mac')]")

    def show_all_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_mac_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[contains(text(), 'Macs')]")

    def show_windows_laptops(self):
        self.actions.move_to_element(self.laptops)
        self.laptops_dropdown.select_by_option_xpath("//a[contains(text(), 'Windows')]")

    def show_all_components(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[@class='see-all']")

    def show_mice(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Mice')]")

    def show_monitors(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Monitors')]")

    def show_phones_and_pdas(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phones_and_pdas_dropdown.select_by_option_xpath("//a[@class='see-all']")
        self.show_phones_and_pdas().click

    def show_pdas(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phones_and_pdas.dropdown.select_by_option.xpath("//a[contains(text(), 'PDAs']")

    def show_phones(self):
        self.actions.move_to_element(self.phones_and_pdas)
        self.phones_and_pdas.dropdown.select_by_option_xpath("//a[contains(text(), 'Phones']")

    def show_printers(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Printers')]")

    def show_scanners(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'Scanners')]")


    def show_web_cameras(self):
        self.actions.move_to_element(self.components)
        self.components_dropdown.select_by_option_xpath("//a[contains(text(), 'WebCameras')]")




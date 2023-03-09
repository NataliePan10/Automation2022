from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element
from Internship.BotanikaBeautyTests.components.actions import Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



class NewProductsPage:
    def __init__(self, browser):
        self.actions = Actions(browser)
        self.navbar = NavigationBar(browser)

        self.add_to_cart_under_shampoo = Element(browser, By.XPATH, "//span[@data-id='39670945120310']/span")
        self.add_to_cart_under_conditioner = Element(browser, By.XPATH, "//span[@data-id = '39670944006198']")
        self.add_to_cart_under_trio_bundle = Element(browser, By.XPATH, "//span[@data-id = '39670955016246']")
        self.add_to_cart_under_spray = Element(browser, By.XPATH, "//span[@data-id = '39670942629942']")

        #self.add_to_cart_btn = Element(browser, By. XPATH, "//span[@data-id = '39670945120310']")
        self.add_to_cart_box = Element(browser, By.XPATH, "//span[@id='AddToCartText-product-template-4']")

        self.conditioner = Element(browser, By.XPATH, "//a[contains(text(),'The Manager Silkening Conditioner')]")
        self.shampoo = Element(browser, By. XPATH, "(//a[@title = 'The Cleanser Hydrating Shampoo'])")
        self.trio_bundle = Element(browser, By.XPATH, "//a[contains(text(),'Trio Bundle: The Manager, Lifter & Cleanser')]")
        self.spray = Element(browser, By.XPATH, "//a[contains(text(),'The Lifter Volumizer Spray')]")

        self.cart_indicator = Element(browser, By.XPATH, "//span[@title]")

        self.amount_of_new_product = Element(browser, By.XPATH, "//input[@type = 'number']")

        self.increase_product_amount = Element(browser, By.XPATH, "//div[@class = 'quantity']")
        self.decrease_product_amount = Element(browser, By.XPATH, "//input[@type = 'number']")

        self.got_btn = Element(browser, By.XPATH, "//button[@class='btn btn-theme js-btn-ok']")


        #Add quickshop btn, remove new products, add navigation bar class

    def quickshop(self, product):
        if product == "The Cleanser Hydrating Shampoo":
            self.add_to_cart_under_shampoo.click()


        if product == "The Manager silkening conditioner":
            self.actions.move_to_element(self.conditioner)
            self.conditioner.click()
            #add code to click on quickshop bnt under manager silking conditioner

        if product == "Trio Bundle:The manager, Lifter & Cleanser":
            self.actions.move_to_element(self.trio_bundle)
            self.trio_bundle.click()

        if product == "The Lifter Volumizer Spray":
            self.actions.move_to_element(self.spray)
            self.spray.click()


    def add_to_cart(self, product):
        self.got_btn.click()
        if product == "The Cleanser Hydrating Shampoo":
            self.actions.move_to_element(self.add_to_cart_under_shampoo)
            self.add_to_cart_under_shampoo.click()



        if product == "The Manager silkening conditioner":
            self.actions.move_to_element(self.conditioner)
            self.conditioner.click()
            #add code to click on quickshop bnt under manager silking conditioner

        if product == "Trio Bundle:The manager, Lifter & Cleanser":
            self.actions.move_to_element(self.trio_bundle)
            self.trio_bundle.click()

        if product == "The Lifter Volumizer Spray":
            self.actions.move_to_element(self.spray)
            self.spray.click()


    def get_shampoo_title(self):
        return self.shampoo.get_text()

    def get_conditioner_title(self):
        return self.conditioner.get_text()

    def get_trio_bundle_title(self):
        return self.trio_bundle.get_text()

    def get_spray_title(self):
        return self.spray.get_text()

    def get_cart_title(self):
        return self.cart_indicator.get_text()

    def get_cart_indicator(self):
        return self.cart_indicator.get_text()

    def amount_of_new_product(self):
        return self.amount_of_new_product.enter_text()


    def increase_product_amount(self):
        return self.increase_product_amount.click()

    def decrease_product_amount(self):
        return self.decrease_product_amount.click()






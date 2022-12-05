from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os




class Browser:
    """
    This class is wrapper around Selenium driver
    """
    def __init__(self, url, browser_name="chrome", time_wait = 10):
        project_name = "Automation2022"
        current_dir = os.getcwd()
        print("Scripts are executed from:", current_dir)
        if project_name in current_dir:
            # we are running locally and we need to reverse our folder structure to find the correct folder
            while not current_dir.endswith(project_name):
                current_dir = os.path.split(current_dir)[0]
                if current_dir == '/':
                    raise Exception("Project folder wasn'nt found in", os.getcwd())
        driver_dir = os.path.join(current_dir, 'drivers')
        print(driver_dir)
        # decide which browser to open, can be extended
        if browser_name.lower() == "firefox":
            self.driver = webdriver.Firefox(executable_path=os.path.join(driver_dir, 'geckodriver'))
            self.driver.maximize_window()
        elif browser_name.lower() == "chrome":
            self.driver = webdriver.Chrome(executable_path=os.path.join(driver_dir, 'chromedriver.exe'))


        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # by default 10, but we can add this like a parameter

    def get_wd_wait(self):
        return self.wait

    def get_driver(self):
        return self.driver

    def shutdown(self):
        self.driver.quit()

    def switch_to_iframe(self):
        self.switch_to_iframe()
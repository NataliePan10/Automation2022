from configparser import ConfigParser

class IninFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = ConfigParser()
            self.data.read_file(config_file)

    def get_browser(self):
        value = self.data.get('environment', 'browser', fallback=None)
        if value is None:
            raise Exception("Browser option is not present in the config file")
        return value

    def get_wait_time(self):
        value = self.data.get('environment', 'wait', fallback=None)
        if value is None:
            raise Exception("Wait time option is not present in the config file")
        return int(value)

    def get_email(self):
        value = self.data.get('section name', 'email', fallback=None)
        if value is None:
            raise Exception("Email is not found in the config file")
        return value

    def get_password(self):
        value = self.data.get('section name', 'password', fallback=None)
        if value is None:
            raise Exception("Password is not found in the config file")
        return value

    def get_height(self):
        value = self.data.get('environment', 'height', fallback=None)
        if value is None:
            raise Exception("Height is not found in config file")
        return int(value)

    def get_width(self):
        value = self.data.get('environment', 'width', fallback=None)
        if value is None:
            raise Exception("Width is not found in config file")
        return int(value)


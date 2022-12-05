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

    def get_user1_email(self, section_name):
        if user1_email not in self.data.keys():
            raise Exception("Email is not found in the config file")
        return int(self.data['email'])

    def get_user1_password(self, section_name):
        if user1_password not in self.data.keys():
            raise Exception("Password is not found in the config file")
        return int(self.data['password'])

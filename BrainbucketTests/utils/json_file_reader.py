import json

class JsonFileReader:
    def __init__(self, filename):
        self.data = None

        with open(filename, 'r') as config_file:
            self.data = json.load(config_file)

    def get_browser(self):
        if 'browser' not in self.data.keys():
            raise Exception("Browser option is not present in the config file")
        return self.data['browser']

    def get_wait_time(self):
        if 'wait_time' not in self.data.keys():
            raise Exception("Wait time option is not present in the config file")
        return int(self.data['wait_time'])

    def get_user1_email(self, section_name):
        if user1_email not in self.data.keys():
            raise Exception("Email is not found in the config file")
        return int(self.data['email'])

    def get_user1_password(self, section_name):
        if user1_password not in self.data.keys():
            raise Exception("Password is not found in the config file")
        return int(self.data['password'])

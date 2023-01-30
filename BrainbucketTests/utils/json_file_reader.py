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

    def get_email(self):
        if user_email not in self.data.keys():
            raise Exception("Email is not found in the config file")
        return self.data['email']

    def get_password(self):
        if user_password not in self.data.keys():
            raise Exception("Password is not found in the config file")
        return self.data['password']

    def get_url(self):
        if 'url' not in self.data.keys():
                raise Exception("URL option is not present in the config file")
        return self.data['url']

    def get_height(self):
        if height not in self.data.keys():
            raise Exception("Height is not found in the config file")
        return self.data['height']

    def get_width(self):
        if width not in self.data.keys():
            raise Exception("Width is not found in the config file")
        return self.data['width']
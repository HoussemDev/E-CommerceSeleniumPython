import configparser

config = configparser.RawConfigParser()
config.read("Configuration/config.ini")


class ReadConfig:

    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmail():
        email = config.get('common info', 'useremail')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
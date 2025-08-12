import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini", encoding='utf-8')

class ReadConfig:
    @staticmethod
    def get_login_page_url():
        url = config.get('login info','login_url')
        return url

    @staticmethod
    def get_email():
        email = config.get('login info', 'email')
        return email

    @staticmethod
    def get_invalid_email():
        invalid_email = config.get('login info', 'invalid_email')
        return invalid_email
    
    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_restaurant_name():
        restaurant_name = config.get('restaurant info', 'restaurant_name')
        return restaurant_name
    
    
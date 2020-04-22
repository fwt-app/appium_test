import logging
from page_object.desired_caps import appium_desired
from page_object.common import common
from selenium.webdriver.common.by import By

class loginView(common):
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    def login_action(self,username,password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info('=====login_action=====')
        logging.info('username:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password:%s' %password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

if __name__ == '__main__':
    driver=appium_desired()
    l=loginView(driver)
    l.login_action('zxw1234','zxw123456')
from page_object.baseView import BaseView
from page_object.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By


class common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.XPATH,'//*[@resource-id="com.tal.kaoyan:id/tv_skip"][@index="2"]')

    def check_cancelBtn(self):
        logging.info('=====check_cancelBtn=====')
        try:
            cancelBtn = self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            print('No cancelBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('=====check_skipBtn=====')
        try:
            skipBtn = self.driver.find_element(*self.skipBtn)

        except NoSuchElementException:
            print('No skipBtn')
        else:
            skipBtn.click()

if __name__ == '__main__':
    driver=appium_desired()
    com=common(driver)
    com.check_cancelBtn()

    com.check_skipBtn()
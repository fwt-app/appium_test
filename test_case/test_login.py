from test_case.myUnit import StartEnd
from page_object.login_view import loginView
import unittest
import logging

class TestLogin(StartEnd):

    def test_login_zxw2018(self):
        logging.info('=====test_login_zxw2018=====')
        l=loginView(self.driver)
        l.login_action('自学网2018','zxw2018')

    def test_login_zxw2017(self):
        logging.info('=====test_login_zxw2017=====')
        l=loginView(self.driver)
        l.login_action('自学网2017','zxw2017')

    def test_login_error(self):
        logging.info('====test_login_error====')
        l=loginView(self.driver)
        l.login_action('777','0999')

if __name__ == '__main__':
    unittest.main()
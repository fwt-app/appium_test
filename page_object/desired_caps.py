
from appium import webdriver
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException
import logging.config

file=open('../yaml_conf/desired_caps.yaml','r')
data1= yaml.load(file,Loader=yaml.FullLoader)
#yaml.warnings({'YAMLLoadWarning': False})

#data= yaml.full_load(file)

#data=yaml.load(file)


CON_LOG='../log/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

def appium_desired():
    desired_caps = {}
    desired_caps['platformName'] = data1['platformName']
    desired_caps['platformVersion'] = data1['platformVersion']
    desired_caps['deviceName'] = data1['deviceName']
    desired_caps['app'] = data1['app']
    desired_caps['appPackage'] = data1['appPackage']
    desired_caps['appActivity'] = data1['appActivity']
    desired_caps['noReset'] = data1['noReset']
#    desired_caps['unicodeKeyboard'] = data1['unicodeKeyboard']
   # desired_caps['resetKeyboard'] = data1['resetKeyboard']
    logging.info('start app...')
    driver = webdriver.Remote('http://' + str(data1['ip']) + ':' + str(data1['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver
if __name__ == '__main__':
    appium_desired()

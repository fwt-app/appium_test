from appium import webdriver
import yaml
import logging
from selenium.common.exceptions import NoSuchElementException
import logging.config
from os import path

file=open('../yaml_conf/desired_caps.yaml','r')
data=yaml.load(file,Loader=yaml.FullLoader)

#CON_LOG='log.conf'
#logging.config.fileConfig(CON_LOG)
#logging=logging.getLogger()

log_path = "../log/log.conf"
log_file_path = path.join(path.dirname(path.abspath(__file__)), log_path)
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("predict")

desired_caps={}
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']
desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']
logging.info('start app...')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)

def check_cancelBtn():
    logging.info('check cancelBtn')
    try:
        cancelBtn=driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        logging.info('No cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    logging.info('check skipBtn')
    try:
        skipBtn=driver.find_element_by_xpath('//android.widget.TextView[@text="跳过"]')
        #skipBtn=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        logging.info('No skipBtn')
    else:
        skipBtn.click()
check_cancelBtn()
#print(driver.contexts)
#driver.implicitly_wait(5)
check_skipBtn()

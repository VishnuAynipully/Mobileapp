from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
 
class DeckerApp:
    cap={
        "deviceName":"Samsung",
        "platformName":"Android",
        "automationName":"uiAutomator2",
        # "version":"9.0",
        # "udid":"emulator-5554",
        "browserName":"chrome",
        "chromedriverExecutable":"C:\\Users\\2022402\\Downloads\\chromedriver.exe"
    }
 
    def initiate_Driver(self):
 
    #self.appium_service =AppiumService()
    #global appium service
        try:
            global driver
            #driver = webdriver.Remote("http:localhost:4723/wd/hub", self.desired_caps)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
        except TypeError:
            print("error: Appium Server is not Working ....")
            
    def launch_Appium_Driver(self):
   
        driver.get("https://www.quest-global.com/")
        time.sleep(15)

    def quit_session():
        driver.quit()    
obj = DeckerApp()
obj.initiate_Driver()
obj.launch_Appium_Driver()
obj.quit_session()

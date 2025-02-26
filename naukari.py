from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
class DockerApp:
    cap= {
        "deviceName":"Samsung",
        "platformName":"Android",
        "automationName":"UiAutomatior2",
        "app":""
    }
    def initiate_Driver(self):
        #self.appium_service=AppiumService()
        #global appium_service
        try:
            global driver
            #driver=webdriver.Remote("http://localhost:4723/wd/hub",self.desired_caps)
            driver=webdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdletimeout":500})
        except TypeError:
            print("Error:Appium Server not working...")
 
    def validate_Launch_Screen(self):
        try:
            #validate launch screen image...
            if driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@resource-id='com.naukri.recruiterapp:id/iv_logo']").is_displayed():
                print("Launch Screen image is present")
 
                #click on skip button
                driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.naukri.recruiterapp:id/tv_skip']").click()  
                time.sleep(5)
                print("User clickend on SKIP link")
 
                #Give Email and Password
 
 
                driver.find_element(AppiumBy.ID,"com.naukri.recruiterapp:id/edt_email_id").send_keys("test@email.com")  
                driver.find_element(AppiumBy.ID,"com.naukri.recruiterapp:id/edt_password").send_keys("password1")  
                print("User have written id/pw")
 
                time.sleep(20)
        except:
            print("kubernetes logo is not present")
    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully...")
        time.sleep(20)
 
obj=DockerApp()
obj.initiate_Driver()
obj.validate_Launch_Screen
obj.close_driver()  
 
 
 

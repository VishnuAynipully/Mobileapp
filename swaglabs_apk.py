from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time

class Swagslab:

    cap = {
        "appium:deviceName": "Samsung",
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\2022402\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
    }
    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")

    def test1(self):
 
        try:
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
            time.sleep(2)
            driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='LOGIN']").click()
            time.sleep(2)
        except:
            print("Error occured.")
    def Performactions(self):
        try:
            driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='ADD TO CART'])[1]").click()
            driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='ADD TO CART']").click()
            
        except:
            print("error occured while adding products")
    
    #Validating cart products
    def Validation(self):
        try:
            if driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='2']").is_displayed:
                print("The cart is validated")
            else:
                print("The cart is invalidated")
            #validating count button
            count = len(driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='REMOVE']"))
            print("The no of cart items is,",count)

        except:
            print("valiation is not working")

    def Checkout(self):
        try:
            driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.view.ViewGroup").click()
            time.sleep(5)
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(104, 1809)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(111, 930)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            driver.find_element(AppiumBy.XPATH,"//android.view.ViewGroup[@content-desc='test-CHECKOUT']").click()
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-First Name']").send_keys("vishnu")
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Last Name']").send_keys("Aynipully")
            driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Zip/Postal Code']").send_keys("680620")
            time.sleep(5)
            driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='CONTINUE']").click()
            time.sleep(5)
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(734, 2143)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(718, 503)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
            driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='FINISH']").click()
            time.sleep(5)


        except:
            print("checkout failed")


    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(20)

obj = Swagslab()
obj.initiate_Driver()
obj.test1()
obj.Performactions()
obj.Validation()
obj.Checkout()
obj.close_driver()
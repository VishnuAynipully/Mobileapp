from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
 
def scroll(driver):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(545, 1846)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(559, 774)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
 
def username():
        return "//android.widget.EditText[@content-desc='test-Username']"
 
def password():
        return "//android.widget.EditText[@content-desc='test-Password']"
 
def login_btn():
        return "//android.widget.TextView[@text='LOGIN']"
 
def item_count():
        return "//android.widget.TextView[@content-desc='test-Item title']"
 
def print_item(i):
        return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"
 
def nav_to_cart():
        return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
 
def remove_btn():
        return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
 
def checkout():
        return "//android.view.ViewGroup[@content-desc='test-CHECKOUT']"
 
def fname():
        return "//android.widget.EditText[@content-desc='test-First Name']"
 
def lname():
        return "//android.widget.EditText[@content-desc='test-Last Name']"
 
def postal_code():
        return "//android.widget.EditText[@content-desc='test-Zip/Postal Code']"
 
def continue_btn():
        return "//android.view.ViewGroup[@content-desc='test-CONTINUE']"
 
def finish_btn():
        return "test-FINISH"
 
def back_btn():
        return "test-BACK HOME"
 
def click_filter():
        return "//android.view.ViewGroup[@content-desc='test-Modal Selector Button']/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView"
 
def low_to_high():
        return "//android.widget.TextView[@text='Price (low to high)']"
def first_element():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$7.99']"
def second_element():
        return "//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']"
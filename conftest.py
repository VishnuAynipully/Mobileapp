import json
import sys
from pathlib import Path
from appium import webdriver
from appium.options.common import AppiumOptions
sys.path.append(str(Path(__file__).parent.parent))
import pytest

@pytest.fixture(scope="function")
def launch_app(request):
    try:
        cap= {
        "deviceName":"Samsung",
        "platformName":"Android",
        "automationName":"UiAutomatior2",
        "app":""
    }
        print("initiatind the app instance driver")
        driver=webdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(cap))
        request.instance.driver = driver
        yield driver
        driver.quit()
    except:
        print("Unable to launch the App")
    
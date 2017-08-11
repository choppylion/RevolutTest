from appium import webdriver
import pytest


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = 'Revolut_qa_4.3.0.237.apk'

@pytest.fixture
def driver():
    d = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    d.launch_app()
    yield d
    d.close_app()

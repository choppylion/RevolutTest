from collections import OrderedDict
import json
import os


from appium import webdriver
import pytest


def PATH(p):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class TestConfig:

    def __init__(self):
        self.caps, self.data = self.import_test_data()

    def import_test_data(self):
        filename = "boot_test_config.json"
        try:
            project_dir = os.path.dirname(os.path.abspath(__file__))
            path = os.path.abspath(os.path.join(project_dir, "configs", filename))
            with open(path, 'r') as fr:
                configs_dict = json.load(fr)
                cfg = OrderedDict([(test_name, test_config)
                                   for test_name, test_config in configs_dict.items()])
                for test_name, test_data in cfg.items():
                    yield test_data
        except Exception as e:
            raise IOError("Impossible to read test data:\n{}".format(e))


@pytest.fixture
def driver():
    url = 'http://localhost:4723/wd/hub'
    capabilities = {
        'platformName':     'Android',
        'deviceName':       'Android Emulator',
        'app':              PATH('app/Revolut_qa_4.3.0.237.apk'),
    }

    # setup
    d = webdriver.Remote(url, capabilities)
    d.launch_app()

    yield d

    # teardown
    d.quit()

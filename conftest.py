import pytest
from selenium import webdriver
from utilities.test_data import TestData
import inspect
import logging
"""
This file holds all tests vars to be used by all functions
 It can hols class/ fixtures/ function etc.
"""


@pytest.fixture
def initialize_driver():
    # Init driver with options
    print("Open Driver")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(TestData.url)
    yield driver
    print("Close Driver")
    driver.close()


@pytest.fixture
def loggen():
    FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
    DATEFMT = '%m/%d/%Y %I:%M:%S %p'
    logging.basicConfig(
                        format=FORMAT,
                        datefmt=DATEFMT,
                        handlers=[
                                    logging.FileHandler("./logs/automation.log"),
                                    logging.StreamHandler()
                                ]
                        )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger

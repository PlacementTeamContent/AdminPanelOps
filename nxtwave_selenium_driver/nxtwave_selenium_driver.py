from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class NxtWaveWebDriver:


    @staticmethod
    def get_driver(visible: bool = False):
        """
        :param visible: bool
        :return: selenium chrome webdriver
        Returns selenium chrome driver with visibility of browser window based on parameter 'visible'
        """
        options = Options()
        options.add_argument("--headless")
        if visible:
            return webdriver.Chrome()
        else:
            return webdriver.Chrome(options=options)


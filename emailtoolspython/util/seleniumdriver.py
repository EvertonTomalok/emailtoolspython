from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from .agents import choice_one_user_agent


class Driver:

    def __init__(self):

        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument('--allow-insecure-localhost')

    def _mount_driver(self, use_ua=False):

        if use_ua:
            self.options.add_argument('--user-agent=%s' % choice_one_user_agent())

        return webdriver.Chrome(chrome_options=self.options)

    def get_page_source(self, url, use_user_agent=False):

        """
        Make sure to have chromedriver configured in the path /usr/bin or /usr/local/bin

        :param url: url to extract emails (STRING)
        :param use_user_agent: False or true (BOOL)
        :return: content html of the page.
        """

        driver = self._mount_driver(use_user_agent)
        driver.get(url)

        return driver.page_source

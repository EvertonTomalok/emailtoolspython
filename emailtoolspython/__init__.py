
"""
Python module for help working with Emails.
"""

__author__ = 'Everton Tomalok'
__version__ = '1.0.6'
__email__ = 'evertontomalok123@gmail.com'
name = 'emailtoolspython'

import re
import requests
from bs4 import BeautifulSoup
from .util.agents import choice_one_user_agent


class EmailTools:

    def __init__(self):
        self.regex_simple = r'\s?[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.?[a-zA-Z0-9-.]{0,2}\s?'

    @classmethod
    def _make_compiler(cls, can=False):

        # using another base_regex, different of the self.regex_simple
        base_regex = r'(\.[a-za-z0-9-_]+)*@[a-z0-9-]+\.([a-z0-9-]+)*(\.[a-z0-9-]+)*$'

        if not can:
            regex = '%s%s' % (r'^[a-zA-Z_]', base_regex)

            return re.compile(regex)

        elif can is True:
            regex = '%s%s' % (r'^[a-zA-Z0-9_]', base_regex)

            return re.compile(regex)

        else:
            raise KeyError('"can_starts_with_number" only receives False or True')

    @staticmethod
    def _get_content_page(url, user_agent=False):

        headers = {
            'Connection': 'keep-alive'
        }

        if user_agent:

            ua = choice_one_user_agent()
            headers['User-Agent'] = ua

        # Preparing URL, and make two requests, if the first is failed. One to https and other to http
        try:

            req = requests.get('https://%s'% url, headers=headers)

        except Exception:
            req = requests.get('http://%s' % url, headers=headers)

        return req.content

    @property
    def base_regex(self):
        return self.regex_simple

    def syntax_validation(self, email_parameter=None, can_starts_with_number=False):
        """
        A function to verify if the syntax of an email is valid. True is an email with syntax valid, and False an email
        with syntax invalid.

        To enable verification to emails that start with number, use can_starts_with_number=True  ...
        To disable this feature, use False instead.

        :param email_parameter: String
        :param can_starts_with_number: Bool
        :raise ValueError: Raises if any email isn't pass
        :return: Bool
        """

        if email_parameter is None:
            raise ValueError('You must pass an email as a STRING parameter in the function syntax_validation()')

        compiler = self._make_compiler(can_starts_with_number)

        match_result = compiler.search(email_parameter)

        if match_result is None:
            return False
        else:
            return True

    def extract_emails_from_text(self, text):

        """
        A method to extract all emails from a text. If any email can be extracted from the text passed, a empty list will
        be returned. Another way, all emails will be returned in a list.

        :param text: String
        :return: List
        """

        compiler = re.compile(self.base_regex)

        match_result = compiler.findall(text)

        match_result = [email.strip() for email in match_result]

        return match_result

    def extract_emails_from_web(self, url, user_agent=False, clean_end=[]):

        """
        An url must be passed, like this example: "google.com" or "www.google.com"
        After processing the request, all emails of that page will be extracted, and returned in a list.
        If any email could be found, an empty list will be returned.
        You can "pass user_agent=True", to use an user agent in Header of the request.
        In order to pre processing your email, you can pass a list of 'strings' to be cleaned in email. For example,
        if one email is email@domain.com.netPhrase, you can use clean_end=['.net']. It's very recommended you use '.com'
        in the last position of the array, because if the same email "email@domain.com.netPhrase", if you use
        clean_end=['.com','.net'], your email returned will be "email@domain.com", not "email@domain.com.net" as it must
        to be.

        :param url: String
        :param user_agent: Bool
        :return: List
        """

        content = self._get_content_page(url, user_agent)
        soup = BeautifulSoup(content, "lxml")

        emails_dirty = self.extract_emails_from_text(soup.text)

        emails = list()

        for email in emails_dirty:

            if clean_end != []:
                for item in clean_end:
                    if item in email:
                        email = email.split(item)[0] + item

            if email not in emails:
                emails.append(email)

        return emails
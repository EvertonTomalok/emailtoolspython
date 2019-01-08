
"""
Python module for help working with Emails.
"""

import re
import requests

from bs4 import BeautifulSoup
from .util.agents import choice_one_user_agent
from .util.seleniumdriver import Driver
import socket
import dns.resolver
import dns.name
import smtplib
from dns.resolver import NXDOMAIN, NoAnswer, Timeout


name = 'emailtoolspython'
__author__ = 'Everton Tomalok'
__version__ = '0.2.1'
__email__ = 'evertontomalok123@gmail.com'


class EmailTools:

    def __init__(self):
        self.regex_simple = r'\s?[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.?[a-zA-Z0-9-.]{0,2}\s?'

    @classmethod
    def _make_compiler(cls, can=False):

        # using another base_regex, different of the self.regex_simple
        base_regex = r'[a-za-z0-9_\.]+@[a-z0-9-]+\.([a-z0-9-]+)*(\.[a-z0-9-]+)*$'

        if not can:
            regex = '%s%s' % (r'^[^0-9]', base_regex)

            return re.compile(regex)

        elif can is True:

            return re.compile(base_regex)

        else:
            raise KeyError('"can_starts_with_number" only receives False or True')

    @staticmethod
    def _get_content_page(url, user_agent=False, use_selenium=False):

        if not use_selenium:

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

        else:
            driver = Driver()

            return driver.get_page_source('http://%s' % url, user_agent)

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

    def domain_smtp_validation(self, domain):
        """
        It's a function do validate if a domain exists in mx records from a smtp server.
        Returns 200 if the domain exists, 400 if it doesn't exist, and 401 to you try repeat the test later.
        :param domain: String
        :return: Integer
                 200 - Ok
                 400 - Not Found
                 401 - Try Later
        """

        assert isinstance(domain, str), 'A STRING containing a domain pattern, must be passed as parameter.'

        try:
            dns.resolver.query(domain, 'mx')
            return 200

        except NXDOMAIN:
            return 400
        except NoAnswer:
            return 400
        except Timeout:
            return 401

    def email_smtp_validation(self, email_to_validate):
        """
        It's a function to validade in SMTP, if exists a server with domain of the email, and
        :param email_to_validate: STRING likes a email "example@domain.com"
        :return: INTEGER
                 200 - The email is valid
                 400 - The email is invalid
                 401 - Try later
                 402 - The domain wasn't founded
                 403 - The syntax is invalid
        """

        if not self.syntax_validation(email_to_validate, True):
            """
            First validation. If the syntax isn't a valid email, 405 is returned.
            """
            return 403

        try:
            """
            Now, we'll validate if the domain is registered in a SMTP server, and after this, try to capture a ehlo msg
            and the hello message from server.
            
            If the server sent a hello message for us, the email is valid. 
            
            Some servers are catch all, accepting all email as valid, for example a email 
            banana_12351513ksfa@domain-catch-all.com, this email will be returned as valid, but it isn't.
            """

            # Testing if domain is registered as a server.
            records = dns.resolver.query(email_to_validate.split('@')[1], 'mx')

            mx_record = records[0].exchange
            # Searching for preferences from server
            records[0].preference

            mx_record = str(mx_record)

            # connecting to the STMP
            smtp_server = smtplib.SMTP(timeout=15)
            smtp_server.set_debuglevel(0)
            smtp_server.connect(mx_record)

            # Searching for hello response. If all occur ok, no exceptions will be raised.
            smtp_server.helo()
            smtp_server.helo_resp
            smtp_server.ehlo_msg

            # Send a signal like an valid text email to the server.
            smtp_server.mail('teste@gmail.com')

            code, message = smtp_server.rcpt(email_to_validate)
            smtp_server.quit()

            if code == 250:
                """ 
                The email is valid 
                """
                return 200

            else:
                """
                The email isn't valid
                """
                return 400

        except Exception as err:

            """
            Looking for the exception.
            """

            error = str(type(err))

            if 'dns.exception.Timeout' in error:
                return 401
            elif 'dns.resolver.NoAnswer' in error:
                return 402
            elif 'dns.resolver.NXDOMAIN' in error:
                return 402
            elif 'SMTPServerDisconnected' in error:
                return 400
            else:
                return 400

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

    def extract_emails_from_web(self, url, user_agent=False, clean_end=[], use_selenium=False):

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

        try:
            socket.gethostbyname(url)
        except socket.gaierror:
            raise ConnectionError('Probably the url "{}" is not valid.'.format(url))

        content = self._get_content_page(url, user_agent, use_selenium)
        soup = BeautifulSoup(content, "lxml")

        emails_dirty = self.extract_emails_from_text(soup.text)

        emails = list()

        for email in emails_dirty:

            if clean_end != []:
                for item in clean_end:
                    if item in email:
                        email = email.split(item)[0] + item

                        break

            if email not in emails:
                emails.append(email)

        return emails

import re
import requests


class EmailTools:

    def __init__(self):
        self.regex_simple = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\.?[a-zA-Z0-9-.]{0,2}'

    @classmethod
    def _make_compiler(cls, can=False):

        base_regex = r'(\.[a-za-z0-9-_]+)*@[a-z0-9-]+\.([a-z0-9-]+)*(\.[a-z0-9-]+)*$'

        if not can:
            regex = '%s%s' % (r'^[a-zA-Z_]+', base_regex)

            return re.compile(regex)

        elif can is True:
            regex = '%s%s' % (r'^[a-zA-Z0-9_]+', base_regex)

            return re.compile(regex)

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

    def extract_emails_from_text(self, text=None):

        """
        A method to remove all emails from a text.

        :param text: String
        :return: List
        """

        compiler = re.compile(self.regex_simple)

        match_result = compiler.findall(text)

        if match_result == []:
            return False
        else:
            return match_result

    def extract_emails_from_web(self, url=None):

        # Will be implemented in the future
        pass


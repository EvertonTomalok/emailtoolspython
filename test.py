from emailtoolspython import EmailTools


if __name__ == '__main__':

    email = EmailTools()

    # My personal email
    print(email.email_smtp_validation('evertontomalok123@gmail.com'))

    # This email doesn't exist
    print(email.email_smtp_validation('evertontomalok123123123@gmail.com'))

    # Probably this domain is invalid
    print(email.email_smtp_validation('asdar1t1@214135135qsas1.com'))

    # The syntax is invalid
    print(email.email_smtp_validation('not_a_valid_email@not-domain'))

    # Validating a domain
    print(email.domain_smtp_validation('https://www.gmail.com'))

    # Validating domain of the third example, and it really doesn't exist (at least for now haha)
    print(email.domain_smtp_validation('214135135qsas1.com'))

    # Getting emails from webpage
    print(email.extract_emails_from_web('http://laclaw.com.br/Contato-e-Localizacao.html', user_agent=True))

    # Getting emails from webpage, IGNORING CASE
    print(email.extract_emails_from_web('http://nuitka.net/pages/impressum.html', user_agent=True, ignore_case=True))

    """
    Result expected:
        200
        400
        402
        403
        {'status': 200, 'ip_address': '172.217.28.133'} # The ip_address can change
        {'status': 400, 'ip_address': None}
        ['laclaw@laclaw.com.br']
        ['Kay.Hayen@gmail.com']
    """

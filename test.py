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
    print(email.domain_smtp_validation('gmail.com'))

    # Validating domain of the third example, and it really doesn't exist (at least for now haha)
    print(email.domain_smtp_validation('214135135qsas1.com'))

    """
    Result expected:
        200
        400
        402
        403
        200
        400
    """

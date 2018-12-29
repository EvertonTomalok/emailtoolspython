from emailtoolspython import EmailTools


if __name__ == '__main__':

    email = EmailTools()

    # My personal email
    print(email.smtp_validation('evertontomalok123@gmail.com'))

    # This email isn't exist
    print(email.smtp_validation('evertontomalok123123123@gmail.com'))
    print(email.smtp_validation('asdar1t1@214135135qsas1.com'))

    # The syntax is invalid
    print(email.smtp_validation('not_a_valid_email@not-domain'))

    """
    Result expected:
        200
        400
        404
        405 
    """

from emailtoolspython import EmailTools


if __name__ == '__main__':

    validator = EmailTools()

    # My personal email
    print(validator.smtp_validation('evertontomalok123@gmail.com'))

    # This email isn't exist
    print(validator.smtp_validation('asdar1t1@214135135qsas1.com'))

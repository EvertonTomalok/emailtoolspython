### emailtoolspython
A serie of methods to help you work with validation and extraction of e-mails

# Usage
    >> from emailtoolspython import EmailTools

    >> email = EmailTools()

## Syntax Email Validation
To verify if the syntax of an email is valid, use the method bellow:
    
    >> email.syntax_validation('evertontomalok123@gmail.com')
    >> True
    >> email.syntax_validation('example@invalid_domain')
    >> False
    
Passing the Parameter "can_starts_with_number=True", you can verify e-mails that starts with number:

    >> email.syntax_validation('24hours_laundry@gmail.com')
    >> False
    >> email.syntax_validation('24hours_laundry@gmail.com', can_starts_with_number=True)
    >> True
    
 ## Extract Emails from a text
 To remove all emails from a text, use extract_emails_from_text():
    
    >> validator.extract_emails_from_text('lorsi sldaljq indajfa email@example.com sajdiosafhu. A example@email.com')
    >> ['email@example.com', 'example@email.com']

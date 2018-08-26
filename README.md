### emailtoolspython
A serie of methods to help you work with validation and extraction of e-mails

# Usage
    >> from emailtoolspython import EmailTools

    >> email = EmailTools()

<br>

## Syntax Email Validation
To verify if the syntax of an email is valid, use the method bellow:
    
    >> email.syntax_validation('evertontomalok123@gmail.com')
    >> True
    >> email.syntax_validation('example@invalid_domain')
    >> False
<br>
    
Passing the Parameter "can_starts_with_number=True", you can verify e-mails that starts with number:

    >> email.syntax_validation('24hours_laundry@gmail.com')
    >> False
    >> email.syntax_validation('24hours_laundry@gmail.com', can_starts_with_number=True)
    >> True
<br>
    
 ## Extracting Emails from a text
To extract all emails from a text, use extract_emails_from_text():
    
    >> validator.extract_emails_from_text('lorsi sldaljq indajfa email@example.com sajdiosafhu. A example@email.com')
    >> ['email@example.com', 'example@email.com']

<br>

## Extracting Emails from a web page
You can pass a site domain to extract_emails_from_web(), and all emails crawled in that page, will be returned in a list. 
Note, a domain must be passed like this: "creditas.com.br" or "www.creditas.com.br" or anothers ways "app.creditas.com.br"

    >> email.extract_emails_from_web('creditas.com.br')
    >> ['meajuda@creditas.com.br', 'ouvidoria@creditas.com.br', 'imprensa@creditas.com.br']
<br>

# Author
{
<br>'name': Everton Tomalok,<br>
'email': evertontomalok123@gmail.com<br>
}

### emailtoolspython
A serie of methods to help you work with validation and extraction of e-mails
<br>

# Install

    >> pip install --user emailtoolspython
    
    
Or you can download the zip of the module, to your root project
    
    >> cd path/to/your_module
    >> wget https://github.com/EvertonTomalok/emailtoolspython/archive/master.zip
    

# Usage

    # From pip
    >> from emailtoolspython import EmailTools

    >> email = EmailTools()
    
    # From wget
    >> from emailtoolspython.emailtoolspython import EmailTools

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

Use parameter "user_agent=True" to choice a random user agent to be used in the request
    
    >> email.extract_emails_from_web('urlexample.com', user_agent=True)
    
Pass a list of strings, of possibilities of end domains, if you need to clean emails crawleds from a web site.<br>
For example, a know my emails extracted from web site, will end with .br, I can pass "clean_end=['.br']". 

    >> email.extract_emails_from_web('lendico.com.br', user_agent=True)
    >> ['atendimento@lendico.com.br.leia']

    >> email.extract_emails_from_web('lendico.com.br', user_agent=True, clean_end=['.br'])
    >> ['atendimento@lendico.com.br']

<br>
It's very recommended pass '.com' as the last position in the list, because if the email finishes with other element
different of '.com', probably the email returned not will be the expected.<br>
For example, "email@domain.com.netPhrase", if you use "clean_end=['.com','.net']", your email returned will be "email@domain.com", 
not "email@domain.com.net" as it must to be. To avoid this, use "clean_end=['.net', '.com']", or the items you need.

    >> email.extract_emails_from_web('someurl.com', "clean_end=['.net', '.br', '.ar', '.us', '.com']")
    >> "email@domain.com.net" # The email returned in the method "extract_emails_from_web()", 
                              # it was "email@domain.com.netPhrase", and after pre processing it was this result.

    # Avoid using this:
    >> email.extract_emails_from_web('someurl.com', "clean_end=['.com', '.net']")
    >> "email@domain.com" # The email returned was not what probably you were expecting.

# Author
{
<br>'name': Everton Tomalok,<br>
'email': evertontomalok123@gmail.com<br>
}

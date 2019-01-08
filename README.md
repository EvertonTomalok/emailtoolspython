### emailtoolspython
A series of methods to help you work with validation and extraction of e-mails
<br>

# Install

    >> pip install --user emailtoolspython
    
    
Or you can download the zip of the module, to your root project
    
    >> cd path/to/your/module
    >> wget https://github.com/EvertonTomalok/emailtoolspython/archive/master.zip
    >> unzip master.zip
    >> mv emailtoolspython-master emailtoolspython

# Usage

    # From pip
    >> from emailtoolspython import EmailTools

    >> email = EmailTools()
    
    # From wget
    >> from emailtoolspython.emailtoolspython import EmailTools

    >> email = EmailTools()

<br>

## Syntax Email Validation
To verify if the syntax of an email is valid, use the method below:
    
    >> email.syntax_validation('evertontomalok123@gmail.com')
    >> True
    >> email.syntax_validation('example@invalid_domain')
    >> False
<br>
    
Passing the Parameter "can_starts_with_number=True", you can verify e-mail that starts a number:

    >> email.syntax_validation('24hours_laundry@gmail.com')
    >> False
    >> email.syntax_validation('24hours_laundry@gmail.com', can_starts_with_number=True)
    >> True
<br>
   
 ## Email SMTP Validation
 
 Pass an email to verify if domain is registered as a server, and if the email passed exists or not.
    
    # The example bellow is a valid email
    >> email.email_smtp_validation('evertontomalok123@gmail.com')   
    >> 200 
    
    # It isn't valid or the email couldn't be validated!
    >> email.email_smtp_validation('evertontomalok123123123@gmail.com')   
    >> 400 
    
    # The domain wasn't founded.
    >> email.email_smtp_validation('asdar1t1@214135135qsas1.com')
    >> 402 
    
    # The syntax is invalid
    >> email.email_smtp_validation('not_a_valid_email@not-domain')
    >> 403
    
    All returns:
         200 - The email is valid
         400 - The email is invalid
         401 - Try later
         402 - The domain wasn't founded
         403 - The syntax is invalid

  ## Validating a domain
    # A valid domain
    >> email.domain_smtp_validation('gmail.com'))
    >> 200
    
    # An invalid domain
    >> email.domain_smtp_validation('gmail.com.br'))
    >> 400
    
    # Timeout, try later
    >>  email.domain_smtp_validation('a_timeout_ocurried.com'))
    >> 401
    

 ## Extracting Emails from a text
To extract all emails from a text, use extract_emails_from_text():
    
    >> email.extract_emails_from_text('lorsi sldaljq indajfa email@example.com sajdiosafhu. A example@email.com')
    >> ['email@example.com', 'example@email.com']

<br>

## Extracting Emails from a web page
You can pass a site domain to extract_emails_from_web(), and all emails crawled in that page, will be returned in a list. 
Note, a domain must be passed like this: "creditas.com.br" or "www.creditas.com.br" or another way "app.creditas.com.br"

    >> email.extract_emails_from_web('creditas.com.br')
    >> ['meajuda@creditas.com.br', 'ouvidoria@creditas.com.br', 'imprensa@creditas.com.br']
<br>

Use parameter "user_agent=True" to choose a random user agent to be used in the request
    
    >> email.extract_emails_from_web('urlexample.com', user_agent=True)
    
Pass a list of strings, of possibilities of end domains, if you need to clean emails crawled from a website.<br>
For example, I know that my emails extracted from website, will end with .br, I can pass "clean_end=['.br']". 

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
        
 <br>
 
 You can use selenium (a webdriver that simulate you are using Google Chrome to access some page) to run and crawl web pages
 that need to execute javascript.
 Is very simple use this feature, you only need to have chromedriver in your path /usr/bin or /usr/local/bin, and pass the parameter
 "use_selenium" as True. It's important to mention, that the speed of the crawl will decrease.
 
    # Extract emails using Selenium in headless
    
    >> email.extract_emails_from_web('creditas.com.br', use_selenium=True, user_agent=True) 
    >> ['meajuda@creditas.com.br', 'ouvidoria@creditas.com.br', 'imprensa@creditas.com.br']
    
    # Using selenium, user_agent is not necessary. You can pass user_agent=False, if you want.
    
 You can download chromedriver here (https://sites.google.com/a/chromium.org/chromedriver/downloads) and you can access the
 official documentation - python bindings for selenium (https://selenium-python.readthedocs.io/installation.html).<br>
 For Windows users, go to the official documentation to have help to install chromedriver.
<br><br><br>
# Author
    {
        'name': Everton Tomalok,
        'email': evertontomalok123@gmail.com,
        'medium': medium.com/@everton.tomalok,
        'linkedin': linkedin.com/in/evertontomalok
    }

# Emailer
Multithreaded email process to send emails 

#### Binaries
linux and windows exectable binaries available. 

## Runtime Variables
set to environment:
| KEYWORDS | DEFAULT VALUE | TYPE | DESCRIPTION | REQUIRED | 
| :------ | :-----------: | :--: | :---------: | :------: |
| mail_user || string | mail server account username | true |
| mail_password || string | mail server account password| true |
| mail_host || string | mail server host | true |
| mail_sender || string | email of account that sends emails | true |
| mail_port || integer | mail server port | true |
| mail_receivers || string | JSON list of email receipients | true |
| max_thread_count | 5 | integer | maximun number of threads to start in running process | false |

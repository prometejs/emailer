from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Semaphore
from schemas import Message
import smtplib, logging

def send_email(payload:Message, sender:str, host:str, port:int, user:str, password:str, receivers:list=[], semaphore:Semaphore=None): 
    try:
        message = MIMEMultipart()
        message["From"]=sender
        message["To"]=', '.join(receivers)
        message["Subject"] = payload.subject
        message.attach(MIMEText(payload.body, "plain"))

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, password)  
            server.send_message
            server.sendmail(from_addr=sender, to_addrs=receivers, msg=message.as_string())
    except Exception as e:
        logging.error(f"{e.__class__}:{e}")
    else:
        logging.info("Success sending email")
    finally:
        if semaphore:semaphore.release()
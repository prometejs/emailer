from emailer import send_email
from schemas import Message
import concurrent.futures

max_thread_count = 5 # move to config management

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_thread_count) as executor:
        while True:
            # listen for message[blocking]
            message = {'sd':'sdsd', "body":"sdsdsd"}
            try:
                message = Message(**message)
            except Exception as e:
                print(f'validation failed: {e}')
                # log error
            else:
                print('adding message')
                executor.submit(
                    send_email, 
                    payload=message, 
                    receivers=['jay@gmail.com', 'ga@gmail.com'], 
                    sender="from@example.com", 
                    host="sandbox.smtp.mailtrap.io", 
                    port=25, 
                    user="", 
                    password=""
                )
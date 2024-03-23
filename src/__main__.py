from pydantic import ValidationError
from config import config, BASE_DIR
from emailer import send_email
from schemas import Message
import logging.config, \
    concurrent.futures, \
    threading, signal, \
    logging

sentinel = True

def exit_handler(signum, frame):
    logging.info(f"Program is existing with handler: {signum}")
    global sentinel
    sentinel = False

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)
logging.config.fileConfig(BASE_DIR.joinpath('logging.conf'))

def main():
    
    semaphore = threading.Semaphore(config.max_thread_count)

    with concurrent.futures.ThreadPoolExecutor(max_workers=config.max_thread_count) as executor:
        while sentinel:
            semaphore.acquire()  
            try:
                message = {'sd':'sdsd', "body":"jhgfd"} # listen for new message only when we have an available thread
                message = Message(**message)
            except Exception as e:
                logging.error(msg=e.errors() if isinstance(e, ValidationError) else e)
                semaphore.release()
            else:
                logging.info("Submitting task to thread pool")
                executor.submit(
                    send_email,  
                    payload=message, 
                    receivers=message.receivers or config.receivers, 
                    sender=message.sender or config.sender, 
                    host=config.host, 
                    port=config.port, 
                    user=config.user.get_secret_value(), 
                    password=config.password.get_secret_value(),
                    semaphore=semaphore,
                )

if __name__ == "__main__":
    main()
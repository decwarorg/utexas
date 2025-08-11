""" 'pkill -2 -f python', ctrlc=2=SIGINT, ctrlz=20=SIGTSTP """
from sshkeyboard import listen_keyboard, stop_listening
import signal
import threading
import cli
from robot2 import Robot2
args, kwargs = cli.main()
ro = Robot2(*args, **kwargs)
rothread = threading.Thread(target=ro.main)
rothread.start()
    
def main():
    signal.signal(signal.SIGINT, ctrlc)
    signal.signal(signal.SIGTSTP, ctrlz)
    try:
        ro.set_mode('2')
        listen_keyboard(on_press=keypress)
    except: pass

def keypress(key):
    print(f'{key} key pressed')
    ro.set_mode(key)
    if key == '0': stop_listening()

def ctrlc(sig, frame):
    print('ctrlc translated to 0 key')
    keypress('0')
    
def ctrlz(sig, frame):
    print('ctrlz translated to 0 key')
    keypress('0')
    
if __name__ == "__main__":
    main()

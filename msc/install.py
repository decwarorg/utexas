"""
put/create this install.py script file in a folder where you want the utexas repo to live
cd into that folder and use python to run this script, command is 'python3 install.py' on my mac
"""
import os
if not os.path.exists('utexas'): os.system('git clone https://gitlab.com/decwar/utexas.git')
os.chdir('utexas')
os.system('git fetch')
os.system('git reset --hard origin') # WARNING caution needed if you're coding in the repo
os.chdir('docker')
if not os.path.exists('dsk'):
    os.system('unzip dsk-20251103.zip') # this will eventually be unnecessary
    os.system('mv dsk-20251103 dsk')
os.chdir('..')
os.system('docker build -t utexas -f ./dockerfile-utexas .')
"""
cd into the utexas folder
do the command 'docker compose up' - it will show console messages of the dec10 starting
when it reaches 'utexas-1  | GAM assigned' it's finished and ready
open another terminal and do 'telnet localhost 2030' (may need to 'brew install telnet' on some macs)
"""

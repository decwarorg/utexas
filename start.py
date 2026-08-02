"""
to use this script to start the utexas container

    cd utexas
    python3 start.py
"""
import os
import argparse
import subprocess

def main(args):
    # if not os.path.exists('utexas'): os.system('git clone https://github.com/decwarorg/utexas.git')
    # os.chdir('utexas')
    if False: reset(args) # overwrites
    if not os.path.exists('docker/dsk'): os.system('unzip docker/dsk-20251103.zip && mv dsk-20251103 docker/dsk')
    if False: os.system(f'docker compose up --build --force-recreate utexas') # overwrites
    else: os.system(f'docker compose up utexas')
    
def reset(args):
    os.system('git fetch')
    os.system('git reset --hard origin')  # warning this overwrites local changes
    if args.latest: os.system(f'git checkout {latest_tag()}')

def latest_tag():
    os.system('git fetch --tags')
    latest = subprocess.getoutput("git describe --tags $(git rev-list --tags --max-count=1)")
    return latest

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("--latest", action="store_true")
    # parser.add_argument("--reset", action="store_true")
    # parser.add_argument("--norun", action="store_true")
    args = parser.parse_args()
    # if args.latest: args.reset = True
    main(args)

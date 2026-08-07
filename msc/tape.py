import time
import pexpect
import argparse
import os

def main():
    args, kwargs = cli()
    robot = Robot(*args, **kwargs)
    
class Robot:

    def __init__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        os.system('gcc back10.c -o back10')
        # os.system('rm -rf ./tmp')
        os.system('mkdir ./tmp')
        os.system('cp ./to-tape/* ./tmp')
        os.system('./back10 -cf ../tapes/utexas23-reconstruction.tap ./tmp/*')
        os.system('./back10 -lf ../tapes/utexas23-reconstruction.tap')
        # os.system(f'./create-tape-utexas23-reconstruction')
        self.telnet_entry()
        self.tops10_entry()
        self.tc.expect('.', timeout=10)
        self.tc.sendline('r backup')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('tape mta0:')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('rewind')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('inter')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('files')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('rest [,]*.*=*.*')
        self.tc.expect('/', timeout=10)
        self.tc.sendline('exit')
        self.tc.expect('.', timeout=10)
        self.tops10_exit()
        self.telnet_exit()
        exit()

    def telnet_entry(self):
        print('telnet entry')
        try:
            # self.tc = pexpect.spawn(f"telnet {self.kwargs['ip']} {self.kwargs['port']}", timeout=10, echo=True, encoding='utf-8', logfile=open(f'test.log', 'wt'))
            self.tc = pexpect.spawn(f"telnet {self.kwargs['ip']} {self.kwargs['port']}", timeout=10, echo=True)
            time.sleep(1)
            self.tc.expect('.', timeout=10)
            self.tc.sendline('')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
        except:
            pass

    def tops10_entry(self):
        print('tops10 entry')
        try:
            self.tc.sendline('')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
            self.tc.sendline(f"login {self.kwargs['ppn']}")
            time.sleep(1)
            self.tc.expect('.', timeout=10)
            self.tc.sendline('')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
        except:
            pass

    def tops10_exit(self):
        print('tops10 exit')
        try:
            self.tc.sendline('')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
            self.tc.sendline('kjob')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
        except:
            pass

    def telnet_exit(self):
        print('telnet exit')
        try:
            self.tc.sendline('')
            time.sleep(1)
            self.tc.expect('.', timeout=10)
            self.tc.sendcontrol(']')
            time.sleep(1)
            self.tc.sendline('close')
            time.sleep(1)
            self.tc.terminate(force=True)
        except:
            pass

def cli():
    cli = argparse.ArgumentParser(description='robot')
    cli.add_argument('-n', '--name', default='robot', type=str)
    cli.add_argument('-i', '--ip', default='localhost', type=str)
    cli.add_argument('-p', '--port', default=2030, type=int)
    cli.add_argument('-u', '--ppn', default='decwar', type=str)
    cli2 = cli.parse_args()
    args = set()
    args = tuple(args)
    kwargs = {}
    kwargs['name'] = cli2.name
    kwargs['ip'] = cli2.ip
    kwargs['port'] = cli2.port
    kwargs['ppn'] = cli2.ppn
    return args, kwargs
    
if __name__ == "__main__":
    main()

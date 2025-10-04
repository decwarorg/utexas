# project utexas robots

- [overview](#overview)
  - [main](#main)
  - [brain](#brain)
- [guide](#guide)
  - [setup](#setup)
  - [usage](#usage)

robots in the utexas folder are a 'simple as possible' minimalist skeleton. the concept is that descendant code can spin off and explore various other directions. for example it's natural to picture bringing in some machine learning, but this should be in a separate 'dedicated repo' project because it's something beyond 'absolutely essential'. another example is usage with decwar variants where the idea is to spin off a dedicated repo, make the minimalist skeleton go, and then extend with nice stuff only possible with the variant.  

# overview

boring 'infrastructure' stuff is corralled into main. fun 'decwar specific' stuff begins with the brain. the brain kicks in and takes over once the decwar game command prompt is available, and only knows about giving decwar commands and reacting to decwar output.

## main

the 'secret' here is that there's a child thread with a robot instance spinning slowly and handling telnet, tops10, and pregame topics. the main thread is meanwhile listening to the keyboard. the idea is that the main thread always has to ask and wait for the child thread to take any actions, hopefully in a calm, reasonable, clean way. for shutdown, the child should quit decwar, logout of tops10, and close the telnet connection, at which point finally both threads can exit.

## brain

a brain object is effectively a 'ship in the game'. it knows how to give commands and handle the resulting output. on top of that, it adds basic concepts of 'what to do'. this is where things get interesting. without getting too complex and going beyond minimalist approaches, the tougher, longer surviving, and harder to beat the robots can become, the better. 

# guide

## setup

in your utexas folder, have a venv python virtual environment. can create that with

    python -m venv venv

have your bash shell set to use your venv

    source venv/bin/activate

your bash prompt should now begin with (venv) showing it's active. within your venv, have pip installed pexpect and sshkeyboard

    pip install pexpect
    pip install sshkeyboard

## usage

with project utexas 'booted from disk' and running in a terminal, open other terminals and use the commands

    python robots/main.py [captain's name]
    bash robots/start-some-robots.sh &

to watch and shutdown

    tail -f log1
    pkill -2 -f python
    2 SIGINT     ctrlc
    20 SIGTSTP   ctrlz

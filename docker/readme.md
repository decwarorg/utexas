
we want project utexas to be a docker container

# build richard cornwll's simh pdp10-kl

https://github.com/rcornwell/sims get the contents of master branch into /docker/sims. can remove the folders other than pdp10.

    cd /docker/sims
    make pdp10-kl
    ls -l BIN/pdp10-kl

# build back10 for tape handling

this is used to create tapes for the dec10

    cd /docker/back10
    gcc back10.c -o back10
    ls -l back10


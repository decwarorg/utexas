FROM ubuntu:22.04
RUN apt-get update && apt-get install build-essential cmake telnet -y
RUN apt-get install python3 python3-dev python3-pip python3-setuptools -y
RUN pip install pexpect

# build Richard Cornwll's SIMH KL10 https://github.com/rcornwell/sims
ADD docker /docker
WORKDIR /docker/sims
RUN mkdir build
WORKDIR /docker/sims/build
RUN cmake ..
RUN make pdp10-kl # it's created as /docker/sims/BIN/pdp10-kl
RUN cp /docker/sims/BIN/pdp10-kl /docker/pdp10-kl

# build the BACK-10 tape tool for maniuplating tape
WORKDIR /docker
RUN gcc back10.c -o back10

ADD simh /docker/simh
# ADD msc /docker/msc # we now instead bind this in docker compose so it is live

# if necessary. best done manually, as in automation it currently hangs on the ending continue
# RUN ./pdp10-kl simh/create-boot-disk-from-tape.ini

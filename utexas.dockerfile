FROM ubuntu:24.04
RUN apt-get update && apt-get install build-essential cmake -y

# build richard cornwll's simh kl10 https://github.com/rcornwell/sims
ADD docker /docker
WORKDIR /docker/sims
RUN mkdir build
WORKDIR /docker/sims/build
RUN cmake ..
RUN make pdp10-kl # it's created as /docker/sims/BIN/pdp10-kl
RUN cp /docker/sims/BIN/pdp10-kl /docker/pdp10-kl

# if necessary create the dec10 boot disk
WORKDIR /docker
ADD simh /docker/simh
RUN ./pdp10-kl simh/create-boot-disk-from-tape-docker.ini 

# build back10 for tape handling
WORKDIR /docker/back10-src
RUN gcc back10.c -o back10
RUN cp /docker/back10-src/back10 /docker/back10

# prep utexas23 reconstruction tape file
WORKDIR /docker
ADD utexas23-reconstruction /docker/utexas23-reconstruction
ADD msc /docker/msc
RUN msc/create-tape-utexas23-reconstruction

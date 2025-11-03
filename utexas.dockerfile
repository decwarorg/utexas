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

# misc prep
WORKDIR /docker
RUN gcc back10.c -o back10

# if necessary create the dec10 boot disk
ADD simh /docker/simh
RUN ./pdp10-kl simh/docker-boot-disk.ini 

# prep utexas23 reconstruction tape file
ADD utexas23-reconstruction /docker/utexas23-reconstruction
ADD msc /docker/msc
RUN msc/create-tape-utexas23-reconstruction

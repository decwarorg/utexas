FROM ubuntu:24.04
RUN apt-get update && apt-get install build-essential cmake telnet -y

# build richard cornwll's simh kl10 https://github.com/rcornwell/sims
ADD docker /docker
WORKDIR /docker/sims
RUN mkdir build
WORKDIR /docker/sims/build
RUN cmake ..
RUN make pdp10-kl # it's created as /docker/sims/BIN/pdp10-kl
RUN cp /docker/sims/BIN/pdp10-kl /docker/pdp10-kl

WORKDIR /docker
RUN gcc back10.c -o back10

ADD simh /docker/simh
#RUN ./pdp10-kl simh/create-boot-disk-from-tape.ini # if necessary. and currently hangs on the ending continue

ADD msc /docker/msc
ADD utexas23-reconstruction /docker/utexas23-reconstruction
RUN msc/create-tape-utexas23-reconstruction

CMD ["./pdp10-kl", "./simh/boot-from-disk.ini"]

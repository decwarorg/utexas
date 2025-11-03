FROM ubuntu:24.04
RUN apt-get update && apt-get install build-essential -y

# build richard cornwll's simh kl10
ADD docker /docker
WORKDIR /docker/sims
RUN make pdp10-kl


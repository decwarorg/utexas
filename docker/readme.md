
# docker simh/create-boot-disk-from-tape.ini trouble

by having last line of ini file be 'exit' dockerfile can complete the disk creation but for some reason accounts such as decwar are not there. there's trouble. if that is a 'continue' line the disk is good but the dockerfile hangs. it's stuck inside the sim, where manually we'd do ctrl-e and q. workaround. for docker use premade dsk folder. unzip the dsk folder from dsk-20251103.zip and have it there as docker/dsk. docker copies it in and decwar is running in container. fixing this can be postponed since the dsk image is always the same. as long as were able to create dsk on raspi, we're fine.

# docker on raspi

new sd card with new raspbian debian trixie. following is apparently giving a working docker cli

    noah@raspberrypi:~ $ history
        1  sudo apt-get update
        2  curl -sSL https://get.docker.com | sh
        3  sudo usermod -aG docker $USER
        4  docker


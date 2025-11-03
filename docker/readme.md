
# docker simh/create-boot-disk-from-tape.ini trouble

by having

    ;continue
    exit

at the end, docker can complete the disk creation. but for some reason accounts such as decwar are not there. there's trouble.

workaround. unzip the dsk folder from dsk-20251103.zip and have it there as docker/dsk. docker copies it in and decwar is running in container. fixing this can be postponed since the dsk image is always the same. as long as were able to create dsk on raspi, we're fine.

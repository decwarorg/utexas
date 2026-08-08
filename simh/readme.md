
# docker simh/create-boot-disk-from-tape.ini trouble

by having last line of ini file be 'exit' dockerfile can complete the disk creation but for some reason accounts such as decwar are not there. there's trouble. if that is a 'continue' line the disk is good but the dockerfile hangs. it's stuck inside the sim, where manually we'd do ctrl-e and q. workaround. for docker use manually created dsk folder. unzip the dsk folder from dsk-20251103.zip and have it there as docker/dsk. docker copies it in and decwar is running in container. fixing this can be postponed since the dsk image is always the same. as long as we're able to manually create a new dsk folder at any time, we're fine. and in can case, we don't really want to auto create the dsk folder on every start because it's slow.


# useful passwords

these aren't really needed for decwar, but are useful lore, especially the common or even stadard ppn numbers.

- 1,2 FAILSA
- 6,6 MAINT
- 7,7 OPER
- 10,* DIST
- 100,100 DEMO1
- 100,101 DEMO2
- 5,30 DECWAR

you can also just look in the [tape-boot-create-disk.ini](tape-boot-create-disk.ini) simh script that creates our boot disk, these passwords are set right there! the above is just a nice presentation of those facts on the ground.

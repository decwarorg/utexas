# Getting Started

Have Git, Python, and Docker Desktop installed on your system. Git clone the [utexas project](https://github.com/decwarorg/utexas) to your system. You can start the utexas-10 container with start.py and then use another session to telnet in.

    utexas % python3 start.py
    telnet localhost 2030

The folder msc/vt52 contains [aap's](https://github.com/aap/vt05) fun and relatively simple terminal emulator. If you have the vt52 exe built for your system, then you can do something like this to connect to your utexas-10 container old-school style.

    msc/vt52 % ./vt52 telnet localhost 2030

Your telnet session will be connected to the DEC-10. You may need to hit return to get its attention.

    Trying ::1...
    Connected to localhost.
    Escape character is '^]'.
    Connected to the KL-10 simulator TTY device, line 0
    KL703 00:00:30 TTY4 system 1025
    Connected to Node KL10(1) Line # 4
    Please LOGIN or ATTACH

Go ahead and login as decwar, no password needed. Once logged in, you can always run the game with r gam:decwar, but we'll be headed beyond that in the following.

    .login decwar
    Job 2  KL703  TTY4
    [LGNJSP Other jobs same PPN:3]
    00:00   19-Mar-86   Wednesday
    .dir
    DECWAR	FOR   262  <057>   19-Mar-86	DSKB:	[5,30]
    DECWAR	GRP     0  <000>   19-Mar-86
    DECWAR	HLP    85  <055>   19-Mar-86
    ...snip...
    .r gam:decwar

We're experimenting with Singer’s 1978 “Introduction to DECsystem-10 Assembler Language Programming”. Here's the [pdf within the project](msc/docs/dec10-assembler-singer.pdf). On page 4, using teco to create a test file. Note that $ is the TOPS-10 echo for the escape key. Where you see $, hit escape.

    .make test
    *ihello world$ex$$
    .type test

# Project UTEXAS

- [going backwards](#going-backwards)
- [guide](#guide)
- [folder structure](#folder-structure)

for a nutshell history, please see the [history readme](https://github.com/decwarorg/history) and for push button installation and usage please see the [merely-players readme](https://github.com/decwarorg/merely-players). the person to acknowledge up front is merlyn cousins, as noted in the history readme. working alone, around 2011, merlyn took the source code that had been modified to run on compuserve's pdp-10s and got it to run on standard tops-10, standard pdp-10. we have merlyn to thank for making the source code fully usable. here's a link to [merlyn's github repo](https://github.com/drforbin/decwar) where that all took place.

# going backwards

project utexas is about reconstruction of the primordial utexas tape and effectively going backwards in time. if an original tape or a copy of the original code is discovered, it will hopefully match closely with the utexas reconstruction.

meanwhile, it's a living time capsule of fifty year old hardware and software, completely open for explorations and experiments. it's a big, many layered, complex system, but given time and user feedback can hopefully converge towards modern standards of friendliness and usability.

hardware. the hardware aspects are thanks to richard cornwell, and a useful entrypoint is rich's [pdp10 hardware repo](https://github.com/rcornwell/pidp10), and more broadly rich's [main hardware repo](https://github.com/rcornwell/sims). rich is a member of the [opensimh steering group](https://opensimh.org/about/). project utexas hardware can be a complex topic, as there were multiple generations of dec10 (ka, ki, kl, ks) and a zoo of attached devices. in a nutshell, it's useful to gradually become familiar with the hardware aspects of utexas. for digital systems, fifty years mean nothing, and at least in a digital sense the hardware is very 'real' and 'physical'.

software. tops10, fortran iv, and other necessary low-level system code comes as binary tape images via rich's [personal website](https://sky-visions.com/dec/tops10.shtml). the way to learn about using these is by example and experimentation. getting familiar with the system tapes is a first step to being able to modify the creation and usage of the project utexas tape 'tapes/utexas.tap'. with that capability in hand, the next step is to be able to use the utexas tape to on-the-fly compile, link, and install decwar itself. improving that know-how is reflected in improvements to the simh script [utexas.do](simh/utexas.do). 

to have on the radar. project utexas relates with the higher-level [pidp10 project](https://obsolescence.dev/pdp10). utexas was directly triggered and inspired by the release of the pidp10 in the summer of 2024. all of the work and good spirit of oscar, lars, and rich are further inspiration. ideally utexas can be fully integrated within the pidp10 'ecosystem'. there are good questions to tackle here, especially around interactions between ka and kl simh exes, and also the [pdpcontrol](https://github.com/rcornwell/pidp10/blob/master/bin/pdpcontrol.sh) bash script associated with the pidp10 package. these are simply question marks to keep on the radar and learn about along the way. one thing to keep in mind is that decwar requires fortran iv/66, an earlier fortran than the fortran10/v/77 commonly encountered these days. it's possible that fortran iv integration will play a major role in the future of utexas within the pidp10 context.
 
# guide

there used to be a series of steps here for preparing and running on a raspi, especially for driving the lights of a front panel if one is present. all of that is being obsoleted now by docker compose. we're only assuming that python and docker engine are present. that's true if docker desktop is installed. docker engine can also be present as a headless service, which is especially common on linux and necessary on raspi. for python and docker, [decwar/merely-players install.py](https://github.com/decwarorg/merely-players/-/blob/main/readme.md) has complete 'push button' instructions.

# folder structure

- [project utexas log](project-utexas-log.md)
- msc, miscellaneous shell scripts and related code
  - [create tape utexas23 reconstruction](msc/create-tape-utexas23-reconstruction)
  - [create archive project utexas](msc/create-archive-project-utexas)
- simh, simh scripts
  - [utexas do](simh/utexas.do)
  - [boot from disk](simh/boot-from-disk.ini)
  - [create boot disk from tape](simh/create-boot-disk-from-tape.ini)
- [staging](staging/)
- utexas23-reconstruction, [primordial utexas tape reconstruction](utexas23-reconstruction/DECWAR.TAP)
  - hlp folder, [hlp.com](utexas23-reconstruction/hlp/HLP.COM) comment file. note [decwar.imp](utexas23-reconstruction/hlp/DECWAR.IMP) important file, and the 1982 letter from utexas to compuserve, included on the primordial decwar tape as [decwar.ltr](utexas23-reconstruction/hlp/DECWAR.LTR)
  - msc folder, [msc.com](utexas23-reconstruction/msc/MSC.COM) comment file.
  - tec folder, for [teco scripts](docs/sec9-utexas-primordial-tape.md/#teco-scripts) to autogen fortran include files

# Project UTEXAS DECWAR

- utexas23-reconstruction, [UTEXAS DECWAR 2.3 Source Distribution Tape Reconstruction](utexas23-reconstruction/DECWAR.TAP)
  - HLP folder, [HLP.COM](utexas23-reconstruction/hlp/HLP.COM) comment file, [DECWAR.IMP](utexas23-reconstruction/hlp/DECWAR.IMP) important file, and the 1982 letter from UTEXAS to Compuserve, included on the Decwar SDT as [DECWAR.LTR](utexas23-reconstruction/hlp/DECWAR.LTR).
  - MSC folder, [MSC.COM](utexas23-reconstruction/msc/MSC.COM) comment file.
  - TEC folder, for [TECO-124 code](docs/sec9-utexas-primordial-tape.md/#teco-scripts) to auto-generate Fortran include files. TECO-124 is Clive Dawson's UT version adding screen editing to the standard DEC TECO-24.
- [staging](staging/), Questionable files that potentially may be brought into the reconstruction. Were they on the original SDT?
- msc, Miscellaneous shell scripts, tools, and related code.
  - [create tape utexas23 reconstruction](msc/create-tape-utexas23-reconstruction)
  - to-tape, These file are auto included in the tape as extras.
  - vt52 folder, Fun vt52 emulator.
- simh, SIMH scripts.
  - [utexas do](simh/utexas.do)
  - [boot from disk](simh/boot-from-disk.ini)
  - [create boot disk from tape](simh/create-boot-disk-from-tape.ini)
- docs folder, Docs focused on UT HRC DEC-10 topics.
- docker, Matters specific to the project's Docker Container and the complete environment inside that.

# Getting Started

Have Git, Python, and Docker Desktop installed on your system. Git clone the [utexas project](https://github.com/decwarorg/utexas) to your system. You can start the utexas-10 container with start.py and then use another session to telnet into the DEC-10.

    utexas % python3 start.py
    telnet localhost 2030

The folder msc/vt52 contains [aap's](https://github.com/aap/vt05) fun and relatively simple terminal emulator. If you have the vt52 exe built for your system, then you can do something like this to telnet into the DEC-10.

    msc/vt52 % ./vt52 telnet localhost 2030

Your telnet session will be connected to the DEC-10.

    Trying ::1...
    Connected to localhost.
    Escape character is '^]'.
    Connected to the KL-10 simulator TTY device, line 0
    KL703 00:00:30 TTY4 system 1025
    Connected to Node KL10(1) Line # 4
    Please LOGIN or ATTACH

Go ahead and login as decwar, no password needed. Once logged in, you can always run the game with r gam:decwar.

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

We're experimenting with Singer’s 1978 “Introduction to DECsystem-10 Assembler Language Programming”. Here's the [pdf within the project](docs/dec10-assembler-singer.pdf). Page 4, using teco to create a test file. Note that $ is the TOPS-10 echo for the escape key. Where you see \$, hit escape.

    .make test
    *ihello world$ex$$
    .type test

# Tape

Flow extra files in via the tape by putting them in msc/to-tape. Then in the container, recreate the tape.

    root@1ee085ff605a:/docker# ./msc/create-tape-utexas23-reconstruction

And in TOPS-10 use backup to restore.

    .r backup
    /tape mta0:
    /rewind
    /inter
    /files
    /rest [,]*.*=*.*
    ...snip...
    /exit
    .

# Project UTEXAS DECWAR

- [UTEXAS DECWAR 2.3 Source Distribution Tape Reconstruction](utexas23-reconstruction)
  - [DECWAR.TAP](utexas23-reconstruction/DECWAR.TAP) - Source Distribution Tape Contents Listing
  - [HLP](utexas23-reconstruction/HLP) - Comment File [HLP.COM](utexas23-reconstruction/HLP/HLP.COM), Important File [DECWAR.IMP](utexas23-reconstruction/HLP/DECWAR.IMP), and the 1982 letter from UTEXAS to Compuserve included on the Decwar SDT as [DECWAR.LTR](utexas23-reconstruction/HLP/DECWAR.LTR).
  - [MSC](utexas23-reconstruction/MSC) - Comment File [MSC.COM](utexas23-reconstruction/MSC/MSC.COM).
  - [TEC](utexas23-reconstruction/TEC) - TECO-124 code to auto-generate Fortran include files from MACRO-10 assembly code. TECO-124 is Clive Dawson's UT version adding screen editing to the standard DEC TECO-24.
- [staging](staging/) - Questionable files that potentially may be brought into the SDT Reconstruction. Were they on the original UTEXAS SDT?
- [msc](msc) - Miscellaneous shell scripts, tools, and related code.
  - [msc/create-tape-utexas23-reconstruction](msc/create-tape-utexas23-reconstruction)
  - [msc/to-tape](msc/to-tape) - These file are auto included in the tape as extras.
  - [msc/vt52](msc/vt52) - Fun VT52 emulator.
- [simh](simh) - SIMH scripts.
  - [simh/utexas.do](simh/utexas.do)
  - [simh/boot-from-disk.ini](simh/boot-from-disk.ini)
  - [simh/create-boot-disk-from-tape.ini](simh/create-boot-disk-from-tape.ini)
- [docs](docs) - Docs focused on UT HRC DEC-10 topics.
- [docker](docker) - Matters specific to the project's Docker Container and the complete environment inside that.

# Getting Started

Have Git, Python, Docker Desktop, and a clone of this repo on your system. Start the utexas-10 container with start.py. Every time that the container starts, the Decwar source code is restored from the SDT, compiled, linked, and installed. You can also do all of this manually at any time. The source code is completely alive, active, and in-the-loop. 

    utexas % python3 start.py

Telnet into the DEC-10 from another session. The folder msc/vt52 contains [aap's](https://github.com/aap/vt05) fun and relatively simple terminal emulator. If you have the VT52 exe built for your system you can telnet from it.

    telnet localhost 2030
    msc/vt52 % ./vt52 telnet localhost 2030

Telnet will connect to the DEC-10.

    Trying ::1...
    Connected to localhost.
    Escape character is '^]'.
    Connected to the KL-10 simulator TTY device, line 0
    KL703 00:00:30 TTY4 system 1025
    Connected to Node KL10(1) Line # 4
    Please LOGIN or ATTACH

Login as decwar, no password needed, and run the game with r gam:decwar.

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

In the following, hit the escape key for each $ symbol.

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

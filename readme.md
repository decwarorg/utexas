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

We're experimenting with Singer’s 1978 “Introduction to DECsystem-10 Assembler Language Programming”. Here's the [pdf within the project](msc/docs/dec10-assembler-singer.pdf). Page 4, using teco to create a test file. Note that $ is the TOPS-10 echo for the escape key. Where you see \$, hit escape.

    .make test
    *ihello world$ex$$
    .type test

# Project UTEXAS

- utexas23-reconstruction, [UTEXAS Source Distribution Tape reconstruction](utexas23-reconstruction/DECWAR.TAP)
  - hlp folder, [hlp.com](utexas23-reconstruction/hlp/HLP.COM) comment file. Note [decwar.imp](utexas23-reconstruction/hlp/DECWAR.IMP) important file. And the 1982 letter from UTEXAS to Compuserve, included on the Decwar SDT as [decwar.ltr](utexas23-reconstruction/hlp/DECWAR.LTR).
  - msc folder, [msc.com](utexas23-reconstruction/msc/MSC.COM) comment file.
  - tec folder, for [TECO-124 scripts](docs/sec9-utexas-primordial-tape.md/#teco-scripts) to auto-generate Fortran include files. TECO-124 is Clive Dawson's UT version adding screen editing to the standard DEC TECO-24.
- [staging](staging/), questionable files that potentially could be brought into the reconstruction. Were they on the original SDT?
- msc, miscellaneous shell scripts and related code
  - [create tape utexas23 reconstruction](msc/create-tape-utexas23-reconstruction)
  - docs folder, docs focused on the UT HRC DEC-10.
  - vt52 folder, fun vt52 emulator.
- simh, simh scripts
  - [utexas do](simh/utexas.do)
  - [boot from disk](simh/boot-from-disk.ini)
  - [create boot disk from tape](simh/create-boot-disk-from-tape.ini)
- docker, matters specific to the project's Docker Container and the complete environment inside that.
- [project utexas log](project-utexas-log.md)

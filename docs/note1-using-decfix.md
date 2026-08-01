decfix.mac can be used to manage the high segment. to run it use

    .exec decfix

if decwar is in the high segment

    .sys
    ...snip...
    High Segments:
    Program	Device	Owner	High(P)	Users
    INITIA	DSKB	[SYS]	 8 	1
    GLXLIB	DSKB	[SYS]	39 	7
    DECWAR	DSKB     5,30	56 	1
    ...snip...

it is renamed, effectively clearing it. this should leave the system in a clean state.

    .exec decfix
    .sys
    ...snip...
    High Segments:
    Program	Device	Owner	High(P)	Users
    INITIA	DSKB	[SYS]	 8 	1
    GLXLIB	DSKB	[SYS]	39 	7
    (OBS)	DSKB	[SELF]	56 	1
    ...snip...

# notes

newly booted

    Status of KL703 at  0:00:59 on 19-Mar-86
    Uptime 59, 98% Null time = 97% Idle + 1% Lost, 1% Overhead
    13 Jobs in use out of 128.  13 logged in, 10 detached.
    Job    Who     Line#	What   Size(P)	State	Run Time
     1    [OPR]	DET	STOMPR	9+8	SL	       0 01
     2    [OPR]	CTY	 	4	^C	       0
     3    [SELF]	 4	SYSTAT	22+SPY	RN	       0 $
     4    [OPR]	DET	ACTDAE	183+39	SL	       0
     5    [OPR]	DET	DAEMON	20+SPY	SL	       0
     6    [OPR]	DET	FILDAE	17	HB	       0
     7    [OPR]	DET	QUASAR	109+39	SL	       0
     8    [OPR]	DET	PULSAR	65+39	HB	       0
     9    [OPR]	DET	CATLOG	30+39	HB	       0
    10    [OPR]	DET	ORION	93+39	SL	       0
    11    [OPR]	DET	BATCON	38+39	SL	       0
    12    [OPR]	DET	LPTSPL	74+39	HB	       0
    13    [OPR]	105	 	4	^C	       0
    $ means Execute Only	n means job runs in HPQ n
    High Segments:
    Program	Device	Owner	High(P)	Users
    INITIA	DSKB	[SYS]	 8 	1
    GLXLIB	DSKB	[SYS]	39 	7
    Swapping space used = 675/8192 = 8%
    Virt. Core used = 715/8192 = 9%
    6848P Core left
    Active swapping ratio = 22/7563 = .00
    Virt. Core saved by sharing = 234/(234+715) = 25%
    Average job size =668/13 = 51.3P+281/13 = 21.6P  Total=949/13 = 73.0P
    Busy devices:
    Device	Job	Why	Logical
    LPT010	12	init
    System File Structures:
    Name	Free	Mount
    DSKB	427420	3
    Total Free 427420

one player

    Status of KL703 at  0:02:42 on 19-Mar-86
    Uptime 2:42, 113% Null time = 113% Idle + 0% Lost, 0% Overhead
    14 Jobs in use out of 128.  13 logged in, 10 detached.
    Job    Who     Line#	What   Size(P)	State	Run Time
     1    [OPR]	DET	STOMPR	9+8	SL	       0 01
     2    [OPR]	CTY	 	4	^C	       0
     3     5,30	 4	DECWAR	14+56	SL	       0 #
     4    [OPR]	DET	ACTDAE	183+39	SL	       0
     5    [OPR]	DET	DAEMON	20+SPY	SL	       0
     6    [OPR]	DET	FILDAE	17	HB	       0
     7    [OPR]	DET	QUASAR	109+39	SL	       0
     8    [OPR]	DET	PULSAR	65+39	HB	       0
     9    [OPR]	DET	CATLOG	30+39	HB	       0
    10    [OPR]	DET	ORION	93+39	SL	       0
    11    [OPR]	DET	BATCON	38+39	SL	       0
    12    [OPR]	DET	LPTSPL	74+39	HB	       0
    13    [OPR]	105	 	4	^C	       0
    14     2,5	 5	SYSTAT	22+SPY	RN	       0 $
    # means non-system Hi-Seg
    $ means Execute Only	n means job runs in HPQ n
    High Segments:
    Program	Device	Owner	High(P)	Users
    INITIA	DSKB	[SYS]	 8 	1
    GLXLIB	DSKB	[SYS]	39 	7
    DECWAR	DSKB     5,30	56 	1
    Swapping space used = 742/8192 = 9%
    Virt. Core used = 785/8192 = 10%
    6778P Core left
    Active swapping ratio = 22/7563 = .00
    Virt. Core saved by sharing = 234/(234+785) = 23%
    Average job size =682/14 = 48.7P+337/14 = 24.0P  Total=1019/14 = 72.7P
    Busy devices:
    Device	Job	Why	Logical
    LPT010	12	init
    System File Structures:
    Name	Free	Mount
    DSKB	427420	3
    Total Free 427420

after 'ex decfix'

    Status of KL703 at  0:04:16 on 19-Mar-86
    Uptime 4:16, 116% Null time = 116% Idle + 0% Lost, 0% Overhead
    14 Jobs in use out of 128.  14 logged in, 10 detached.
    Job    Who     Line#	What   Size(P)	State	Run Time
     1    [OPR]	DET	STOMPR	9+8	SL	       0 01
     2    [OPR]	CTY	 	4	^C	       0
     3    [SELF]	 4	DECWAR	14+56	SL	       0 @
     4    [OPR]	DET	ACTDAE	183+39	SL	       0
     5    [OPR]	DET	DAEMON	20+SPY	SL	       0
     6    [OPR]	DET	FILDAE	17	HB	       0
     7    [OPR]	DET	QUASAR	109+39	SL	       0
     8    [OPR]	DET	PULSAR	65+39	HB	       0
     9    [OPR]	DET	CATLOG	30+39	HB	       0
    10    [OPR]	DET	ORION	93+39	SL	       0
    11    [OPR]	DET	BATCON	38+39	SL	       0
    12    [OPR]	DET	LPTSPL	74+39	HB	       0
    13    [OPR]	105	 	4	^C	       0
    14    [SELF]	 5	SYSTAT	22+SPY	RN	       0 $
    @ means superseded Hi-Seg	
    $ means Execute Only	n means job runs in HPQ n
    High Segments:
    Program	Device	Owner	High(P)	Users
    INITIA	DSKB	[SYS]	 8 	1
    GLXLIB	DSKB	[SYS]	39 	7
    (OBS)	DSKB	[SELF]	56 	1
    Swapping space used = 742/8192 = 9%
    Virt. Core used = 785/8192 = 10%
    6778P Core left
    Active swapping ratio = 22/7563 = .00
    Virt. Core saved by sharing = 234/(234+785) = 23%
    Average job size =682/14 = 48.7P+337/14 = 24.0P  Total=1019/14 = 72.7P
    Busy devices:
    Device	Job	Why	Logical
    LPT010	12	init
    System File Structures:
    Name	Free	Mount
    DSKB	427410	4
    Total Free 427410

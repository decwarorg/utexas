# project utexas

- [going backwards](#going-backwards)
- [guide](#guide)
- [folder structure](#folder-structure)

for a nutshell history, please see the [decwar/history readme](https://gitlab.com/decwar/history) and for push button installation and usage please see the [decwar/merely-players readme](https://gitlab.com/decwar/merely-players)

# going backwards

project utexas is about reconstruction of the primordial utexas tape and effectively going backwards in time. if an original tape or a copy of the original code is discovered, it will hopefully match closely with the utexas reconstruction.

meanwhile, it's a living time capsule of fifty year old hardware and software, completely open for explorations and experiments. it's a big, many layered, complex system, but given time and user feedback can hopefully converge towards modern standards of friendliness and usability.

hardware. the hardware aspects are thanks to richard cornwell, and a useful entrypoint is rich's [pdp10 hardware repo](https://github.com/rcornwell/pidp10), and more broadly rich's [main hardware repo](https://github.com/rcornwell/sims). rich is a member of the [opensimh steering group](https://opensimh.org/about/). project utexas hardware can be a complex topic, as there were multiple generations of dec10 (ka, ki, kl, ks) and a zoo of attached devices. in a nutshell, it's useful to gradually become familiar with the hardware aspects of utexas. for digital systems, fifty years mean nothing, and at least in a digital sense the hardware is very 'real' and 'physical'.

software. tops10, fortran iv, and other necessary low-level system code comes as binary tape images via rich's [personal website](https://sky-visions.com/dec/tops10.shtml). the way to learn about using these is by example and experimentation. getting familiar with the system tapes is a first step to being able to modify the creation and usage of the project utexas tape 'tapes/utexas.tap'. with that capability in hand, the next step is to be able to use the utexas tape to on-the-fly compile, link, and install decwar itself. improving that know-how is reflected in improvements to the simh script [utexas.do](simh/utexas.do). 

to have on the radar. project utexas relates with the higher-level [pidp10 project](https://obsolescence.dev/pdp10). utexas was directly triggered and inspired by the release of the pidp10 in the summer of 2024. all of the work and good spirit of oscar, lars, and rich are further inspiration. ideally utexas can be fully integrated within the pidp10 'ecosystem'. there are good questions to tackle here, especially around interactions between ka and kl simh exes, and also the [pdpcontrol](https://github.com/rcornwell/pidp10/blob/master/bin/pdpcontrol.sh) bash script associated with the pidp10 package. these are simply question marks to keep on the radar and learn about along the way. one thing to keep in mind is that decwar requires fortran iv/66, an earlier fortran than the fortran10/v/77 commonly encountered these days. it's possible that fortran iv integration will play a major role in the future of utexas within the pidp10 context.
 
# guide

there used to be a series of steps here for preparing and running on a raspi, especially for driving the lights of a front panel if one is present. all of that is being obsoleted now by docker compose. we're only assuming that python and docker engine are present. that's true if docker desktop is installed. docker engine can also be present as a headless service, which is especially common on linux and necessary on raspi. for python and docker, [decwar/merely-players install.py](https://gitlab.com/decwar/merely-players/-/blob/main/readme.md) has complete 'push button' instructions.

# folder structure

- [project utexas log](project-utexas-log.md)
- msc, miscellaneous shell scripts and related code
  - [create tape utexas23 reconstruction](msc/create-tape-utexas23-reconstruction)
  - [create archive project utexas](msc/create-archive-project-utexas)
- simh, simh scripts
  - [utexas do](simh/utexas.do)
  - [boot from disk](simh/boot-from-disk.ini)
  - [create boot disk from tape](simh/create-boot-disk-from-tape.ini)
- [staging](staging/readme.md)
- utexas23-reconstruction, [primordial utexas tape reconstruction](utexas23-reconstruction/DECWAR.TAP)
  - hlp folder, [hlp.com](utexas23-reconstruction/hlp/HLP.COM) comment file. note [decwar.imp](utexas23-reconstruction/hlp/DECWAR.IMP) important file, and the 1982 letter from utexas to compuserve, included on the primordial decwar tape as [decwar.ltr](utexas23-reconstruction/hlp/DECWAR.LTR)
  - msc folder, [msc.com](utexas23-reconstruction/msc/MSC.COM) comment file.
  - tec folder, for [teco scripts](docs/sec9-utexas-primordial-tape.md/#teco-scripts) to autogen fortran include files

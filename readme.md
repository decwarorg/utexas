# project utexas

- [going backwards](#going-backwards)
- [guide](#guide)
- [folder structure](#folder-structure)

nutshell history

- 1971, [original single player star trek](https://en.wikipedia.org/wiki/Star_Trek_(1971_video_game)), written in basic for ucal irvine sds sigma 7, mike mayfield. in 1971, mike mayfield, then in his final year of high school, frequented a computer lab at the university of california, irvine, while teaching himself how to program. the lab operated both a sds sigma 7 and a dec pdp10. the pdp10 hosted a version of the 1962 pdp1 spacewar. mayfield had gained illicit access to the sigma 7 at the lab and wanted to create his own version of the game for the system. spacewar required a vector graphics display, however, and the sigma 7 only had access to a non-graphical teletype model 33.
- 1972, rewrite of original, basic for hp 2000c at hp office near ucal irvine, mike mayfield
- 1973, ut trek, written in basic, grady hicks and jim korp at utexas
- 1974, ut fortran, aka [super star trek](https://gitlab.com/esr/super-star-trek), single player fortran on utexas cdc 6600, dave matuszek and paul reynolds
- mid 70s, war, fortran two player version written for utexas cdc 6600, author unknown, rewritten by robert schneider
- 1978, [decwar](https://en.wikipedia.org/wiki/Decwar#Original_versions), assembly and fortran, eighteen player version written for utexas pdp10, bob hysick and jeff potter. version 1.0 of decwar was released in august 1978. the university would make copies available on tape for the nominal fee of $50, and it soon appeared on pdp10s around the world. the greatly updated 2.0 was released in july 1979, and another major version, 2.3, on 20 november 1981.

[utexas center for american history](https://briscoecenter.org/) catalog item [v2.2](https://repositories.lib.utexas.edu/items/1aa48343-09ab-4b3b-a9f2-e2e525074a4d) has files migrated from a decus magnetic tape, including a somewhat doubtful patched executable, but no source code. here's the instructions a utexas player saw [june 3, 1980 v2.2 utexas](hlp/DECWAR22.HLP). utexas decwar had eighteen playable ships. this is also definitely what players at the southwest texas state university computation center, san marcos texas, saw circa 1983 and 1984.

[utexas center for american history](https://briscoecenter.org/) catalog item [v2.3](https://repositories.lib.utexas.edu/items/7e2ccf50-e814-4bce-91d2-a7f6440eabe4) is source code ported circa 2011 by merlyn cousins from the compuserve decwar 2.3 source code to simh pdp10. harris newman received this code around 1995, as discussed elsewhere in this repo. it started as an original utexas 2.3 tape and had been modified by compuserve circa 1981 for commercial purposes. here's the instructions a compuserve player saw [november 20, 1981 v2.3 compuserve](hlp/DECWAR23CIS.HLP). compuserve decwar had ten playable ships.

# going backwards

project utexas is about reconstruction of the primordial utexas tape and effectively going backwards in time. if an original tape or a copy of the original code is discovered, it will hopefully match closely with the utexas reconstruction.

meanwhile, it's a living time capsule of fifty year old hardware and software, completely open for explorations and experiments. it's a big, many layered, complex system, but given time and user feedback can hopefully converge towards modern standards of friendliness and usability.

hardware. the hardware aspects are thanks to richard cornwell, and a useful entrypoint is rich's [pdp10 hardware repo](https://github.com/rcornwell/pidp10), and more broadly rich's [main hardware repo](https://github.com/rcornwell/sims). rich is a member of the [opensimh steering group](https://opensimh.org/about/). project utexas hardware can be a complex topic, as there were multiple generations of dec10 (ka, ki, kl, ks) and a zoo of attached devices. in a nutshell, it's useful to gradually become familiar with the hardware aspects of utexas. for digital systems, fifty years mean nothing, and at least in a digital sense the hardware is very 'real' and 'physical'.

software. tops10, fortran iv, and other necessary low-level system code comes as binary tape images via rich's [personal website](https://sky-visions.com/dec/tops10.shtml). the way to learn about using these is by example and experimentation. getting familiar with the system tapes is a first step to being able to modify the creation and usage of the project utexas tape 'tapes/utexas.tap'. with that capability in hand, the next step is to be able to use the utexas tape to on-the-fly compile, link, and install decwar itself. improving that know-how is reflected in improvements to the simh script [utexas.do](https://github.com/drforbin/decwar/blob/master/utexas/simh/utexas.do). 

to have on the radar. project utexas relates with the higher-level [pidp10 project](https://obsolescence.dev/pdp10). utexas was directly triggered and inspired by the release of the pidp10 in the summer of 2024. all of the work and good spirit of oscar, lars, and rich are further inspiration. ideally utexas can be fully integrated within the pidp10 'ecosystem'. there are good questions to tackle here, especially around interactions between ka and kl simh exes, and also the [pdpcontrol](https://github.com/rcornwell/pidp10/blob/master/bin/pdpcontrol.sh) bash script associated with the pidp10 package. these are simply question marks to keep on the radar and learn about along the way. one thing to keep in mind is that decwar requires fortran iv/66, an earlier fortran than the fortran10/v/77 commonly encountered these days. it's possible that fortran iv integration will play a major role in the future of utexas within the pidp10 context.
 
# guide

there used to be a series of steps for preparing and running on a raspi, especially for driving the lights of a front panel if one is present. all of that is being obsoleted now by docker compose. 

we're only assuming that python and docker engine are present. that's true if docker desktop is installed. docker engine can also be present as a headless service. this is especially common on linux.

with python and docker, [install.py](install.py) takes care of everything. it contains it's own simple instructions.

# folder structure

- top level
  - [install.py](install.py)
  - [utexas log](project-utexas-log.md/#project-utexas-log)
  - [utexas v2.2 player guide](hlp/DECWAR22.HLP)
  - [compuserve v2.3 player guide](hlp/DECWAR23CIS.HLP)
- msc, miscellaneous shell scripts and related code
  - [create tape utexas23 reconstruction](msc/create-tape-utexas23-reconstruction)
  - [create archive project utexas](msc/create-archive-project-utexas)
- simh, simh scripts
  - [utexas do](simh/utexas.do)
  - [boot from disk](simh/boot-from-disk.ini)
  - [create boot disk from tape](simh/create-boot-disk-from-tape.ini)
- utexas23-reconstruction, [primordial utexas tape reconstruction](docs/sec9-utexas-primordial-tape.md)
  - hlp folder, [hlp.com](utexas23-reconstruction/hlp/HLP.COM) comment file. note [decwar.imp](utexas23-reconstruction/hlp/DECWAR.IMP) important file, and the 1982 letter from utexas to compuserve, included on the primordial decwar tape as [decwar.ltr](utexas23-reconstruction/hlp/DECWAR.LTR)
  - msc folder, [msc.com](utexas23-reconstruction/msc/MSC.COM) comment file.
  - tec folder, for [teco scripts](docs/sec9-utexas-primordial-tape.md/#teco-scripts) to autogen fortran include files

# versions

- v1.0 20251109

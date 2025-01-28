# Ahri Announcer Script

Utilizes PowerShell and Python to automate the Star Guardian Ahri League of Legends announcer mod.
Please feel free to fork this project, to use with other announcers (or mods!)

## Video Tutorial
[https://www.youtube.com/watch?v=rT_sWqCz2uQ](https://www.youtube.com/watch?v=rT_sWqCz2uQ)

## Pre-Requisites
- `cslol-tools` which is downloaded along with [cslol-manager](https://github.com/LeagueToolkit/cslol-manager).
- `ritobin` which can be downloaded from [https://github.com/moonshadow565/ritobin](https://github.com/moonshadow565/ritobin). 
- `Python` - Scripts were made with Python 3.11.5. Requires Python to be in your PATH, so that python can be run from PowerShell.
- `cdtb` which can be downloaded using `pip3 install cdtb` - Source at [https://github.com/CommunityDragon/CDTB](https://github.com/CommunityDragon/CDTB)
- The script expects League to be installed in the default Windows location (`C:\Riot Games\League of Legends\`). If your League is installed somewhere else, you will need to change lines 42-45 to reference your install location.

## Setup
Folder Structure should look like this in order for the script to work properly:

```
.
├── cs-lol/
│   ├── hashes.game.txt
│   ├── wad-extract.exe
│   ├── wad-make.exe
│   └── other tools....
├── ritobin/
│   └── bin/
│       ├── hashes/
│       │   ├── hashes.binentries.txt
│       │   └── other hash files...
│       ├── ritobin_cli.exe
│       └── ritobin_gui.exe
├── scripts/
│   ├── AnnouncerFix.py
│   ├── fixAhri_globals_S15.py
│   ├── fixAhri_Maps_S15.py
│   └── info_maker.py
└── AhriAnnouncerBuilder.ps1
```

#  This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# AnnouncerFix Python Script - Copyright (C) 2025 buzzyjessibee
#                      __
#                     // \
#                     \\_/ //
#   ''-.._.-''-.._.. -(||)(')
#                     '''
#

# Correct as of 15.2
# Special Thanks to Leischii, Slime, and SirDexal

import re
import argparse

def modify_soundkey(text, pykeFlag):
    oddOnes = ['_Ace', '_PlayerDisconnectYourTeam', '_FirstBlood']
    veryOddOnes = ['_TurretPlatingFall30Seconds']
    mapThings = ['_StartGameMessage2Map', '_StartGameMessage1Map']
    inhibRespawn = ['_InhibitorRespawn']
    shutDown = ['_Shutdown']
    turretDie = ['_TurretLostFirstBlood']

    # Define the regex pattern
    pattern = r'("Play_vo_Announcer_)(@voice@)(_[a-zA-Z0-3]+)(.*)'

    # Need a match object to take into account the odd events
    match = re.search(pattern, text)
    
    # Define the replacement string
    replacement = r'\1Global_\2_@event name@\4'
    replacement_odd = r'\1Global_\2_@event name@"'
    replacement_very_odd = r'\1Global_\2\3"'
    replacement_mapThings = r'\1Global_\2_@event name@Map\4'
    replacement_shutDown = r'\1Global_\2_OnKilledUnitOnKillingSpree"'
    replacement_turret = r'\1Global_\2_OnTurretDie\4'
    replacement_fuckriot = r'\1Global_\2\3\4'

    # Pyke Things
    pyke_map1_replacement = r'\1Global_\2_OnStartGameMessage2"'
    pyke_map2_replacement = r'\1Global_\2_OnStartGameMessage2ButchersBridge"'

    # Get the string of group 3 (event name)
    eventString = match.group(3)
    
    # Perform the replacement
    if eventString in oddOnes:
        #print('Odd Event!')
        modified_text = re.sub(pattern, replacement_odd, text)
    elif eventString in shutDown:
        #print('Renamed shutDown!')
        modified_text = re.sub(pattern, replacement_shutDown, text)
    elif eventString in turretDie:
        #print('Renamed Event!')
        modified_text = re.sub(pattern, replacement_turret, text)
    elif eventString in inhibRespawn:
        #print('finna kill riot!')
        modified_text = re.sub(pattern, replacement_fuckriot, text)
    elif eventString in veryOddOnes:
        #print('Very Odd Event!')
        modified_text = re.sub(pattern, replacement_very_odd, text)
    elif eventString in mapThings:
        #print('Map Event!')
        if pykeFlag:
            if eventString == '_StartGameMessage1Map':
                modified_text = re.sub(pattern, pyke_map2_replacement, text)
            else:
                modified_text = re.sub(pattern, pyke_map1_replacement, text)
        else:
            modified_text = re.sub(pattern, replacement_mapThings, text)

    else:
        #print('Normal Event!')
        modified_text = re.sub(pattern, replacement, text)
    
    return modified_text

# Function to modify the file
def modify_file(input_file, pykeFlag):
    pattern = r'("Play_vo_Announcer_)(@voice@)(_[a-zA-Z0-3]+)(.*)'

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    for i, line in enumerate(lines):
        match = re.search(pattern, line)

        if match: # Modify the line if it matches the pattern
            lines[i] = modify_soundkey(line, pykeFlag)
        else: # Leave the line unchanged if it doesn't match
            lines[i] = line

    # Overwrite the original file with the modified content
    with open(input_file, 'w') as outfile:
        outfile.writelines(lines)

# Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument("map", choices=["Map11", "Map12"], help="The map file to be used (either Map11 or Map12).")
parser.add_argument("-p", "--pyke", help="Flag to enable Pyke specific changes", action="store_true")
args = parser.parse_args()

if args.map == "Map11":
    print("Map11 selected. Running Map11-specific logic...")
    input_file = 'temp\map11.py'
else:
    print("Map12 selected. Running Map12-specific logic...")
    input_file = 'temp\map12.py'

pykeFlag = args.pyke # if changing for Pyke announcer. Run program with -p for True, otherwise leave False.

modify_file(input_file, pykeFlag)

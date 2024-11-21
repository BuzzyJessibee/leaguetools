# AnnouncerFix Python Script by buzzyjessibee
# Correct as of 14.23
# Special Thanks to Leischii, Sweet Braised Slime, SirDexal

import re

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
                modified_text = re.sub(pattern, pyke_map1_replacement, text)
            else:
                modified_text = re.sub(pattern, pyke_map2_replacement, text)
        else:
            modified_text = re.sub(pattern, replacement_mapThings, text)

    else:
        #print('Normal Event!')
        modified_text = re.sub(pattern, replacement, text)
    
    return modified_text

# Function to modify the file
def modify_file(input_file, output_file, pykeFlag):
    pattern = r'("Play_vo_Announcer_)(@voice@)(_[a-zA-Z0-3]+)(.*)'
    # Open the input file for reading and the output file for writing
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Read through each line in the input file
        for line in infile:
            # Apply the regex replacement only if the line matches the pattern
            match = re.search(pattern, line)

            if match:
                modified_line = modify_soundkey(line, pykeFlag)
            else:
                modified_line = line

            # Write the modified (or unchanged) line to the output file
            outfile.write(modified_line)

# Example usage
input_file = 'map11.py'
output_file = 'map11_replace.py'
pykeFlag = False # if changing for Pyke announcer, change to True, otherwise leave False.

modify_file(input_file, output_file, pykeFlag)

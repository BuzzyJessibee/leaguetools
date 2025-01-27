# This program is free software: you can redistribute it and/or modify
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

# Fix Ahri globals S15 - Copyright (C) 2025 buzzyjessibee
#                      __
#                     // \
#                     \\_/ //
#   ''-.._.-''-.._.. -(||)(')
#                     '''
#

# Special thanks to:
#           GuiSai for the original globals values
#           Slime for helping with the ARAM globals

import re

def add_to_globals(pattern, text_to_insert, offset, delete=False):
    file_path = "temp\globals.py"

    # Open file for editing
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Search for the pattern using regex and find the line number
    for i, line in enumerate(lines):
        if re.search(pattern, line):

            insert_position = i + offset

            if delete:
                del lines[insert_position] # Delete "AudioFeature(None)"

            lines.insert(insert_position, text_to_insert)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)



text = '''            "MapID(11)?AudioFeature(AhriAnnouncer)"
            "MapID(11)?AnnouncerVoice(Ahri)"
            "MapID(11)?ShowCustomAnnouncerOption(1)"
            "MapID(11)?CustomAnnouncerMessage(game_message_AhriAnnouncerEnabled)"
'''

text_12 = '''            "MapID(12)?AudioFeature(AhriAnnouncer)"
            "MapID(12)?AnnouncerVoice(Ahri)"
            "MapID(12)?ShowCustomAnnouncerOption(1)"
            "MapID(12)?CustomAnnouncerMessage(game_message_AhriAnnouncerEnabled)"
'''

# Change Default
add_to_globals(r'^\s*mExpandedMutator: string = "Default"$', text, 5, delete=True)

# Change PracticeTool
add_to_globals(r'^\s*mExpandedMutator: string = "PracticeTool"$', text, 8)

# Change ARAM
add_to_globals(r'^\s*mExpandedMutator: string = "ARAM"$', text_12, 2)

# Change Classic(?)
add_to_globals(r'^\s*mExpandedMutator: string = "CLASSIC"$', text, 2)

# Change Swiftplay
add_to_globals(r'^\s*mExpandedMutator: string = "SWIFTPLAY"$', text, 6, delete=True)

# Change dumb riot shit
add_to_globals(r'^\s*mExpandedMutator: string = "MapSkin_Map11_Boba_SRS"$', text, 3, delete=True)

# 15.2 ARURF
add_to_globals(r'^\s*mExpandedMutator: string = "ARURF"$', text, 12, delete=True)
add_to_globals(r'^\s*mExpandedMutator: string = "URF"$', text, 12, delete=True)

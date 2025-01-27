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

# Fantome info.json Maker - Copyright (C) 2025 buzzyjessibee
#                      __
#                     // \
#                     \\_/ //
#   ''-.._.-''-.._.. -(||)(')
#                     '''
#

import json
import os

# info.json base structure
data = {
    "Author": "GuiSai | Maintained by Jessibee",
    "Description": "\"Come on, Kiko, we're the life of the party.\"",
    "Heart": "",
    "Home": "",
    "Name": "Star Guardian Ahri Announcer Base",
    "Version": ""
}

# Ask the user for a version number
version_number = input("Enter the version number: ")

# Update the Version field in the data structure
data["Version"] = version_number

# Define the relative output path
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, "../output/META") 

# Output file name
output_file = os.path.join(output_folder, "info.json")

# Write the updated structure to a JSON file
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"JSON file created successfully: {output_file}")

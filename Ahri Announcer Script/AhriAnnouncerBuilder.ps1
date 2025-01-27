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

# Fix Ahri S15 - Copyright (C) 2025 buzzyjessibee
#                      __
#                     // \
#                     \\_/ //
#   ''-.._.-''-.._.. -(||)(')
#                     '''

Write-Host "                      __"
Write-Host "                     // \"
Write-Host "                     \\_/ //"
Write-Host "   ''-.._.-''-.._.. -(||)(')"
Write-Host "                     '''"
Write-Host ""
Write-Host "Fix Ahri S15 - Copyright (C) 2025 buzzyjessibee"
Write-Host ""

# Create a Stopwatch instance
$stopwatch = [System.Diagnostics.Stopwatch]::StartNew()

# Update Hashes From CDragon
Write-Host "Updating Hashes..."
cdtb fetch-hashes
Copy-Item "$env:LOCALAPPDATA\cdragon\data\hashes\lol\hashes.game.txt" ".\cslol-tools" -Force
Copy-Item "$env:LOCALAPPDATA\cdragon\data\hashes\lol\*" ".\ritobin\bin\hashes" -Force

# Prepare for wad extraction
Write-Host "Creating temp dir and copying wads..."
New-Item -ItemType Directory -Force -Path "temp" | Out-Null
Copy-Item "C:\Riot Games\League of Legends\Game\DATA\FINAL\Global.wad.client" ".\temp" -Force
Copy-Item "C:\Riot Games\League of Legends\Game\DATA\FINAL\Maps\Shipping\Map11.wad.client" ".\temp" -Force
Copy-Item "C:\Riot Games\League of Legends\Game\DATA\FINAL\Maps\Shipping\Map12.wad.client" ".\temp" -Force
Copy-Item "C:\Riot Games\League of Legends\Game\DATA\FINAL\Maps\Shipping\Map11.en_US.wad.client" ".\temp" -Force

# Working with Global.wad.client
Write-Host "Extracting Global.wad.client..."
Start-Process ".\cslol-tools\wad-extract.exe" -ArgumentList ".\temp\Global.wad.client" -Wait
Write-Host "Extracting globals..."
Copy-Item ".\temp\Global.wad\globals" ".\temp" -Force
Write-Host "Cleaning Up..."
Remove-Item ".\temp\Global.wad" -Recurse -Force
Remove-Item ".\temp\Global.wad.client" -Force

# Working with Map11.wad.client
Write-Host "Extracting Map11.wad.client..."
Start-Process ".\cslol-tools\wad-extract.exe" -ArgumentList ".\temp\Map11.wad.client" -Wait
Write-Host "Extracting map11.bin..."
Copy-Item ".\temp\Map11.wad\data\maps\shipping\map11\map11.bin" ".\temp" -Force
Write-Host "Cleaning Up..."
Remove-Item ".\temp\Map11.wad" -Recurse -Force
Remove-Item ".\temp\Map11.wad.client" -Force

# Working with Map12.wad.client
Write-Host "Extracting Map12.wad.client..."
Start-Process ".\cslol-tools\wad-extract.exe" -ArgumentList ".\temp\Map12.wad.client" -Wait
Write-Host "Extracting map12.bin..."
Copy-Item ".\temp\Map12.wad\data\maps\shipping\map12\map12.bin" ".\temp" -Force
Write-Host "Cleaning Up..."
Remove-Item ".\temp\Map12.wad" -Recurse -Force
Remove-Item ".\temp\Map12.wad.client" -Force

# Working with Map11.en_US.wad.client
Write-Host "Extracting Map11.en_US.wad.client"
Start-Process ".\cslol-tools\wad-extract.exe" -ArgumentList ".\temp\Map11.en_US.wad.client" -Wait
Write-Host "Extracting Ahri Announcer Files..."
Copy-Item ".\temp\Map11.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared\announcer_global_ahri_vo_audio.bnk" ".\temp" -Force
Copy-Item ".\temp\Map11.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared\announcer_global_ahri_vo_audio.wpk" ".\temp" -Force
Copy-Item ".\temp\Map11.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared\announcer_global_ahri_vo_events.bnk" ".\temp" -Force
Write-Host "Cleaning Up..."
Remove-Item ".\temp\Map11.en_US.wad" -Recurse -Force
Remove-Item ".\temp\Map11.en_US.wad.client" -Force 

# Rename globals to globals.bin
Write-Host "Renaming globals"
Rename-Item -Path ".\temp\globals" -NewName "globals.bin"

# Converting bins with Ritobin
Write-Host "Converting Bins..."
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\globals.bin" -Wait
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\map11.bin" -Wait
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\map12.bin" -Wait

# Clean up bins
Write-Host "Removing Old Bins..."
Remove-Item ".\temp\globals.bin" -Force
Remove-Item ".\temp\map11.bin" -Force 
Remove-Item ".\temp\map12.bin" -Force 

# Run Python Scripts on Files
Write-Host "Running fixAhri_Globals Script..."
python .\scripts\fixAhri_globals_S15.py
Write-Host "Running fixAhri_Maps Script on map11.bin..."
python .\scripts\fixAhri_Maps_S15.py Map11
Write-Host "Running fixAhri_Maps Script on map12.bin..."
python .\scripts\fixAhri_Maps_S15.py Map12
Write-Host "Running AnnouncerFix Script on map11.bin..."
python .\scripts\AnnouncerFix.py Map11
Write-Host "Running AnnouncerFix Script on map12.bin..."
python .\scripts\AnnouncerFix.py Map12

# Convert py with Ritobin
Write-Host "Converting back to bin..."
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\globals.py" -Wait
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\map11.py" -Wait
Start-Process ".\ritobin\bin\ritobin_cli.exe" -ArgumentList ".\temp\map12.py" -Wait

# Clean up py files
Write-Host "Removing the .py files..."
Remove-Item ".\temp\globals.py" -Force
Remove-Item ".\temp\map11.py" -Force 
Remove-Item ".\temp\map12.py" -Force 

# Rename globals.bin to globals
Write-Host "Renaming globals (part 2)"
Rename-Item -Path ".\temp\globals.bin" -NewName "globals"

# Prepare Mod
Write-Host "Preparing mod output directories..."
New-Item -ItemType Directory -Force -Path "output" | Out-Null
New-Item -ItemType Directory -Force -Path "output\META" | Out-Null
New-Item -ItemType Directory -Force -Path "output\WAD" | Out-Null

# Make info.json
Write-Host "Creating info.json"
python .\scripts\info_maker.py 

# Prepare wad folders
Write-Host "Preparing Wads..."
Write-Host "Creating Directories..."
New-Item -ItemType Directory -Path ".\temp\Map11.wad\data\maps\shipping\map11\" -Force | Out-Null
New-Item -ItemType Directory -Path ".\temp\Map12.wad\data\maps\shipping\map12\" -Force | Out-Null
New-Item -ItemType Directory -Path ".\temp\Map12.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared" -Force | Out-Null
New-Item -ItemType Directory -Path ".\temp\Global.wad\" -Force | Out-Null

# Move Files to wad folders
Write-Host "Moving files..."
Move-Item -Path ".\temp\globals" -Destination ".\temp\Global.wad\globals"
Move-Item -Path ".\temp\map11.bin" -Destination ".\temp\Map11.wad\data\maps\shipping\map11\map11.bin"
Move-Item -Path ".\temp\map12.bin" -Destination ".\temp\Map12.wad\data\maps\shipping\map12\map12.bin"
Move-Item -Path ".\temp\announcer_global_ahri_vo_audio.bnk" -Destination ".\temp\Map12.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared" -Force
Move-Item -Path ".\temp\announcer_global_ahri_vo_audio.wpk" -Destination ".\temp\Map12.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared" -Force
Move-Item -Path ".\temp\announcer_global_ahri_vo_events.bnk" -Destination ".\temp\Map12.en_US.wad\assets\sounds\wwise2016\vo\en_us\shared" -Force

# Make Wads
Write-Host "Making Wads..."
Start-Process ".\cslol-tools\wad-make.exe" -ArgumentList ".\temp\Global.wad" -Wait
Start-Process ".\cslol-tools\wad-make.exe" -ArgumentList ".\temp\Map11.wad" -Wait 
Start-Process ".\cslol-tools\wad-make.exe" -ArgumentList ".\temp\Map12.wad" -Wait
Start-Process ".\cslol-tools\wad-make.exe" -ArgumentList ".\temp\Map12.en_US.wad" -Wait 

# Move wads to mod
Write-Host "Moving Wads..."
Move-Item -Path ".\temp\Global.wad.client" -Destination ".\output\WAD"
Move-Item -Path ".\temp\Map11.wad.client" -Destination ".\output\WAD"
Move-Item -Path ".\temp\Map12.wad.client" -Destination ".\output\WAD"
Move-Item -Path ".\temp\Map12.en_US.wad.client" -Destination ".\output\WAD"

# Clean up folders
Write-Host "Cleaning up temp dir..."
Remove-Item ".\temp\" -Recurse -Force 

# Zip Mod
Write-Host "Zipping Mod..."
Compress-Archive -Path ".\output\META", ".\output\WAD" -DestinationPath ".\output\SG_Ahri_Base.zip"
Rename-Item -Path ".\output\SG_Ahri_Base.zip" -NewName "SG_Ahri_Base.fantome"

# Clean Up Output
Write-Host "Cleaning up output dir..."
Remove-Item ".\output\META" -Recurse -Force
Remove-Item ".\output\WAD" -Recurse -Force 

# Done
Write-Host "Done!"

# Stop the stopwatch
$stopwatch.Stop() 

# Get total elapsed seconds
$totalSeconds = $stopwatch.Elapsed.TotalSeconds

# Calculate minutes and seconds
$minutes = [math]::Floor($totalSeconds / 60)
$seconds = [math]::Floor($totalSeconds % 60)

# Output the elapsed time in minutes and seconds
Write-Host "Elapsed time: $minutes minutes and $seconds seconds"

# Don't Close Window!
Read-Host "Press Enter to continue"
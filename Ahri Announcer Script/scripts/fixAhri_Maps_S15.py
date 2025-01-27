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

# Fix Ahri Map11/12 S15 - Copyright (C) 2025 buzzyjessibee
#                      __
#                     // \
#                     \\_/ //
#   ''-.._.-''-.._.. -(||)(')
#                     '''
#

# Special thanks to Slime for the bank data <3

import re
import argparse

def modify_file(file_path, pattern, text_to_insert, ins_offset, map_id):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Search for the pattern using regex and find the line number
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            # Insert the text at offset
            insert_position = i + ins_offset
            
            # Ensure we're not inserting beyond the file's end
            if insert_position <= len(lines):
                lines.insert(insert_position, text_to_insert)
            else:
                # If the position is beyond the last line, append the text
                lines.append(text_to_insert)
            break  # Stop after inserting text at the first match
    
    if map_id == 12: # ARAM Specific Logic
        pattern = r'^\s*0xa02b6406: list2\[link\] = \{$'
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                # Insert the text at offset
                insert_position = i + 6
                lines.insert(insert_position, "            0x6a22acfa\n")
                break  # Stop after inserting text at the first match

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Bank Files Entries to insert
text_to_insert_map11 = '''        BankUnit {
                name: string = "ENV_Map11_Boba2025"
                bankPath: list[string] = {
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/ENV_Map11_Boba2025_audio.bnk"
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/ENV_Map11_Boba2025_events.bnk"
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/ENV_Map11_Boba2025_audio.wpk"
                }
                events: list[string] = {
                    "Play_sfx_Env_BlackRose_TurretBasicAttack_hit"
                    "Play_sfx_Env_BlackRose_TurretBasicAttack_missilelaunch"
                    "Play_sfx_Env_BlackRose_TurretChampionBasicAttack_cast"
                    "Play_sfx_Env_BlackRose_TurretChampionBasicAttack_hit"
                    "Play_sfx_Env_BlackRose_TurretChampionBasicAttack_missilelaunch"
                    "Play_sfx_Env_Boba_BlackRose_Inhibitor_alive_loop"
                    "Play_sfx_Env_Boba_BlackRose_Inhibitor_death_cast"
                    "Play_sfx_Env_Boba_BlackRose_Inhibitor_death_loop"
                    "Play_sfx_Env_Boba_BlackRose_Inhibitor_respawn_cast"
                    "Play_sfx_Env_Boba_BlackRose_Inhibitor_spawn"
                    "Play_sfx_Env_Boba_BlackRose_Nexus_active_loop"
                    "Play_sfx_Env_Boba_BlackRose_Nexus_spawn"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_alive_loop"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_death_cast"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_death_loop"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_idle_cast"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_respawn_cast"
                    "Play_sfx_Env_Boba_Noxus_Inhibitor_spawn"
                    "Play_sfx_Env_Boba_Noxus_Nexus_active_loop"
                    "Play_sfx_Env_Boba_Noxus_Nexus_death"
                    "Play_sfx_Env_Boba_Noxus_Nexus_spawn"
                    "Play_sfx_Env_Map11_Boba_Ambience"
                    "Play_sfx_Env_Map11_Boba_AmbienceBase"
                    "Play_sfx_Env_Map11_Boba_AmbienceNEJungle"
                    "Play_sfx_Env_Map11_Boba_AmbienceNWJungle"
                    "Play_sfx_Env_Map11_Boba_AmbienceSEJungle"
                    "Play_sfx_Env_Map11_Boba_AmbienceSWJungle"
                    "Play_sfx_Env_Map11_Boba_Noxtorra_Idle1"
                    "Play_sfx_Env_Map11_Boba_Noxtorra_Idle2"
                    "Play_sfx_Env_Noxus_Turret_death"
                    "Play_sfx_Env_Noxus_TurretBasicAttack_hit"
                    "Play_sfx_Env_Noxus_TurretBasicAttack_missilelaunch"
                    "Play_sfx_Env_Noxus_TurretChampionBasicAttack_cast"
                    "Play_sfx_Env_Noxus_TurretChampionBasicAttack_hit"
                    "Play_sfx_Env_Noxus_TurretChampionBasicAttack_missilelaunch"
                    "Play_sfx_Env_Noxus_TurretNexus_respawn"
                    "Play_sfx_Env_Noxus_TurretShield_spawn"
                }
            }
            BankUnit {
                name: string = "MUS_Map11_SEASONAL_25s1_BOBA"
                bankPath: list[string] = {
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/MUS_map11_SEASONAL_25s1_BOBA_audio.bnk"
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/MUS_map11_SEASONAL_25s1_BOBA_events.bnk"
                    "ASSETS/Sounds/Wwise2016/SFX/Shared/MUS_map11_SEASONAL_25s1_BOBA_audio.wpk"
                }
            }
'''

text_to_insert_map12 = '''    0x6a22acfa = FeatureAudioDataProperties {
        bankUnits: list2[embed] = {
            BankUnit {
                name: string = "Announcer_Global_Ahri_VO"
                bankPath: list[string] = {
                    "ASSETS/Sounds/Wwise2016/VO/en_US/Shared/Announcer_Global_Ahri_VO_audio.bnk"
                    "ASSETS/Sounds/Wwise2016/VO/en_US/Shared/Announcer_Global_Ahri_VO_events.bnk"
                    "ASSETS/Sounds/Wwise2016/VO/en_US/Shared/Announcer_Global_Ahri_VO_audio.wpk"
                }
                events: list[string] = {
                    "Play_vo_Announcer_Global_Ahri_OnAce"
                    "Play_vo_Announcer_Global_Ahri_OnAceblue"
                    "Play_vo_Announcer_Global_Ahri_OnAcepurple"
                    "Play_vo_Announcer_Global_Ahri_OnAcered"
                    "Play_vo_Announcer_Global_Ahri_OnChampionDoubleKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionDoubleKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionDoubleKillpurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionDoubleKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionDoubleKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionHexaKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionHexaKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionHexaKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionHexaKillYou"
                    "Play_vo_Announcer_Global_Ahri_OnChampionHexaKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillHeroHero"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillHeroHeroEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillHeroHeroYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillHeroYouEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionblueHero"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionblueHeropurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionblueHerored"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillMinionHeroEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillMinionHeroYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionpurpleHero"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionpurpleHeroblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionredHero"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillminionredHeroblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillMinionYouEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillturretblueHeropurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillturretblueHerored"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillTurretHeroAlt"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillTurretHeroEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillTurretHeroYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillturretpurpleHeroblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillturretredHeroblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillTurretYouEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionKillYouHeroYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionPentaKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionPentaKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionPentaKillpurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionPentaKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionPentaKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionQuadraKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionQuadraKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionQuadraKillpurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionQuadraKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionQuadraKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionTripleKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionTripleKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionTripleKillpurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionTripleKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionTripleKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionUnrealKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnChampionUnrealKillEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnChampionUnrealKillpurple"
                    "Play_vo_Announcer_Global_Ahri_OnChampionUnrealKillred"
                    "Play_vo_Announcer_Global_Ahri_OnChampionUnrealKillYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerDieblue"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerDieEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerDiepurple"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerDiered"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerDieYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnblue"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnpurple"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnred"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnSoonblue"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnSoonEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnSoonpurple"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnSoonred"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnSoonYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerRespawnYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerUnderAttackblue"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerUnderAttackpurple"
                    "Play_vo_Announcer_Global_Ahri_OnDampenerUnderAttackred"
                    "Play_vo_Announcer_Global_Ahri_OnDefeat"
                    "Play_vo_Announcer_Global_Ahri_OnFirstBlood"
                    "Play_vo_Announcer_Global_Ahri_OnInhibitorAttackedYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillDragonblue"
                    "Play_vo_Announcer_Global_Ahri_OnKillDragonpurple"
                    "Play_vo_Announcer_Global_Ahri_OnKillDragonred"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpree"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet1"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet2"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet3"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet4"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet5"
                    "Play_vo_Announcer_Global_Ahri_OnKilledUnitOnKillingSpreeSet6"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet1YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet2YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet3YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet4YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet5YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6blue"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6EnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6purple"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6red"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6You"
                    "Play_vo_Announcer_Global_Ahri_OnKillingSpreeSet6YourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnKillWormblue"
                    "Play_vo_Announcer_Global_Ahri_OnKillWormpurple"
                    "Play_vo_Announcer_Global_Ahri_OnKillWormred"
                    "Play_vo_Announcer_Global_Ahri_OnLeave"
                    "Play_vo_Announcer_Global_Ahri_OnLeaveEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnLeaveYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnMinionAlmostKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnMinionAlmostKillred"
                    "Play_vo_Announcer_Global_Ahri_OnMinionHalfKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnMinionHalfKillred"
                    "Play_vo_Announcer_Global_Ahri_OnMinionsSpawn"
                    "Play_vo_Announcer_Global_Ahri_OnNexusAttackedYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnNexusUnderAttackblue"
                    "Play_vo_Announcer_Global_Ahri_OnNexusUnderAttackpurple"
                    "Play_vo_Announcer_Global_Ahri_OnNexusUnderAttackred"
                    "Play_vo_Announcer_Global_Ahri_OnOneMinuteMinionsSpawn"
                    "Play_vo_Announcer_Global_Ahri_OnQuit"
                    "Play_vo_Announcer_Global_Ahri_OnQuitEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnQuitEnemyTeamAlt"
                    "Play_vo_Announcer_Global_Ahri_OnQuitYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnQuitYourTeamAlt"
                    "Play_vo_Announcer_Global_Ahri_OnReconnect"
                    "Play_vo_Announcer_Global_Ahri_OnReconnectEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnReconnectYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map1"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map10"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map11"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map2"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map4"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map6"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1Map8"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2ButchersBridge"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map1"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map10"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map11"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map12"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map2"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map3"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map4"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map6"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage2Map8"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage3Map10"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage3Map3"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage3Map8"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage4Map10"
                    "Play_vo_Announcer_Global_Ahri_OnSurrenderblue"
                    "Play_vo_Announcer_Global_Ahri_OnSurrenderpurple"
                    "Play_vo_Announcer_Global_Ahri_OnSurrenderred"
                    "Play_vo_Announcer_Global_Ahri_OnTurretAlmostKillblue"
                    "Play_vo_Announcer_Global_Ahri_OnTurretAlmostKillred"
                    "Play_vo_Announcer_Global_Ahri_OnTurretAttackedYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnTurretDieblue"
                    "Play_vo_Announcer_Global_Ahri_OnTurretDieEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnTurretDiepurple"
                    "Play_vo_Announcer_Global_Ahri_OnTurretDiered"
                    "Play_vo_Announcer_Global_Ahri_OnTurretDieYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnTurretHalfKillred"
                    "Play_vo_Announcer_Global_Ahri_OnTurretUnderAttackblue"
                    "Play_vo_Announcer_Global_Ahri_OnTurretUnderAttackpurple"
                    "Play_vo_Announcer_Global_Ahri_OnTurretUnderAttackred"
                    "Play_vo_Announcer_Global_Ahri_OnVictory"
                    "Play_vo_Announcer_Global_Ahri_OnVictoryblue"
                    "Play_vo_Announcer_Global_Ahri_OnVictorypurple"
                    "Play_vo_Announcer_Global_Ahri_OnVictoryred"
                    "Play_vo_Announcer_Global_Ahri_OnWelcome"
                    "Play_vo_Announcer_Global_Ahri_OnWelcomeToLeague"
                    "Play_vo_Announcer_Global_Ahri_TurretPlatingFall30Seconds"
                    "Play_vo_Announcer_Global_Ahri_TurretPlatingFallOff"
                    "Play_vo_Announcer_Global_Ahri_OnPointEnemyTeam"
                    "Play_vo_Announcer_Global_Ahri_OnPointYou"
                    "Play_vo_Announcer_Global_Ahri_OnPointYourTeam"
                    "Play_vo_Announcer_Global_Ahri_OnStartGameMessage1ModeSnowdowShowdown"
                    "Play_vo_Announcer_Global_Ahri_OnVictoryAlmostEnemy"
                    "Play_vo_Announcer_Global_Ahri_OnVictoryAlmostYou"
                    "Play_vo_Announcer_Global_Ahri_OnVictoryAlmostYourTeam"
                }
                voiceOver: bool = true
            }
        }
        music: embed = MusicAudioDataProperties {
            themeMusicID: string = "mus_map12_phase_select"
            victoryMusicID: string = "mus_map12_victory"
            defeatMusicID: string = "mus_map12_defeat"
            victoryBannerSound: string = "Play_sfx_Env_SRUAP_Victory_Banner"
            defeatBannerSound: string = "Play_sfx_Evn_SRUAP_Defeat_Banner"
            ambientEvent: string = "Play_sfx_Env_Map12_Ambience_base"
        }
        feature: hash = 0x15de0934
    }
'''

# Command Line Parser
parser = argparse.ArgumentParser()
parser.add_argument("map", choices=["Map11", "Map12"], help="The map file to be used (either Map11 or Map12).")
args = parser.parse_args()

if args.map == "Map11":
    print("Map11 selected. Running Map11-specific logic...")
    file_path = "temp\map11.py"
    pattern = r'"Announcer_Global_Ahri_VO"'
    modify_file(file_path, pattern, text_to_insert_map11, 7, map_id=11)
else:
    print("Map12 selected. Running Map12-specific logic...")
    file_path = "temp\map12.py"
    pattern = r'^\s*feature: hash = 0x01692855'
    modify_file(file_path, pattern, text_to_insert_map12, 2, map_id=12)
#Development Order
1. lay out classes and files
2. save/load information
3. character creation
4. display layout and info
5. room creation
6. movement
7. combat


#Define Classes and functions

###Player
1. health - decrements as player fights monsters

*Health
*Battered
*Mauled
*Dead

2. sanity - decrements as player flees from monsters

*Sane
*Colorful
*Loopy
*Insane

3. inventory - list of objects usable by player that are present regardless of player location
4. player_creation - if no player exists, walk player through creation 

###Item
1. item_desc - description of the item
2. item_name - item name
3. item_function - use of item

*Weapon
*Key
*Effect - heals or damages player when used

###GameControl
1. save_game - saves game state

*player stats
*room location

2. load_game - loads game state

###Room
1. movement_options - return to last room, or randomly 1 or 2 other doors to new rooms
2. room_desc - description of the room
3. monster - what monster is present
4. room_options - options attached to certain rooms/monsters

###Display
1. menu_options - options that are always present

#Save Game
#Load Game

2. rebuild_display - resets display to new state when option is selected






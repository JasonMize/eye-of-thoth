from display import Display
from player import Player
from display_room import DisplayRoom
from input_handler import InputHandler
from player_input import PlayerInput

display = Display()
display_room = DisplayRoom(display)
player_input = PlayerInput(display)
player = Player(display, display_room, player_input)
input_handler = InputHandler(display, player_input, player)

#overall game keeps running	
def alive ():
	return player.is_alive


def main ():
	#Main loop 
	while alive():
	
		#draw display
		display.rebuild_display(display_room, player_input, player)
	
		#take player input	
		player_input.player_gives_input()

		#act on player input	
		input_handler.menu_input_handler()
		

if  __name__ == '__main__':
	main()
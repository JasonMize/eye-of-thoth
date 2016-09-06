from display import Display
from player import Player
from display_room import DisplayRoom
from input_handler import InputHandler
from player_input import PlayerInput

display = Display()
player = Player()
display_room = DisplayRoom()
player_input = PlayerInput()
input_handler = InputHandler(display, player_input, player)

#overall game keeps running	
def alive ():
	return player.is_alive


def main ():
	#Main loop 
	while alive():
	
		#draw display
		display.rebuild_display(display_room)
	
		#take player input	
		player_input.player_gives_input(display)

		#act on player input	
		input_handler.menu_input_handler()
		

if  __name__ == '__main__':
	main()
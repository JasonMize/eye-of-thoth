from display import Display
from player import Player

display = Display()
player = Player()

#overall game keeps running	
def alive ():
	return player.is_alive


def main ():
	#Main loop 
	while alive():
	
		#draw display
		display.rebuild_display()
	
		#take player input	
		display.player_gives_input()

		#act on player input	
		display.menu_input_handler()
		

if  __name__ == '__main__':
	main()
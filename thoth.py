from display import Display


display = Display()


#overall game keeps running	
def alive ():
	return display.is_alive


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
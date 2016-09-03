from display import Display

def main ():
	'''Main loop '''
	display = Display()
	while display.alive():
		display.rebuild_display()
		display.player_input()	
		display.menu_input_handler()
		


if  __name__ == '__main__':
	main()
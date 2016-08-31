import os

# import yaml

from display import Display


class GameControl(object):

	def __init__(self):
		pass
		

	def save_game(self):
		if not os.path.exists('./save_games'):
			os.makedirs('./save_games')	

		save_state = [player, "another item, room, health, etc."]	

		filepath = "./save_games/{}.yml".format(player)
			
		with open(filepath, 'w') as save_file:
			yaml.dump(save_state, save_file)

		print("Game saved.")	

	
	def load_game(self):
		pass

	def create_character(self):
		print ("What is your name?")
		player = input("\t> ")	

		Display.menu_options(self)



class PlayerInput (object):

	def __init__(self):
		self.player_selection = ""
		self.list_of_possible_player_selections = []

	#get player input
	def player_gives_input(self, display):
		if display.location == "create_player":
			self.player_selection = input("\tEnter Your Name > ")
		else:	
			self.player_selection = input("\t> ").lower()
			self.list_of_possible_player_selections.append(self.player_selection)

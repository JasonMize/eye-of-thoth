import textwrap

class PlayerInput (object):

	def __init__(self, display):
		self.display = display
		self.player_selection = ""
		self.list_of_possible_player_selections = []


	#get player input
	def player_gives_input(self):
		if self.display.location == "create_player":
			self.player_selection = input("\tEnter Your Name > ")
		else:	
			self.player_selection = input("\t> ").lower()


	def input_validity_checker(self):
		#don't check player name
		if self.display.location == "create_player" or self.player_selection == "":
			self.list_of_possible_player_selections = []
			return self.player_selection
		else: 		
			#take all possible selections and compare them to input, if no match then return error
			list_of_matches = []
			for item in self.list_of_possible_player_selections:
				if self.player_selection == item:
					list_of_matches.append(item)

			if list_of_matches == []:
				
				self.display.error = "error1"				

		self.list_of_possible_player_selections = []


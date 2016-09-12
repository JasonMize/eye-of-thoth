
class Player (object):

    def __init__(self):
        self.health = 4
        self.sanity = 4
        self.is_alive = True
        self.name = ""

    def health_sanity_adjustment (adjustment):
        pass

    def player_reset (self, name):
        self.health = 4
        self.sanity = 4
        self.name = name
        self.is_alive = True

    def draw (self, display):
        pass











# class Player(object):

#   HEALTH = {
#       4 : "Sound In Body",
#       3 : "Battered",
#       2 : "On Death's Doorstep",
#       1 : "Dead",
#   }
  
#   SANITY = {
#       4 : "Sound In Mind",
#       3 : "Unhinged", 
#       2 : "Dangerously Bizarre",
#       1 : "Insane",
#   }


#   def __init__(self, display, display_room, player_input):
#       self.display = display
#       self.display_room = display_room
#       self.player_input = player_input
#       self.is_alive = True
#       self.name = ""
#       self.health = 4
#       self.sanity = 4
#       self.player_physical_attack = 100
#       self.player_mystical_attack = 100


#   #set health 
#   def health_adjustment(self, adjustment):
#       self.health += adjustment
#       print("health: " + str(self.health))
#       if self.health <= 1:
#           self.health = 1
#           self.display.error = "error_dead"
#           self.is_alive = False
#           self.display.rebuild_display(self.display_room, self.player_input, self)
#       return self.health



#   #set sanity 
#   def sanity_adjustment(self, adjustment):
#       self.sanity += adjustment
#       print("sanity: " + str(self.sanity))
#       if self.sanity <= 1:
#           self.sanity = 1
#           self.display.error = "error_insane"
#           self.is_alive = False
#           self.display.rebuild_display(self.display_room, self.player_input, self)
#       return self.sanity


#   def player_reset(self, name):
#       self.name = name
#       self.health = 4
#       self.sanity = 4


#   def get_health(self):
#       return self.HEALTH[self.health]


#   def get_sanity(self):
#       return self.SANITY[self.sanity]

#   def hud(self):  
#       if self.name:       
#           print("\tSANITY: {}\t\t{}\t\tHEALTH: {}".format(self.get_sanity(), self.name, self.get_health() ))





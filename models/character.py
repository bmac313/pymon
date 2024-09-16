class Player:
	name = "Red"   # The default player name if name entry is bypassed
	gender = "AG"  # Gender by default is AG (agender / genderless) if entry is bypassed
	money = 0      # Currency unit is set in game_data.json
	party = []     # Party is an empty list by default
	inventory = [] # Same as party
	badges = []    # This will hold "progression items" like badges in the original Pokemon.
	equipment = [] # holds items equipped by the TRAINER
	
	def __init__(self, name, money, party, inventory, equipment):
		self.name = name
		self.money = money
		self.party = party
		self.inventory = inventory
		self.equipment = equipment

class NPC:
	name = ""
	trainer_class = "NRM"  # Normal-type trainer is default. Names of T. classes can be found in types.json
	
	def __init__(self, name):
		self.name = name
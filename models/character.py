# The class for the player character
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

class Pokemon:
	id = 0
	name = "Missingno"
	epithet = "Glitch Pokemon"
	types = []
	moves_default = []
	gender = "AG"
	catch_rate = 0
	height = 0
	weight = 0
	xp_yield = 0
	level_rate = "slow"
	
	def __init__(self, id, name, epi, types, moves, gender, cr, h, w, xp, lvl_rate):
		self.id = id
		self.name = name
		self.epithet = epi
		self.types = types
		self.moves = moves
		self.gender = gender
		self.catch_rate = cr
		self.height = h
		self.weight = w
		self.xp_yield = xp
		self.level_rate = lvl_rate

class NPC:
	name = ""
	def __init__(self, name):
		self.name = name

class Trainer(NPC):
	trainer_class = "NRM"  # Normal-type trainer is default. Names of T. classes can be found in types.json
	def __init__(self, name, tc):
		super().__init__(self, name, tc)
		self.trainer_class = tc

import json
from src.models import character

with open('json/creature_dex.json') as f:
	dex = json.load(f).get("BULBASAUR")
	gender_ratio_m = dex.get("percent_male")
	gender_ratio_f = dex.get("percent_female")
	bulba = character.Pokemon(
		dex.get("id"),              #self.id
		dex.get("name"),            #self.name
		dex.get("epithet"),         #self.epithet
		dex.get("types"),           #self.types
		dex.get("moves_default"),   #self.moves
		"male",                     #self.gender
		dex.get("catch_rate"),      #self.catch_rate
		dex.get("height"),          #self.height
		dex.get("weight"),          #self.weight
		dex.get("xp_yield"),        #self.xp_yield
		dex.get("level_rate")       #self.level_rate
	)

print(bulba.name)
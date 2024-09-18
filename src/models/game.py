class Move:

class Type:
	
	# if this class is instantiated without parameters, it will default to the settings below.
	# a list of types and abbreviations can be found in types.json.
	abbreviation = "NRM"
	half_effective_on = ["ROC"]
	super_effective_on = []
	no_effect_on = ["GST"]
	trainer_class = {
			"male": ["Idol"],
			"female": ["Idol"],
			"nb": ["Idol"],
			"agender": ["Idol"]
		}
		
	__init__(self, abb, half_eff, super_eff, no_eff, tc):
		self.abbreviation = abb
		self.half_effective_on = half_eff
		self.super_effective_on = super_eff
		self.no_effect_on = no_eff
		self.trainer_class = tc
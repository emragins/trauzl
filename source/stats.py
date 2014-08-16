class Stats(object):
	def __init__(self):
		self.maxHp = 20
		self.hp = self.maxHp
		self.meleeDamage = 10
		self.rangeDamage = 7
		self.moveSpeed = 2
		self.damageReduction = 0
		self.damageReductionType = None
		self.jumpStrength = 5
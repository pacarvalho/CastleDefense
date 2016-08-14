'''
	Castle Defense Player

	Encapsulates the notion of a player. Resource, friendship, etc

	By Paulo and Katie
'''

class Player:
	def __init__(self,name):
		# Player Name
		self.name = name

		# Player resources
		self.resources = {'lumber':0}

	def get_resources(self):
		''' Resources that belong to this player '''
		return self.resources

	def use_resource(self,resource,amount):
		''' 
			Attemps to use the given resource. 
			Returns true if the player has enough of it
		'''
		if (self.resources[resource] >= amount):
			self.resources[resource] -= amount
			return True
		return False

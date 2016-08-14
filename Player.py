'''
	Castle Defense Player

	Encapsulates the notion of a player. Resource, friendship, etc

	By Paulo and Katie
'''

class Player:
	def __init__(self, name='Neutral'):
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

	def get_name(self):
		''' Returns the player name '''
		return self.name

	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

	def __ne__(self, other):
		return not self.__eq__(other)

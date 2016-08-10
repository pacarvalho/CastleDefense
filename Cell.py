'''
	Castle Defense Cell

	Basic building block of the world. Contains the playing entity
	Belongs to a grid. 

	By Paulo and Katie
'''

from entities.Default import Default

class Cell:
	def __init__(self):
		# Contains playing object. Ex: Soldier, wall, etc
		self.entity = Default()
		self.isClicked = False

	'''
		Sets the current entity in this cell
	'''
	def set_entity(self, entity):
		self.entity = entity

	'''
		Deletes the current entity on this cell
	'''
	def delete_entity(self):
		self.entity = Default()


	'''
		Return the range of the entity
		0 for pasive
		1 for melee
		>1 for ranged
	'''
	def get_range_entity(self):
		return self.entity.get_range()

	'''
		Returns the icon of the entity at its current state
	'''
	def get_icon(self):
		if(not self.isClicked):
			return self.entity.get_default_icon()
		else:
			return self.entity.get_highlight_icon()

	'''
		Selects the given cell
	'''
	def select(self):
		self.isClicked = True

	'''
		Selects the given cell
	'''
	def deselect(self):
		self.isClicked = False


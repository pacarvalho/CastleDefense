'''
	Castle Defense Cell

	Basic building block of the world. Contains the playing entity
	Belongs to a grid. 

	By Paulo and Katie
'''

from entities.Default import Default
from copy import deepcopy

class Cell:
	def __init__(self):
		# Contains playing object. Ex: Soldier, wall, etc
		self.entity = Default()

	'''
		Sets the current entity in this cell
	'''
	def set_entity(self, entity):
		self.entity = entity

	'''
		Gets the current entity in this cell
	'''
	def get_entity(self):
		return self.entity

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
		return self.entity.get_icon()

	'''
		Selects the given cell
	'''
	def select(self):
		return self.entity.set_selected(True)

	'''
		Selects the given cell
	'''
	def deselect(self):
		return self.entity.set_selected(False)

	'''
		Sets the path that the underlying entity should follow
	'''
	def set_motion_path(self, path):
		self.entity.set_motion_path(path)

	'''
		Returns the destination from the entity
	'''
	def get_destination(self, game_cycle):
		return self.entity.get_destination(game_cycle)

	'''
		Returns if the underlying entity is passable
	'''
	def get_blocking(self):
		return self.entity.get_blocking()


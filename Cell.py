'''
	Castle Defense Cell

	Basic building block of the world. Contains the playing entity
	Belongs to a grid. 

	By Paulo and Katie
'''

from entities.Default import Default
from entities.Tree import Tree
from entities.Peasant import Peasant
from entities.Wall import Wall
from copy import deepcopy
from Player import Player

class Cell:
	def __init__(self):
		# Contains playing object. Ex: Soldier, wall, etc
		self.entity = Default(Player())


	'''
		Sets the current entity in this cell
	'''
	def set_entity(self, entity):
		self.entity = entity

	'''
		Sets the entity by string name
	'''
	def set_entity_by_name(self,name,player):
		if name == 'wall':
			self.set_entity(Wall(player))

	'''
		Gets the current entity in this cell
	'''
	def get_entity(self):
		return self.entity

	'''
		Deletes the current entity on this cell
	'''
	def delete_entity(self):
		self.entity = Default(Player())


	'''
		Return the range of the entity
		0 for pasive
		1 for melee
		>1 for ranged
	'''
	def get_range(self):
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

	'''
		Returns if this cell is currently selected
	'''
	def get_selected(self):
		return self.entity.get_selected()

	'''
		Returns a list of the available actions
	'''
	def get_available_actions(self):
		return self.entity.get_available_actions()

	def set_destination_action(self, action):
		''' Sets the actions to be executed at destination '''
		self.entity.set_destination_action(action)

	def get_destination_action(self):
		''' Gets the actions to be executed at destination '''
		return self.entity.get_destination_action()

	def get_remaining_steps_path(self):
		''' Number of steps remaining in the path '''
		return self.entity.get_remaining_steps_path()

	def reset_action(self):
		self.entity.reset_action()

	def get_player(self):
		''' Returns the player to whom the underlying entity belongs '''
		return self.entity.get_player()




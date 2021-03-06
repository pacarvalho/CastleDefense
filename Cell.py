'''
	Castle Defense Cell

	Basic building block of the world. Contains the playing entity
	Belongs to a grid. 

	By Paulo and Katie
'''

from entities.Entity import Entity
from copy import deepcopy
from Player import Player
import json

class Cell:
	def __init__(self):
		self.entities = {}

		# Import JSON Definition File
		with open('entities/entities.json', 'r') as data_file:
			self.entities = json.load(data_file)

		# Contains playing object. Ex: Soldier, wall, etc
		self.entity = Entity(Player(),self.entities['default'])

	'''
		Sets the current entity in this cell
	'''
	def set_entity(self, entity):
		self.entity = entity

	'''
		Sets the entity by string name
	'''
	def set_entity_by_name(self,name,player):
		self.set_entity(Entity(player,self.entities[name]))

	'''
		Gets the current entity in this cell
	'''
	def get_entity(self):
		return self.entity

	'''
		Deletes the current entity on this cell
	'''
	def delete_entity(self):
		self.entity = Entity(Player(),self.entities['default'])


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

	def get_attack_damage(self, game_cycle):
		''' Returns the attack damage of this entity for this iteration '''
		return self.entity.get_attack_damage(game_cycle)

	def deduct_hitpoints(self,value):
		''' 
			Number of hitpoints to deduct 
			Return False when entity has 0 hitpoints
		'''
		return self.entity.deduct_hitpoints(value)

	def increment_hitpoints(self,value):
		''' 
			Number of hitpoints to deduct 
			Returns false once entity has full HP
		'''
		return self.entity.increment_hitpoints(value)




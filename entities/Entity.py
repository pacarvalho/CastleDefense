'''
	Castle Defense Entity - Entity

	Becomes a specific entity determined by config file

	By Katie and Paulo
'''
from PIL import ImageTk
from EntityBase import EntityBase
from copy import deepcopy
from collections import deque

class Entity(EntityBase):
	def __init__(self, player, config):
		self.config = config

		# Does this cell block others from stepping on it or going through?
		self.blocking = self.config['blocking']

		# Entity description
		self.description = self.config['name']

		# Icons
		self.default_icon = ImageTk.PhotoImage(file=self.config['default_icon'])
		self.highlight_icon = ImageTk.PhotoImage(file=self.config['highlight_icon'])

		# Is the entity currently clicked?
		self.isClicked = False

		# Current motion path
		self.motion_path = deque()

		# Last time this entity moved and attacked
		self.last_motion_cycle = 0
		self.last_attack_cycle = 0

		# Motion speed of the entity in game iterations
		self.speed = self.config['movement_speed']

		# All available actions
		self.available_actions = self.config['available_actions']

		# Destination action - Action to be executed at end of path
		self.destination_action = tuple(self.config['default_action'])

		# Belongs to player
		self.player = player

		# Attack speed of the entity in game iterations
		# And other attack properties
		self.attack_speed = self.config['attack_speed']
		self.attack_damage = self.config['attack_damage']
		self.attack_range = self.config['attack_range']


		# Current and Maximum hitpoints of the entity (cur,max)
		self.hitpoints = [self.config['start_hitpoints'],self.config['max_hitpoints']]

	# Returns the action range of this entity
	def get_range(self):
		return self.attack_range

	# Returns the image of the current state
	def get_icon(self):
		if(not self.isClicked):
			return self.default_icon
		else:
			return self.highlight_icon

		return self.default_icon

	def get_hitpoints(self):
		''' Returns the current hitpoints of the entity '''
		return self.hitpoints

	def get_description(self):
		''' Returns the current hitpoints of the entity '''
		return self.description

	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return self.isClicked

	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		self.isClicked = state
		return self.isClicked

	def get_blocking(self):
		''' Returns true if object cannot be walked on '''
		return self.blocking

	def set_motion_path(self,path):
		''' Sets the path for motion '''
		self.motion_path = deque(deepcopy(path))

	def get_destination(self, game_cycle):
		''' 
			Gets the next cell for moving this entity 

			Returns null if its not time for the entity to move
		'''
		if (len(self.motion_path) > 0) and (self.last_motion_cycle+self.speed <= game_cycle):
			self.last_motion_cycle = game_cycle
			return self.motion_path.popleft()
		return tuple()

	def get_available_actions(self):
		''' Returns a list of strings with the available actions '''
		return self.available_actions

	def set_destination_action(self, action):
		''' Sets the actions to be executed at destination '''
		self.destination_action = action

	def get_destination_action(self):
		''' Gets the actions to be executed at destination '''
		return self.destination_action

	def get_remaining_steps_path(self):
		''' Number of steps remaining in the path '''
		return len(self.motion_path)

	def reset_action(self):
		''' Resets all actions in the entity '''
		self.destination_action = tuple(self.config['available_actions'])
		self.motion_path = deque()

	def get_player(self):
		''' Returns the player to whom this entity belongs '''
		return self.player

	def get_attack_damage(self, game_cycle):
		''' Returns the attack damage of this entity for this iteration '''
		if (self.last_attack_cycle+self.attack_speed) <= game_cycle:
			self.last_attack_cycle = game_cycle
			return self.attack_damage
		return 0

	def deduct_hitpoints(self,value):
		''' 
			Number of hitpoints to deduct 
			Return False when entity has 0 hitpoints
		'''
		self.hitpoints[0] -= value
		if (self.hitpoints[0] <= 0):
			self.hitpoints[0] = 0
			return False
		return True

	def increment_hitpoints(self,value):
		''' 
			Number of hitpoints to deduct 
			Returns false once entity has full HP
		'''
		self.hitpoints[0] += value
		if (self.hitpoints[0] >= self.hitpoints[1]):
			self.hitpoints[0] = self.hitpoints[1]
			return False
		return True










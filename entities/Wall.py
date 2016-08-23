'''
	Castle Defense Entity - Wall

	Wall

	By Katie and Paulo
'''
from PIL import ImageTk
from EntityBase import EntityBase
from copy import deepcopy
from collections import deque

class Wall(EntityBase):
	def __init__(self, player):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# Entity description
		self.description = "Wall"

		# Icons
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/wall.gif')
		self.highlight_icon = ImageTk.PhotoImage(file='entities/icons/wall_highlight.gif')

		# Is the entity currently clicked?
		self.isClicked = False

		# Current motion path
		self.motion_path = deque()

		# Last time this entity moved
		self.last_motion_cycle = 0

		# Speed of the entity in game iterations
		self.speed = 0

		# All available actions
		self.available_actions = {}

		# Destination action - Action to be executed at end of path
		self.destination_action = tuple(['',''])

		# Belongs to player
		self.player = player

		# Attack speed of the entity in game iterations
		self.attack_speed = 0

		# Attack damage of the entity
		self.attack_damage = 0

		# Current and Maximum hitpoints of the entity (cur,max)
		self.hitpoints = [1000,1000]

	# Returns the action range of this entity
	def get_range(self):
		return 0

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
		return

	def get_destination(self, game_cycle):
		''' 
			Gets the next cell for moving this entity 

			Returns null if its not time for the entity to move
		'''
		return []

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
		self.destination_action = tuple(['',''])
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








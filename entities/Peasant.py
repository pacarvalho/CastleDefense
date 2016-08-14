'''
	Castle Defense Entity - Peasant

	Peasant

	By Katie and Paulo
'''
from PIL import ImageTk
from EntityBase import EntityBase
from copy import deepcopy
from collections import deque

class Peasant(EntityBase):
	def __init__(self, player):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# Entity description
		self.description = "Peasant"

		# Icons
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/peasant.gif')
		self.highlight_icon = ImageTk.PhotoImage(file='entities/icons/peasant_highlight.gif')

		# Is the entity currently clicked?
		self.isClicked = False

		# Current motion path
		self.motion_path = deque()

		# Last time this entity moved
		self.last_motion_cycle = 0

		# Speed of the entity in game iterations
		self.speed = 1

		# All available actions
		self.available_actions = {'move':[],'build':['house','wall']}

		# Destination action - Action to be executed at end of path
		self.destination_action = tuple(['',''])

		# Belongs to player
		self.player = player

	# Returns the action range of this entity
	def get_range(self):
		return 1

	# Returns the image of the current state
	def get_icon(self):
		if(not self.isClicked):
			return self.default_icon
		else:
			return self.highlight_icon

		return self.default_icon

	def get_hitpoints(self):
		''' Returns the current hitpoints of the entity '''
		return 100

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
		self.destination_action = tuple(['',''])
		self.motion_path = deque()

	def get_player(self):
		''' Returns the player to whom this entity belongs '''
		return self.player











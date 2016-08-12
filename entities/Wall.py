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
	def __init__(self):
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
		self.available_actions = []

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
		return 1000

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









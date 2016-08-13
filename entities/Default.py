'''
	Castle Defense Entity - Default

	Unnocopied terrain

	By Katie and Paulo
'''
from PIL import ImageTk
from EntityBase import EntityBase

class Default(EntityBase):
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = False

		# Entity description
		self.description = ""

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/grass.gif')

		# All available actions
		self.available_actions = {}

		# Destination action - Action to be executed at end of path
		self.destination_action = tuple(['',''])

	# Returns the action range of this entity
	def get_range(self):
		return 0

	# Returns the image of the current state
	def get_icon(self):
		return self.default_icon

	def get_hitpoints(self):
		''' Returns the current hitpoints of the entity '''
		return 100

	def get_description(self):
		''' Returns the current hitpoints of the entity '''
		return self.description

	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return False

	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		return True

	def get_blocking(self):
		''' Returns true if object cannot be walked on '''
		return self.blocking

	def set_motion_path(self,path):
		''' Sets the path for motion '''
		pass

	def get_destination(self, game_cycle):
		''' Gets the next cell for moving this entity '''
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
		return 0

	def reset_action(self):
		''' Resets all actions in the entity '''
		return




'''
	Castle Defense Entity - Base Class

	Interface for all other entities

	By Katie and Paulo
'''
from PIL import ImageTk
import abc

class EntityBase():
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def get_range(self):
		''' Returns the action range of this entity '''
		return 

	@abc.abstractmethod
	def get_icon(self):
		''' Returns the image of the current state '''
		return 

	@abc.abstractmethod
	def get_hitpoints(self):
		''' Returns the current hitpoints of the entity '''
		return 

	@abc.abstractmethod
	def get_description(self):
		''' Returns the description of the entity '''
		return 

	@abc.abstractmethod
	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return 

	@abc.abstractmethod
	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		return  

	@abc.abstractmethod
	def get_blocking(self):
		''' Returns true if object cannot be walked on '''
		return 

	@abc.abstractmethod
	def set_motion_path(self,path):
		''' Sets the path for motion '''
		return

	@abc.abstractmethod
	def get_destination(self, game_cycle):
		''' Gets the next cell for moving this entity '''
		return 


	@abc.abstractmethod
	def get_available_actions(self):
		''' Returns a list of strings with the available actions '''
		return

	@abc.abstractmethod
	def set_destination_action(self, action):
		''' Sets the actions to be executed at destination '''
		return

	@abc.abstractmethod
	def get_destination_action(self, action):
		''' Gets the actions to be executed at destination '''
		return

	@abc.abstractmethod
	def get_remaining_steps_path(self):
		''' Number of steps remaining in the path '''
		return

	@abc.abstractmethod
	def reset_action(self):
		''' Resets all actions in the entity '''
		return

	





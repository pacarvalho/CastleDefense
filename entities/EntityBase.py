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
	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return 

	@abc.abstractmethod
	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		return  



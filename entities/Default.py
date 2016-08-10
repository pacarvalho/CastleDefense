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

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/grass.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 0

	# Returns the image of the current state
	def get_icon(self):
		return self.default_icon

	def get_hitpoints(self):
		''' Returns the current hitpoints of the entity '''
		return 100

	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return self.isClicked

	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		return False


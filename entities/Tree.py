'''
	Castle Defense Entity - Tree

	Tree terrain

	By Paulo and Katie
'''
from PIL import ImageTk
from EntityBase import EntityBase

class Tree(EntityBase):
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/tree.gif')
		self.highlight_icon = ImageTk.PhotoImage(file='entities/icons/tree_highlight.gif')

		# Is the entity currently clicked?
		self.isClicked = False

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
		return 150

	def get_selected(self):
		''' Returns true if entity is currently selected '''
		return self.isClicked

	def set_selected(self, state):
		''' Sets if the entity is or not selected '''
		self.isClicked = False



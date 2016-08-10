'''
	Castle Defense Entity - Tree

	Tree terrain

	By Paulo and Katie
'''
from PIL import ImageTk

class Tree:
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/tree.gif')

		# highlight icon
		self.highlight_icon = ImageTk.PhotoImage(file='entities/icons/tree_highlight.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 0

	# Returns the image of the current state
	def get_default_icon(self):
		return self.default_icon

	# Returns the image of the current state
	def get_highlight_icon(self):
		return self.highlight_icon



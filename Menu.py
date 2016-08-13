'''
	Castle Defense Menu

	Setups central game controls for user

	by Katie and Paulo
'''
from PIL import ImageTk
from Control_Menu import Control_Menu

class Menu	:
	def __init__(self):
		self.minimap = None
		self.menu_icon = ImageTk.PhotoImage(file='entities/icons/menu.gif')
		self.display_init_text = True
		self.default_text = "Welcome to Castle Defense !"
		self.control_menu = Control_Menu()

	def get_icon(self):
		return self.menu_icon

	# Returns the text to display on the menu
	def get_text(self, selected_cells):
		# To start if nothing has been selected, continue to display default text
		if(len(selected_cells) == 0 and self.display_init_text):
			return self.default_text

		# Only when one cell is selected do we display the following
		elif (len(selected_cells) == 1):
			# Set this to False so the default text doesnt display any more
			self.display_init_text = False

			# Get and Display Entity information
			entity = selected_cells.values()[0].get_entity()
			description = entity.get_description()
			hitpoints = entity.get_hitpoints()
			text = description + "\n\nHitpoints: " + str(hitpoints) 
			return text

		# Else dont display anything
		return ""

	def get_available_actions(self, selected_cells):
		# Only continue if there are cells selected
		if len(selected_cells) == 0:
			return {}

		# Get a list of dictionaries for available actions
		valid_actions = [cell.get_available_actions() for cell in selected_cells.values()]

		if len(valid_actions) > 1:
			# Get the intersection of the sets
			# TODO: Improve this so that subactions are intersected
			result = set(valid_actions[0])
			for c in valid_actions[1:]:
				result.intersection_update(c)
			return list(result)
    	
    	# If there is only one cell selected
		return valid_actions[0]

	def get_control_menu(self):
		return self.control_menu









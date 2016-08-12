'''
	Control Menu

	Setups buttons on the menu

	by Katie and Paulo
'''
import Tkinter as tk
from copy import deepcopy

class Control_Menu():
	def __init__(self):
		# Number of buttons
		self.num_btns = 16
		# Initialize the buttons
		self.buttons = [ tk.Button(text = "", command = "", state = "disabled") for i in range(self.num_btns) ]

		# Last set of actions
		self.last_actions = []

		# Action that is currently selected
		self.selected_action = ''

	'''
		Updates the buttons to the currenlty available actions
	'''
	def update_buttons(self, actions):
		# Only update the buttons if the actions differ from the last_actions
		if(set(actions) != set(self.last_actions)):
			# Update local copy of available actions
			self.last_actions = deepcopy(actions)
			
			for i in range(self.num_btns):
				if (len(actions) > i):
					self.buttons[i].config(text=actions[i])
				else:
					self.buttons[i].config(state = "disabled")

	'''
		Returns the buttons 
	'''
	def get_buttons(self):
		return self.buttons

	'''
		Returns the number of buttons
	'''
	def get_num_btns(self):
		return self.num_btns

	'''
		Returns the action that is currently active
		Defined as the button having been clicked or default
	'''
	def get_current_action(self):
		return self.selected_action

	'''
		Sets the current action
	'''
	def set_current_action(self,action):
		self.selected_action = action

				




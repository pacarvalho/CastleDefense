'''
	Control Menu

	Setups buttons on the menu

	by Katie and Paulo
'''
import Tkinter as tk
from copy import deepcopy
from functools import partial

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

		# Menu that is currently being displayed

	'''
		Updates the control menu
	'''
	def update(self,actions):
		# Only update the buttons if the actions differ from the last_actions
		if(set(actions) != set(self.last_actions)):
			# Update local copy of available actions
			self.last_actions = deepcopy(actions)

			# Get the base actions
			base_actions = [action.split('-')[0] for action in self.last_actions]

			# Remove repeats
			# TODO: Implement a method that does not loose the order
			base_actions = list(set(base_actions))

			# If move is available, set it as default action
			if 'move' in base_actions:
				self.selected_action = 'move'

			# Update the buttons
			self.update_buttons(base_actions)

	def update_sub_buttons(self,action):
		subactions = []
		for act in self.last_actions:
			if action == act.split('-')[0]:
				subactions += [act.split('-')[1]]

		self.update_buttons(subactions)
		


	'''
		Updates the buttons to the currenlty available actions
	'''
	def update_buttons(self, unique_actions):	
		for i in range(self.num_btns):
			if (len(unique_actions) > i):
				self.buttons[i].config(text=unique_actions[i],state = "normal")
				self.buttons[i].config(command=partial(self.set_current_action,unique_actions[i]))
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
		if action == 'build':
			self.update_sub_buttons(action)
			self.selected_action = 'move'
			return 
			
		self.selected_action = action

				




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
		self.last_actions = {}

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

			# # Get the base actions
			# base_actions = [action.split('-')[0] for action in self.last_actions]

			# If move is available, set it as default action
			print self.last_actions
			if 'move' in self.last_actions.keys():
				self.selected_action = ('move',[])

			# Update the buttons
			self.update_buttons(self.last_actions.keys(), [])

	'''
		TODO: Add HERE!!
	'''
	def update_sub_buttons(self,action):
		subactions = self.last_actions[action]

		self.update_buttons([action],subactions)
		


	'''
		Updates the buttons to the currenlty available actions
	'''
	def update_buttons(self, actions, subactions):
		# Subaction menu
		if (len(subactions) > 0):	
			for i in range(self.num_btns):
				if (len(subactions) > i):
					self.buttons[i].config(text=subactions[i],state = "normal")
					self.buttons[i].config(command=partial(self.set_current_action,(actions[0],subactions[i])))
				else:
					self.buttons[i].config(text = '', state = "disabled")

		# Top level
		else:
			for i in range(self.num_btns):
				if (len(actions) > i):
					self.buttons[i].config(text=actions[i],state = "normal")
					self.buttons[i].config(command=partial(self.set_current_action,(actions[i],'')))
				else:
					self.buttons[i].config(text = '', state = "disabled")

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
	def set_current_action(self,action_tuple):
		if action_tuple[0] == 'build' and action_tuple[1] == '':
			self.update_sub_buttons(action_tuple[0])
			self.selected_action = ('move',[])
			return 

		self.selected_action = action_tuple

				




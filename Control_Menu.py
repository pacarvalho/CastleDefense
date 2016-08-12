'''
	Control Menu

	Setups buttons on the menu

	by Katie and Paulo
'''
import Tkinter as tk
from copy import deepcopy

class Control_Menu():
	def __init__(self):
		self.num_btns = 16
		self.buttons = [ tk.Button(text = "", command = "") for i in range(self.num_btns) ]
		self.last_actions = []

	def update_buttons(self, actions):
		# Only update the buttons if the actions differ from the last_actions
		if(set(actions) != set(self.last_actions)) :
			print "Buttons updated"
			self.last_actions = deepcopy(actions)
			
			for i in range(self.num_btns):
				if (len(actions) > i):
					self.buttons[i].config(text=actions[i])
				else:
					self.buttons[i].config(state = "disabled")

	def get_buttons(self):
		return self.buttons

	def get_num_btns(self):
		return self.num_btns
				




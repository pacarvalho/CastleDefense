'''
	Castle Defense Screen

	Displays the game screen

	By Katie and Paulo
'''

import Tkinter as tk
import math 

class Screen(tk.Tk):
	def __init__(self, *args, **kwargs):

		########## Important Variables ############
		# Current viewing location
		self.current_view_x = 0
		self.current_view_y = 10
		# Number cells in sight
		self.num_cells_view_x = 25
		self.num_cells_view_y = 17
		# Size of a cell in pixels
		self.cell_size = 32

		# Set up the drawing environment
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('Castle Defense - By Paulo and Katie')

		# Size of the screen
		self.screen_width = 1000
		self.screen_height = 800

		# Offset from screent to game
		self.screen_x_offset = self.screen_width/2 - (self.num_cells_view_x*self.cell_size)/2
		self.screen_y_offset = 7

		# Create a frame
		self.frame = tk.Frame(self, width=self.screen_width, height=self.screen_height)
		self.frame.pack()

		# Create the canvas for the game scene
		self.canvas = tk.Canvas(self.frame, width=self.num_cells_view_x*self.cell_size, height=self.num_cells_view_y*self.cell_size)
		self.canvas.place(x=self.screen_x_offset, y=self.screen_y_offset)

		# Create the canvas for the game menu
		self.menu_canvas = tk.Canvas(self.frame, width=self.num_cells_view_x*self.cell_size, height=self.num_cells_view_y*self.cell_size)
		self.menu_canvas.place(x=self.screen_x_offset, y=self.screen_y_offset + self.num_cells_view_y*self.cell_size)

		# Stores the lines for the attack animation
		self.attack_lines = []

	'''
		Sets the grid for the game
	'''
	def set_grid(self, grid):
		self.grid = grid

		# Keep references to all images that can appear on the screen
		self.canvas_image = [[self.canvas.create_image(x*self.cell_size, y*self.cell_size, anchor=tk.NW, image=self.grid.get_icon(x,y)) for y in range(self.num_cells_view_y)] for x in range(self.num_cells_view_x)]

	'''
		Returns the game grid
	'''
	def get_grid(self):
		return self.grid

	'''
		Sets the grid for the game
	'''
	def set_menu(self, menu):
		self.menu = menu

		# Keep references to all images that can appear on the screen
		self.menu_on_canvas = self.menu_canvas.create_image(0, 0, anchor=tk.NW, image=self.menu.get_icon())
		
		# Set initial menu text
		self.menu_text = self.menu_canvas.create_text(self.cell_size*9.5 + 13, self.cell_size/2 , anchor=tk.NW, text = self.menu.get_text({}), font=("Helvetica", 18) )
		
		# Set control menu
		self.control_menu = self.menu.get_control_menu()
		
		# Variables for configuring the display of the buttons
		init_x = self.screen_width/1.52 + 4
		init_y = self.num_cells_view_y*self.cell_size + 19
		btn_width = self.cell_size*1.8
		btn_height = self.cell_size

		# Place buttons on menu
		buttons = self.control_menu.get_buttons()
		num_btns = self.control_menu.get_num_btns()
		for i in range(num_btns):
			btn = buttons[i]
			btn.place(x = init_x + btn_width*(i%4) , y = init_y+btn_height*(i/4), width = btn_width, height = btn_height, anchor=tk.NW)

	'''
		Updates the game graphics with the correct icons
	'''
	def update_graphics(self):
		# Update Cell Icons
		count_x = -1
		for x in range(self.current_view_x,self.current_view_x+self.num_cells_view_x):
			count_x += 1
			count_y = -1
			for y in range(self.current_view_y,self.current_view_y+self.num_cells_view_y):
				count_y += 1
				self.canvas.itemconfig(self.canvas_image[count_x][count_y],image=self.grid.get_icon(x,y))

		# Erase the current lines
		for line in self.attack_lines:
			self.canvas.delete(line)
		self.attack_lines = []

		# Update the attack animation
		for attack_pair in self.grid.get_attack_pairs_list():
			# Get coordinates 
			attack_x = attack_pair[0] - self.current_view_x 
			attack_y = attack_pair[1] - self.current_view_y 
			attacked_x = attack_pair[2] - self.current_view_x 
			attacked_y = attack_pair[3] - self.current_view_y 

			# Check if both cells are within the viewing screen
			if (attack_x > self.num_cells_view_x):
				pass
			elif (attacked_x > self.num_cells_view_x):
		 		pass
		 	elif (attack_x < 0):
		 		pass
		 	elif (attacked_x < 0):
		 		pass
			elif (attack_y > self.num_cells_view_y):
				pass
			elif (attacked_y > self.num_cells_view_y):
				pass
			elif (attack_y < 0): 
				pass
			elif (attacked_y < 0):
				pass
			else: # All tests passed
				line = self.canvas.create_line(
							(attack_x+0.5)*self.cell_size,
							(attack_y+0.5)*self.cell_size,
							(attacked_x+0.5)*self.cell_size,
							(attacked_y+0.5)*self.cell_size)
				self.attack_lines += [line]


		# Update the menu
		self.update_menu()

		# Update the size of the screen in case the user has changed it
		self.screen_height = self.winfo_height()
		self.screen_width = self.winfo_width()

	'''
		Updates the game menu with the correct information
	'''
	def update_menu(self):
		###### Update Menu Text ###### 
		selected_cells = self.grid.get_selected()
		self.menu_canvas.itemconfig(self.menu_text, text=self.menu.get_text(selected_cells))

		###### Update Menu Buttons ######
		# Get available actions from the selected cells
		available_actions = self.menu.get_available_actions(selected_cells)
		self.control_menu.update(available_actions)

	'''
		Moves the screen in the given direction by x cells
	'''
	def move_screen(self, direction):
		if (direction == 'up'):
			self.current_view_y += 2
		elif (direction == 'down'):
			self.current_view_y -= 2
		elif (direction == 'left'):
			self.current_view_x += 2
		elif (direction == 'right'):
			self.current_view_x -= 2

		# Keep the view within bounds
		if (self.current_view_y < 0):
			self.current_view_y = 0
		if (self.current_view_y > self.grid.num_cells_y-self.num_cells_view_y):
			self.current_view_y = self.grid.num_cells_y-self.num_cells_view_y
		if (self.current_view_x < 0):
			self.current_view_x = 0
		if (self.current_view_x > self.grid.num_cells_x-self.num_cells_view_x):
			self.current_view_x = self.grid.num_cells_x-self.num_cells_view_x

	'''
		Gets the cell in the grid from the screen at mouseclick x,y
	'''
	def get_clicked_cell(self, click_x, click_y):
		# Calculate the cell based on the mouse click
		cell_in_view_X = int(math.floor((click_x)/self.cell_size))
		cell_in_view_Y = int(math.floor((click_y)/self.cell_size))

		cell_in_grid_X = cell_in_view_X + self.current_view_x 
		cell_in_grid_Y = cell_in_view_Y + self.current_view_y

		# If the click is out of bounds
		if (cell_in_grid_X < 0):
			cell_in_grid_X = 0
		if (cell_in_grid_X > self.current_view_x + self.num_cells_view_x-1):
			cell_in_grid_X = self.current_view_x + self.num_cells_view_x-1
		if (cell_in_grid_Y < 0):
			cell_in_grid_Y = 0
		if (cell_in_grid_Y > self.current_view_y + self.num_cells_view_y-1):
			cell_in_grid_Y = self.current_view_y + self.num_cells_view_y-1

		return (cell_in_grid_X,cell_in_grid_Y)	

	'''
		Returns the control menu
	'''	
	def get_control_menu(self):
		return self.menu.get_control_menu()




	














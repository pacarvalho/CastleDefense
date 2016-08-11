'''
	Castle Defense Grid

	Keeps the board information. 

	by Katie and Paulo
'''
from Queue import Queue
from copy import deepcopy

class Grid:
	def __init__(self, cells):
		# Array of cells (2D Array)
		self.cells = cells

		# Save the size of the grid
		self.num_cells_x, self.num_cells_y = len(cells), len(cells[0])

		# Saves list of currently selected cells
		self.selected_cells = {}

		# Keeps track of the current game cycle
		self.game_cycle = 0

		# 

	'''
		Gets the correct icons from the cells at a specific 
		x,y coordinate in the grid
	'''
	def get_icon(self,x,y):
		return self.cells[x][y].get_icon()

	'''
		Sets the cell at the given x,y location to be highlighted
	'''
	def set_selected(self,x,y):
		# Only deselect if the new clicked cell allowed itself to be selected
		selectConfirmed = self.cells[x][y].select()
		if (selectConfirmed and ((x,y) not in self.selected_cells.keys())):
			for cell in self.selected_cells.values():
				# Deselect previous cell if one exists
				# TODO: Implement this so it allows for selecting multiple objects
				cell.deselect()

		# Update the list of selected obejects
		self.get_selected()


	'''
		To be decided!!!
	'''
	def set_action(self,x,y):
		for coord,cell in self.selected_cells.items():
			path = self.calculate_path(coord[0],coord[1],x,y)

			cell.set_motion_path(path)


	'''
		Calculates a clear path between two locations on the grid
		A clear path is one that contains no "unpassable" entities
	'''
	def calculate_path(self,cur_x,cur_y,des_x,des_y):
		queue = Queue()

		# Add starting cell to the queue
		queue.put(((cur_x,cur_y),[(cur_x,cur_y)],[(cur_x,cur_y)]))

		return self.helper_calculate_path(des_x,des_y,queue)

	'''
		calculate_path helper
	'''
	def helper_calculate_path(self,des_x,des_y,queue):
		current = queue.get()
		current_node = current[0]
		current_path = current[1]
		checked_nodes = current[2]

		current_neighbors = self.get_neighbors(current_node[0],current_node[1])
		for n in current_neighbors:
			# If we have found the destination
			if ((n[0] == des_x) and (n[1] == des_y)):
				return current_path + [n]

			# If neightbor is not already in the path
			# If neighbor is passable
			if (n not in checked_nodes) and not (self.cells[n[0]][n[1]].get_blocking()):
				path = deepcopy(current_path) + [n]
				checked_nodes += [n]
				queue.put((n,path,checked_nodes))

		return self.helper_calculate_path(des_x,des_y,queue)

	'''
		Returns the direct neighbors of a cell

		Returns as coordinates
	'''
	def get_neighbors(self, cell_x, cell_y):
		# Keeps list of neighbbors
		neighbors = []
		for dx in range(-1,2):
			# Neighbors have to be within the grid
			if ((cell_x + dx)  < self.num_cells_x) and ((cell_x + dx) > 0):
				for dy in range(-1,2):
					# Do not include itself as a neighbor
					if not ((dx == 0) and (dy == 0)):
						if ((cell_y + dy)  < self.num_cells_y) and ((cell_y + dy) > 0):
							neighbors += [(cell_x + dx,cell_y + dy)]

		return neighbors

	'''
		Returns the cells that are currently selected

		Returns an array with the selected cells
	'''
	def get_selected(self):
		# Empty the list
		self.selected_cells = {}

		# Go through all cells and add to dictionary the selected ones
		for x in range(self.num_cells_x):
			for y in range(self.num_cells_y):
				if (self.cells[x][y].get_selected()):
					self.selected_cells[(x,y)] = self.cells[x][y]


	'''
		Updates the overall game state
	'''
	def update(self):

		# Get the list of currenlty selected cells
		self.get_selected()

		self.game_cycle += 1
		self.update_position()

	'''
		Moves all entities one motion step

		Polls the entity to determine if its time for it to move.
	'''
	def update_position(self):
		for cellArray in self.cells:
			for cell in cellArray:
				# Check if object should move
				next_pos = cell.get_destination(self.game_cycle)

				if len(next_pos) > 0:
					isBlocking = self.cells[next_pos[0]][next_pos[1]].get_blocking()
					if not isBlocking:
						self.cells[next_pos[0]][next_pos[1]].set_entity(cell.get_entity())
						cell.delete_entity()





		


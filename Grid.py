'''
	Castle Defense Grid

	Keeps the board information. 

	by Katie and Paulo
'''
from Queue import Queue
from copy import deepcopy

class Grid:
	def __init__(self, cells, teams):
		# List of teams
		self.teams = teams

		# Array of cells (2D Array)
		self.cells = cells

		# Save the size of the grid
		self.num_cells_x, self.num_cells_y = len(cells), len(cells[0])

		# Saves list of currently selected cells
		self.selected_cells = {}

		# Keeps track of the current game cycle
		self.game_cycle = 0

		# Coordinates of attack and attackee pairs (attacker_x,attacker_y,attackee_x,atttackee_y)
		self.attack_pairs_list = []

	'''
		Gets the correct icons from the cells at a specific 
		x,y coordinate in the grid
	'''
	def get_icon(self,x,y):
		return self.cells[x][y].get_icon()

	'''
		Sets the cell at the given x,y location to be highlighted

		isMultiple - When set to true does not deselect currently selected
	'''
	def set_selected(self,x,y,isMultiple):
		# Update the list of selected obejects
		self.get_selected()

		# Only deselect if the new clicked cell allowed itself to be selected
		selectConfirmed = self.cells[x][y].select()
		if (selectConfirmed and ((x,y) not in self.selected_cells.keys()) and not isMultiple):
			for cell in self.selected_cells.values():
				# Deselect previous cell if one exists
				# TODO: Implement this so it allows for selecting multiple objects
				cell.deselect()


	'''
		Executes an action with the currently selected cells

		Possible actions:
			'move' = Sets the entity on a path

		TODO: Add actions types!
	'''
	def set_action(self,x,y,action,player):

		# Update the list of selected obejects
		self.get_selected()

		# Check to whom the selected entities belong
		# Only allow actions on entitiy belonging to current player
		ownership = [cell.get_player().get_name() for cell in self.selected_cells.values()]
		if not ((len(set(ownership)) == 1) and ownership[0] == player.get_name()):
			return

		for coord,cell in self.selected_cells.items():
			path = self.calculate_path(coord[0],coord[1],x,y)
			
			cell.set_motion_path(path)

			# Set the action to be executed at the destination
			cell.set_destination_action(action)

 

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

		while not queue.empty():
			current = queue.get()
			current_node = current[0]
			current_path = current[1]
			checked_nodes = current[2]

			current_neighbors = self.get_neighbors(current_node[0],current_node[1],1)

			for n in current_neighbors:
				# If we have found the destination
				if ((n[0] == des_x) and (n[1] == des_y)):
					return current_path + [n]

				# If neighbor is not already in the path
				# If neighbor is passable
				if (n not in checked_nodes) and not (self.cells[n[0]][n[1]].get_blocking()):
					path = deepcopy(current_path) + [n]
					checked_nodes += [n]
					queue.put((n,path,checked_nodes))

		print "Error- No Path To Destination Was Found"
		return None


	'''
		Returns the direct neighbors of a cell

		Returns as coordinates
	'''
	def get_neighbors(self, cell_x, cell_y, radius):
		# Keeps list of neighbbors
		neighbors = []
		for dx in range(-radius,radius+1):
			# Neighbors have to be within the grid
			if ((cell_x + dx)  < self.num_cells_x) and ((cell_x + dx) > 0):
				for dy in range(-radius,radius+1):
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

		return self.selected_cells


	'''
		Updates the overall game state
	'''
	def update(self):

		# Get the list of currenlty selected cells
		self.get_selected()

		# Reset the attack Pair list
		self.attack_pairs_list = []

		self.game_cycle += 1
		self.update_action()

	def update_action(self):
		cur_x = -1 # Keeps track of the coordinate of the current cell 
		for cellArray in self.cells:
			cur_y = -1 # Keeps track of the coordinate of the current cell 
			cur_x += 1
			for cell in cellArray:
				cur_y += 1
				destination_action = cell.get_destination_action()
				player = cell.get_player()
				
				if destination_action[0] == 'move':
					self.update_position(cell)
				elif destination_action[0] == 'build':
					# We have arrived at the building location
					if (cell.get_remaining_steps_path() == 1):
						# Place building at last position in the path
						action_pos = cell.get_destination(self.game_cycle)

						# Protect against speed control from entity
						# TODO: Implement this without the speed control. So entity builds as soon as arriving on path
						if (len(action_pos) > 0):

							# Only build on top of non blocking objects
							if not (self.cells[action_pos[0]][action_pos[1]].get_blocking()):
								self.cells[action_pos[0]][action_pos[1]].set_entity_by_name(destination_action[1],player)

							# Reset the entity
							cell.reset_action()
					else:
						self.update_position(cell)
				elif destination_action[0] == 'attack':
					# Get neighbors within attack range
					enemy_in_range = False
					for neighbor in self.get_neighbors(cur_x,cur_y,cell.get_range()):
						player1 = self.cells[neighbor[0]][neighbor[1]].get_player()
						player2 = cell.get_player()
						# Check for alliance
						if not self.get_are_allies(player1,player2):
							enemy_in_range = True
							has_damaged = self.attack_helper(cell,self.cells[neighbor[0]][neighbor[1]])

							# Update the attacker list
							if has_damaged:
								self.attack_pairs_list += [tuple([cur_x,cur_y,neighbor[0],neighbor[1]])]

							break # Required to stop entity when reaching range
					if not enemy_in_range: # Move if no one is in range
						self.update_position(cell)

				else:
					self.update_position(cell)

	'''
		Attack Routine

		Reduces the HP of the attack receiver by the 
		Damage per Iteration of the attacker
	'''
	def attack_helper(self,attacker,attackee):
		damage = attacker.get_attack_damage(self.game_cycle)

		# Do the damage. Is the entity still alive?
		is_alive = attackee.deduct_hitpoints(damage)

		# Replace entity with default
		if not is_alive:
			attackee.delete_entity()

		# If damage was done return true
		if damage > 0:
			return True
		return False



	'''
		Moves all entities one motion step

		Polls the entity to determine if its time for it to move.
	'''
	def update_position(self, cell):
		# Check if object should move
		next_pos = cell.get_destination(self.game_cycle)

		if len(next_pos) > 0:
			isBlocking = self.cells[next_pos[0]][next_pos[1]].get_blocking()
			if not isBlocking:
				self.cells[next_pos[0]][next_pos[1]].set_entity(cell.get_entity())
				cell.delete_entity()

	'''
		Returns true if two players are in the same team
	'''
	def get_are_allies(self,player1,player2):
		# In case we are dealing with neutral player
		if (player1.get_name() == 'Neutral') or (player2.get_name() == 'Neutral'):
			return True
		for team in self.teams:
			if team.get_are_allies(player1,player2):
				return True
		return False

	'''
		Returns the attacker list pairs
	'''
	def get_attack_pairs_list(self):
		return self.attack_pairs_list












		


'''
	Castle Defense Main

	Runs the castle defense program

	By Paulo and Katie
'''

from Screen import Screen
from Grid import Grid
from KeyHandler import KeyHandler
from ManualMapCreator import ManualMapCreator

# Intantiate the screen
screen = Screen()

# Instantiate the key handler
keyHandler = KeyHandler(screen)

# Instantiate the grid with its default cells
manualMapCreator = ManualMapCreator()
grid = Grid(manualMapCreator.get_cell_array())
screen.set_grid(grid)


# Runs the game
def run():
	print "Im Running"

	screen.update_graphics()

	# Updates the screen
	screen.update()

	# Calls this function periodically
	screen.after(5000, lambda: run())	

# Calls the run method for the first time
run()

# Main game loop
screen.mainloop()
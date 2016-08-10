'''
	Castle Defense Main

	Runs the castle defense program

	By Paulo and Katie
'''

from Screen import Screen
from Grid import Grid
from Cell import Cell
from KeyHandler import KeyHandler
from entities.Tree import Tree


# Intantiate the screen
screen = Screen()

# Instantiate the key handler
keyHandler = KeyHandler(screen)

# Instantiate the grid with its default cells
cellArray = [[Cell() for x in range(100)] for y in range(100)]
grid = Grid(cellArray)
screen.set_grid(grid)

for i in range(100):
	cellArray[i][9].set_entity(Tree())

for i in range(100):
	cellArray[9][i].set_entity(Tree())


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
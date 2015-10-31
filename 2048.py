"""
Clone of 2048 game.
"""
import random

import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    merge lines
    """
    
    new_line = []
    
    for item in line:
        if item != 0:
            new_line.append(item)
    
    
    doubled_line = []
    
    
    for index in range(len(new_line)):
        
        if index < len(new_line)-1:
            if new_line[index] == new_line[index + 1]:
                
                doubled_line.append(new_line[index]*2)

                new_line[index + 1] = "X"
            elif new_line[index] != "X":
                doubled_line.append(new_line[index])
        else:
            if new_line[index] != "X":
                doubled_line.append(new_line[index])

   
    add_zeros = (len(line) - len(doubled_line)) * [0]
    
    
    doubled_line += add_zeros
    
    return doubled_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._width = grid_width
        self._height = grid_height
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._board = [[0 for dummy_idx in range(self._width)]
                           for dummy_idx in range(self._height)]
        self.new_tile()
        self.new_tile()
        
        
        self._idx = {}
        #generate indices
        def gen_idx( grid_height, grid_width):
                """
                generate index dict
                """
                left_idx = []
                for dummy_idx in range(grid_height):
                    left_idx.append((dummy_idx, 0))

                up_idx = []
                for dummy_idx in range(grid_width):
                    up_idx.append((0, dummy_idx))

                down_idx = []
                for dummy_idx in range(grid_width):
                    down_idx.append((grid_height-1, dummy_idx))

                right_idx = []
                for dummy_idx in range(grid_height):
                    right_idx.append((dummy_idx, grid_width-1))



                self._idx[LEFT] = left_idx
                self._idx[RIGHT] = right_idx
                self._idx[UP] = up_idx
                self._idx[DOWN] = down_idx
        gen_idx(self._height, self._width)        
        #print "indices ",self.indices
        for item in self._board:
            print item
        print 
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._board)

    def get_grid_height(self):
        """
        Get the height of the the_board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the the_board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        
        the_flag = []
        #this is a helper function 
        def produce_line(start_cell, direction, num_steps):
            """
            Generate each line
            """
            
            the_line = []
            the_cells = []
            for step in range(num_steps):

                row = start_cell[0] + direction[0] * step
                col = start_cell[1] + direction[1] * step
                
                the_cells.append((row, col))
                cell_val = self._board[row][col]

                the_line.append(cell_val)
            #print "before ", the_line
            #print "after ", merge(the_line)
            after =  merge(the_line)
            
            for item in range(len(the_cells)):
                self.set_tile(the_cells[item][0], the_cells[item][1], after[item])
                if the_line[item] != after[item]:
                    the_flag.append("True")
                
                    
                    
            
            
        if direction == UP or direction == DOWN: 
            for item in self._idx[direction]:
                produce_line(item, OFFSETS[direction], self._height)
        else:
            for item in self._idx[direction]:
                produce_line(item, OFFSETS[direction], self._width)
                
        print "True" in the_flag       
        if "True" in the_flag:
            
            self.new_tile()
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_width = random.randrange(self._width)
        random_height = random.randrange(self._height)
        tile_val = 0
        determine_possibility = random.randrange(100)
        #print "possibility ", determine_possibility
        
        if self._board[random_height][random_width] == 0:
            if determine_possibility < 90:
                tile_val = 2
            else:
                tile_val = 4
                
            self.set_tile(random_height, random_width, tile_val)
        else:
            self.new_tile()
                
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._board[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


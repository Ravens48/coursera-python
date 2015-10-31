"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
            
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        self._human_list = []
        self._zombie_list = []
        self.__init__(self.get_grid_height(), self.get_grid_width())
            
        
        
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        
        """
        self._zombie_list.append((row, col))
        
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)     
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for item in self._zombie_list:
            
            yield item
        

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for item in self._human_list:
            yield item
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        width = self.get_grid_width()
        height = self.get_grid_height()
        visited = poc_grid.Grid(height, width)
        distance_field = [[(width * height) for dummy_idx in range(width)] for dummy_idx in range(height)] 
        boundary = poc_queue.Queue()
        
        if entity_type == 7:
            entity = self._zombie_list
        else:
            entity = self._human_list
        
        for item in entity:
            boundary.enqueue(item)
            distance_field[item[0]][item[1]] = 0
            visited.set_full(item[0],item[1]) 
            
        while boundary:
            current_cell = boundary.dequeue()
            neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]) and self.is_empty(neighbor[0],neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    boundary.enqueue(neighbor)
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
                    
        for item in distance_field:
            print item
        print    
        print visited
        return distance_field
        
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        
        for item in zombie_distance_field:
            print item
        obstacle = self.get_grid_width() * self.get_grid_height()
        new_list = []
        for item in self._human_list:
            values = {}
            neighbors = self.eight_neighbors(item[0], item[1])
            for neighbor in neighbors:
                print neighbor
                if zombie_distance_field[neighbor[0]][neighbor[1]] < obstacle:
                    values[zombie_distance_field[neighbor[0]][neighbor[1]]] = neighbor
        
            move_to = values[max(values)]
            new_list.append(move_to)
        print values 
        self._human_list = new_list
        print self._human_list
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for item in human_distance_field:
            print item
        obstacle = self.get_grid_width() * self.get_grid_height()
        new_list = []
        for item in self._zombie_list:
            values = {}
            neighbors = self.four_neighbors(item[0], item[1])
            for neighbor in neighbors:
                print neighbor
                
                if human_distance_field[neighbor[0]][neighbor[1]] < obstacle:
                    values[human_distance_field[neighbor[0]][neighbor[1]]] = neighbor
        
            move_to = values[min(values)]
            if human_distance_field[item[0]][item[1]] > min(values):
                new_list.append(move_to)
            else:
                new_list.append(item)
        print values 
        self._zombie_list = new_list
        print self._zombie_list

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))

#n = Apocalypse(20, 30, [(4, 15), (5, 15), (6, 15), (7, 15), (8, 15), (9, 15), (10, 15), (11, 15), (12, 15), (13, 15), (14, 15), (15, 15), (15, 14), (15, 13), (15, 12), (15, 11), (15, 10)], [(12, 12), (7, 12)], [])

#n.compute_distance_field(ZOMBIE) 

#obj = Apocalypse(3, 3, [(1, 1), (1, 2)], [(2, 2)], [(0, 2)])
#dist = [[2, 1, 0], [3, 9, 9], [4, 5, 6]]
#obj.move_zombies(dist)


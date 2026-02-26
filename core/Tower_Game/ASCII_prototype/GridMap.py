from random import choice, randint
from Map_db import *

class Grid():
    def __init__(self, x_axis:int, y_axis:int):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.grid_id = create_grid_id(x_axis, y_axis)
        
        self.grid = fill_grid(self.grid_id, x_axis, y_axis)


# Grid id creation (Which tile is in each position of the grid)
def create_grid_id(x_axis, y_axis):
    grid_id = []
    for x in range(x_axis):
        grid_line = []
        for y in range(y_axis):
            #grid_line.append(choice(list(tiles.values())))
            grid_line.append(all_tiles["floor"])
        grid_id.append(grid_line)
    return grid_id    


# Grid symbols disposition (How the grid will be displayed)
def fill_grid(grid_id, x_axis, y_axis):
    grid = []
    for x in range(x_axis):
        grid_line = []
        for y in range(y_axis): 
            grid_line.append(grid_id[x][y].symbol)
            # grid_line.append("-  ")
            
            # Sobreposition of tiles (Borders must be walls)
            if x == 0 or y == 0 or y == y_axis - 1 or x == x_axis - 1:
                if x == 0 and y < y_axis - 1 or x == x_axis - 1 and y < y_axis - 1:
                    grid_line[y] = "███" # Wall
                else:
                    grid_line[y] = "█  " # Wall
        
        grid.append(grid_line)
    return grid 

class Map(Grid):
    
    def __init__(self, x_axis:int, y_axis:int, biome:str="dungeon"):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.biome = biomes[biome]
        self.map = None

    def generate_map(self):
        self.map = fill_grid(create_grid_id(self.x_axis, self.y_axis), self.x_axis, self.y_axis)    
    
    # generate terrain from top-left to bottom-right from a random point inside the map
    def generate_terrain(width:int, height:int, num_areas:int, tile:Tile, irreguar:bool=True):
        coordinates = [randint(1, x_axis-2), randint(1, y_axis-2)] # Example: [3, 3]; from 0 to 10
    
        if irregular:
            pass
        else:
            for i in range():
                pass
        pass

        

    def print_map(self):
        if not self.map == None:
            x = self.x_axis
            y = self.y_axis
            print(f"[{x}, {y}]\n")
            centralizer = "                    " # 6 'tabs' to the right
            for i in range(x):
                line = centralizer
                for j in range(y):
                    line += self.map[i][j]
                print(line)

            


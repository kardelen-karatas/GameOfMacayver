class LabItem:
        
    """
    Item in the labyrinth. The item is placed on the tile of the labyrinth with coordinates given.    
    """

    def __init__(self, item_type, x, y):
        self.x = x
        self.y = y
        self.item_type = item_type

    def __str__(self):
        return "{}".format(self.item_type)#, self.x, self.y)

class Player(LabItem):

    def __init__(self,item_type = 'player', x = 0, y= 0):
        """
        Player of the game, inherits the LabItem class. He is initialized on the coorditanes x = 0 and y = 0.
        """
        LabItem.__init__(self, item_type, x, y)
        self.counter = 0
        self.lives = 1

    def move_right(self, tiles):
        """
        Move the player to the right tile
        Args:
            tiles (list): canvas of the labyrinth
        """
        self.x += 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y][self.x - 1].remove_item()        

    def move_left(self, tiles):
        """
        Move the player to the left tile
        Args:
            tiles (list): canvas of the labyrinth
        """
        self.x -= 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y][self.x + 1].remove_item()
    
    def move_down(self, tiles):
        """
        Move the player to the tile below
        Args:
            tiles (list): canvas of the labyrinth
        """
        self.y += 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y - 1][self.x].remove_item()               

    def move_up(self, tiles):
        """
        Move the player to the tile above
        Args:
            tiles (list): canvas of the labyrinth
        """
        self.y -= 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y + 1][self.x].remove_item()
              
    def pick_up(self, tile):
        """
        Pick up an item and increment the counter
        Args:
            tile (Tile): tile of the canvas
        """
        if tile.lab_item != None and tile.lab_item.item_type == 'object':
            self.counter += 1


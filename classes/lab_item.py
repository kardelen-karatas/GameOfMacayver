class LabItem:
    def __init__(self, item_type = 'object', x = 0, y = 0):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.counter = 0



    def move_right(self, tiles):
        self.x += 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y][self.x - 1].remove_item()        

    def move_left(self, tiles):
        self.x -= 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y][self.x + 1].remove_item()
    
    def move_down(self, tiles):
        self.y += 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y - 1][self.x].remove_item()               

    def move_up(self, tiles):
        self.y -= 1
        tiles[self.y][self.x].add_lab_item(self)
        tiles[self.y + 1][self.x].remove_item()
              
    def pick_up(self, tile):
        if tile.lab_item != None and tile.lab_item.item_type == 'object':
            self.counter += 1

    def __str__(self):
        return "{}".format(self.item_type)#, self.x, self.y)


# class Player(LabItem):
#     def __init__(self, type = 'guard'):
#         super().__init__()

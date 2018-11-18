class LabItem:
    def __init__(self, item_type = 'player', x = 0, y = 0):
        self.x = x
        self.y = y
        self.item_type = item_type
        self.counter = 0

    def move_right(self):
        self.x += 1
    
    def move_left(self):
        self.x -= 1
    
    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

    def pick_up(self, tile):
        if tile.lab_item != None:
            self.counter += 1

    def __str__(self):
        return "{}".format(self.item_type)#, self.x, self.y)


# class Guard(LabItem):
#     def __init__(self, type = 'guard'):
#         super().__init__()

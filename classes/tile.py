class Tile:
    def __init__(self, tile_type='floor'):
        self.tile_type = tile_type
        self.lab_item = None
        self.counter = 0

    def add_lab_item(self, item):
        self.lab_item  = item

    def remove_item(self):
        self.counter +=1
        self.lab_item  = None

    def __str__(self):
        return "{}:{}".format(self.tile_type,self.lab_item)


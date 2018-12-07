class Tile:

    """
    Tile in the canvas of the labyrinth. It is possible to add items on a tile.
    By default any item placed on the tile.
    """

    def __init__(self, tile_type='floor'):
        """Args: tile_type (str): type of tile (default floor)"""
        self.tile_type = tile_type
        self.lab_item = None

    def add_lab_item(self, item):
        """
        Args:
            item (LabItem): item of the labyrinth to be added.
        """
        self.lab_item = item

    def remove_item(self):
        self.lab_item = None

    def __str__(self):
        return "{}:{}".format(self.tile_type, self.lab_item)

from os.path import abspath, dirname, join


class Config():

    GAME_BASEPATH = dirname(abspath(__file__))
    IMAGES_BASEPATH = join(GAME_BASEPATH, 'images')
    MAPS_BASEPATH = join(GAME_BASEPATH, 'maps')

    @classmethod
    def get_image_path(cls, image):
        return join(cls.IMAGES_BASEPATH, image)

    @classmethod
    def get_map_path(cls, pattern):
        return join(cls.IMAGES_BASEPATH, pattern)

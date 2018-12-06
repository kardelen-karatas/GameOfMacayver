from os.path import abspath, dirname, join


class Config:

    GAME_BASEPATH = dirname(abspath(__file__))
    IMAGES_BASEPATH = join(GAME_BASEPATH, 'images')
    PATTERNS_BASEPATH = join(GAME_BASEPATH, 'patterns')

    @classmethod
    def get_image_path(cls, image):
        return join(cls.IMAGES_BASEPATH, image)

    @classmethod
    def get_pattern_path(cls, pattern):
        return join(cls.PATTERNS_BASEPATH, pattern)

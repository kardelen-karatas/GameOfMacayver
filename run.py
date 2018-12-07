import argparse
from classes.game import Game


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", nargs='?', default='pattern_file',
                        help="This file contains the pattern of the labyrinth."
                             "File must have 15 rows and 15 columns."
                             "The pattern of the labyrinth is composed"
                             "of the 'F' and 'W'. 'F' represents the floor,"
                             "'W' represents water. The position of the"
                             "guardian, represented by 'G', must also be"
                             "proposed in the pattern."
                             "It contains only one guardian"
                             "and it should be placed on the "
                             "bottom right corner, like lab[14][14].")
    arguments = parser.parse_args()
    p_file = arguments.pattern

    g = Game(p_file)
    g.game_loop()


if __name__ == '__main__':
    main()

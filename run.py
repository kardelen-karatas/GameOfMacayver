import argparse
from classes.game import Game


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "pattern",
        nargs='?',
        default='pattern_file',
        help="this file contains the pattern of the labyrinth. File must have 15 rows and 15 columns. The pattern of the labyrinth is composed of the 'F' and 'W'. 'F' represents the floor, 'W' represents water. The position of the guardian, represented by 'G', must also be proposed in the pattern. The labyrinth contains only one guardian and it should be placed at 15th column and on the 15th line (on the bottom right) of the labyrinthe, like lab[14][14].",
    )
    arguments = parser.parse_args()
    p_file = arguments.pattern

    g = Game(p_file)
    g.run()


if __name__ == '__main__':
    main()

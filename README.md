## The Hungry Octopus Game

The game consists of a tile maze with a player (an octopus) and 2 items (plankton) randomly distributed in the labyrinth. The labyrinth is composed of the floor and water. The player can only move on the floor with up, down, right and left with the keyboard buttons. The game ends when the player picks up all the items and arrives at the door. 

**ATTENTION** If the player arrives in front of the door without picking up all the items, **he loses the game**  

### Prerequisites

To run this project on your computer, you must install python3 and pygame version 1.9.4. It is also suggested to use the virtual environment.   

### Installing

To install all python dependencies with vitual environment:
```
pip install -r requirements.txt
```

### Usage

To run the game: 

```
python run.py
```

You can also change the labyrinth pattern by using a text file that contains another pattern. The labyrinth pattern must have 15 rows and 15 columns. The pattern is composed of the `F` and `W`. `F` represents the floor, `W` represents the water. The position of the guardian, represented by `G`, must also be proposed in the pattern. The labyrinth contains only one guardian and it should be placed at 15th column and on the 15th line (on the bottom right corner) of the labyrinth, like `labyrinth[14][14]`.  

To run the game with another pattern file: 
```
python run.py PATTERN_FILE_PATH
```

### Tutorials for Pygame (inspired by)
* http://usingpython.com/pygame-tilepatterns/
* Interface Graphique Pygame pour Python, OpenClassrooms


### Built With
* VSCode

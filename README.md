# Connect Four - Python

This is Connect Four game implemented in Python. THe game allows players to play against each other or against an AI. The AI can either be a basic random AI or a harder AI that includes a time limit for player moves.

---

### Features

- Player vs Player
- Player vs AI: Play against a simple AI that randomly selects a valid column
- Play vs Harder AI: Play against a more challenging AI where the player has 5 seconds to make a move. If the palyer doesn't make a move in time, the game ends.

---

### Installation

1. Clone or download the repository
2. Ensure Python 3.x is installed on your mahcine
3. Run: ` python main.py`

---

### Gameplay

1. After starting the game, choose the desired game mode by entering the corresponding number (1, 2, or 3).
2. For Player vs Player, two players will alternately choose columns.
3. For Player vs AI, the player will input their column choice, and the AI will make its move automatically.
4. For Player vs Harder AI, the player must input their column within 5 seconds. If the player doesn’t input a valid column in time, the game ends.
5. Enter a column (1-7) to drop a piece in the corresponding column of the grid.
6. Enter 0 to exit the game at any time.

---

## Future improvements

- Enhance AI using advanced strategies like Minimax or Monte Carlo Tree Search.
- Implement a save/load feature for game state persistance.
- Add a Graphical User Interface

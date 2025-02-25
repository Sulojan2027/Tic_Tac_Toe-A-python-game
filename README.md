# Tic Tac Toe (Python)

A simple **Tic Tac Toe** game implemented in Python. The game allows a human player to compete against a computer opponent.

## Features
- **Human vs Computer** gameplay.
- **Random Move Selection** for the computer.
- **Auto-detection of Wins, Losses, and Draws**.
- **Command-line based interface**.

## How to Play
- The game starts with the computer placing an `X` in the center of the board.
- The player is prompted to enter a move by selecting a number (1-9).
- The game board updates after each move.
- The first player to align three symbols (`X` or `O`) **horizontally, vertically, or diagonally** wins.
- If all spaces are filled without a winner, the game declares a draw.

## Game Board Layout
Each number represents a possible move location:
```
+-------+-------+-------+
|   1   |   2   |   3   |
+-------+-------+-------+
|   4   |   5   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+
```
- Enter a number to place your **O** in that spot.

## Installation & Running
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/tic-tac-toe-python.git
   cd tic-tac-toe-python
   ```
2. **Run the game:**
   ```sh
   python tic_tac_toe.py
   ```

## Code Overview
- `display_board(board)`: Prints the game board.
- `enter_move(board)`: Accepts the player's move.
- `make_list_of_free_fields(board)`: Returns available moves.
- `victory_for(board, sign)`: Checks if a player has won.
- `draw_move(board)`: AI places a random move.

## Example Gameplay
```
Enter your move (1-9): 1
+-------+-------+-------+
|   O   |   2   |   3   |
+-------+-------+-------+
|   4   |   X   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+
Computer's turn...
```

## Future Improvements
- Improve AI with **Minimax Algorithm** for strategic moves.
- Add **Graphical User Interface (GUI)** using Tkinter or Pygame.
- Implement a **two-player mode**.

## Contributing
Feel free to fork this repository, improve the game, and submit a pull request!

---
Enjoy the game! 🎮
Tic-Tac-Toeeeeeeeeeeeeeeeeee

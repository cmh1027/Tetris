# Opensource Assignment

## Tetris
The classic game of tetris implemented in pygame
As level goes up, eccentric blocks will be appear and speed will rapidly increase!

### implementation
There are 4 difficulties (Unrelated to capitalization)
* Easy : python main.py easy , python main.py // 3 Items each, Start at Level 1
* Normal : python main.py normal // 2 Items each, Start at Level 5
* Hard : python main.py hard // 1 Items each, Start at Level 10
* Hell : python main.py hell // No items, Start at Level 15

### Files
* Block.py : Control blocks and check if a row is full
* Board.py : Check the entire board for block movement
* constants.py : Constants
* main.py : General Controller

#### Controls
* Left: Move left
* Right: Move right
* DOWN: Drop faster
* SPACE: Drop to bottom instantly
* Enter: Restart after game ends
* R: Reset game
* G: Hold block
* H: Hold block
* S: Rotate block
* P: Pause game
* ESC: Quit Window
* 1: Item1 - Slow the block
* 2: Item2 - Block removal 
* 3: Item3 - Block Bomb

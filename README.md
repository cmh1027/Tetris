# Opensource Assignment

## Tetris
The classic game of tetris implemented in pygame
As level goes up, eccentric blocks will be appear and speed will rapidly increase!
You can hold 2 blocks unlike other tetris games!

### implementation
There are 4 difficulties (Unrelated to capitalization)
* Easy : python main.py easy , python main.py // 3 Items each, Start at Level 1
* Normal : python main.py normal // 2 Items each, Start at Level 5
* Hard : python main.py hard // 1 Items each, Start at Level 10
* Hell : python main.py hell // No items, Start at Level 15

Other invalid argv will be regarded as easy mode

### Files
* Block.py : Control blocks and check if a row is full
* Board.py : Check the entire board for block movement
* constants.py : Constants
* main.py : General Controller
* easy.mp3 : bgm for easy mode (Tetris(Tengen) - Bradinsky)
* normal.mp3 : bgm for normal mode (Tetris(Tengen) - Troika)
* hard.mp3 : bgm for hard mode (Dungeon and Fighter - Luke battle theme)
* hell.mp3 : bgm for hell mode (The Matrix  Soundtrack- Juno Reactor Vs Don Davis - Navras)
* blockfull.wav : soundeffect when row is full
* bomb.wav : soundeffect for bomb item
* slow.wav : soundeffect for slow item
* fast.wav : soundeffect when effect of slow item ends
* skip.wav : soundeffect for skip item
* levelup.wav : soundeffect for levelup
* over.wav : soundeffect for gameover

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
* 1: Item1 - Slow the block (Double a time interval for 5 phases)
* 2: Item2 - Block removal (Skip the block)
* 3: Item3 - Block Bomb (Remove blocks around the bomb block - 5x5)

#### Blocks
* 4 pieces blocks
* 5 pieces blocks
* 6 pieces blocks
* Bomb block(Red color)
* Column Bomb block(skyblue color) - destroy a column blocks where it's dropped

#### Strategy
1. You can hold 2 bomb blocks
2. Be careful when you use bomb blocks. It can ruin your block disposition.
3. Difficulty depends on rows you destoryed. If you want to high score, try to destroy rows simultaneously as many as you can! It will give you more score.
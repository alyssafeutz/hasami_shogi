# hasami_shogi
Simulation of Hasami Shogi board game using Python

Hasami Shogi Rules: 

The game is played on a traditional shogi board (which happend to be the same as a chess board) of nine by nine squares.  

Each player starts out with nine pieces- in this case, there is a player with nine black pieces and another player with nine red pieces.

First player to move is the player with black pieces.  After one move, play switches to the other player.

A player can make a valid move by moving their piece any number of blank spaces vertically or horizontally.  The piece cannot jump over another piece.

The goal is to capture 8 of the opponent pieces.  

A capture can be done in one of two ways.  If an opponent's piece is in a corner square, the piece is captured if it is surrounded on three sides by "enemy" pieces. 

A capture can also be made if an opponent's piece is sandwiched my "enemy" pieces on both sides vertically, or both sides horizontally.  

A player can move a piece into a sandwiched position without being captured; the capture can only happen if the enemy is the one to move their piece into a surrounding position.  

The first player to capture eight enemy pieces wins.  




# 348. Design Tic-Tac-Toe

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [Valid Tic-Tac-Toe State](valid-tic-tac-toe-state.md)

## Problem:

<p>Design a Tic-tac-toe game that is played between two players on a <i>n</i> x <i>n</i> grid.
</p>

<p>You may assume the following rules:
<ol>
<li>A move is guaranteed to be valid and is placed on an empty block.</li>
<li>Once a winning condition is reached, no more moves is allowed.</li>
<li>A player who succeeds in placing <i>n</i> of their marks in a horizontal, vertical, or diagonal row wins the game.</li>
</ol>
</p>

<p><b>Example:</b><br />
<pre>
Given <i>n</i> = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
</pre>
</p>

<p><b>Follow up:</b><br />
Could you do better than O(<i>n</i><sup>2</sup>) per <code>move()</code> operation?
</p>
## Solutions:

```c++
class TicTacToe {
public:
    /** Initialize your data structure here. */
    TicTacToe(int n) {
        this->n = n;
        rowCount[0].resize(n);
        rowCount[1].resize(n);
        colCount[0].resize(n);
        colCount[1].resize(n);
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        if (++rowCount[player - 1][row] == n)   return player;
        if (++colCount[player - 1][col] == n)   return player;
        if (row == col) {
            if(++diagonalCount[player - 1] == n) return player;
        }
        if (row + col == n - 1) {
            if (++antiDiagonalCount[player - 1] == n)   return player;
        }
        
        return 0;
    }
private:
    int n;
    vector<int> rowCount[2];
    vector<int> colCount[2];
    int diagonalCount[2] {0};
    int antiDiagonalCount[2] {0};
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
```

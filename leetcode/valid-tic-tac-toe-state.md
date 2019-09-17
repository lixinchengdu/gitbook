# 810. Valid Tic-Tac-Toe State

* *Difficulty: Medium*

* *Topics: Math, Recursion*

* *Similar Questions:*

  * [Design Tic-Tac-Toe](design-tic-tac-toe.md)

## Problem:

<p>A Tic-Tac-Toe board is given as a string array <code>board</code>. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.</p>

<p>The <code>board</code> is a 3 x 3 array, and consists of characters <code>&quot; &quot;</code>, <code>&quot;X&quot;</code>, and <code>&quot;O&quot;</code>.&nbsp; The &quot; &quot; character represents an empty square.</p>

<p>Here are the rules of Tic-Tac-Toe:</p>

<ul>
	<li>Players take turns placing characters into empty squares (&quot; &quot;).</li>
	<li>The first player always places &quot;X&quot; characters, while the second player always places &quot;O&quot; characters.</li>
	<li>&quot;X&quot; and &quot;O&quot; characters are always placed into empty squares, never filled ones.</li>
	<li>The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.</li>
	<li>The game also ends if all squares are non-empty.</li>
	<li>No more moves can be played if the game is over.</li>
</ul>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> board = [&quot;O&nbsp; &quot;, &quot;&nbsp; &nbsp;&quot;, &quot;&nbsp; &nbsp;&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> The first player always plays &quot;X&quot;.

<strong>Example 2:</strong>
<strong>Input:</strong> board = [&quot;XOX&quot;, &quot; X &quot;, &quot;   &quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong> Players take turns making moves.

<strong>Example 3:</strong>
<strong>Input:</strong> board = [&quot;XXX&quot;, &quot;   &quot;, &quot;OOO&quot;]
<strong>Output:</strong> false

<strong>Example 4:</strong>
<strong>Input:</strong> board = [&quot;XOX&quot;, &quot;O O&quot;, &quot;XOX&quot;]
<strong>Output:</strong> true
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>board</code> is a length-3 array of strings, where each string <code>board[i]</code> has length 3.</li>
	<li>Each <code>board[i][j]</code> is a character in the set <code>{&quot; &quot;, &quot;X&quot;, &quot;O&quot;}</code>.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    bool validTicTacToe(vector<string>& board) {
        const int n = 3;
        int rowCount[2][n] = {0};
        int colCount[2][n] = {0};
        int diag[2] = {0};
        int antiDiag[2] = {0};
        int count[2] = {0}; // count!!!
        bool rowWin = false;
        bool colWin = false;
        bool winner[2] = {false};
        
        
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == ' ') continue;
                int player = (board[i][j] == 'X' ? 0 : 1);
                ++count[player];
                if (++rowCount[player][i] == n) {
                    if (rowWin)    return false;
                    else rowWin = true;
                    winner[player] = true;
                }
                
                if (++colCount[player][j] == n) {
                    if (colWin)    return false;
                    else colWin = true;
                    winner[player] = true;
                }
                
                if (i == j) {
                    if (++diag[player] == n) {
                        winner[player] = true;
                    }
                }
                
                if (i + j == n -1) {
                    if (++antiDiag[player] == n) {
                        winner[player] = true;
                    }
                }
                
            }
        }
        
        if (winner[0] == true) {
            return count[0] == count[1] + 1;
        } else if (winner[1] == true) {
            return count[0] == count[1];
        } else {
            return count[0] == count[1] || count[0] == count[1] + 1;
        }
    }
};
```

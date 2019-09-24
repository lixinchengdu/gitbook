# 419. Battleships in a Board

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

Given an 2D board, count how many battleships are in it. The battleships are represented with <code>'X'</code>s, empty slots are represented with <code>'.'</code>s. You may assume the following rules:

<ul>
<li>You receive a valid board, made of only battleships or empty slots.</li>
<li>Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape <code>1xN</code> (1 row, N columns) or <code>Nx1</code> (N rows, 1 column), where N can be of any size.</li>
<li>At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.</li>
</ul>

<p><b>Example:</b><br />
<pre>X..X
...X
...X
</pre>
In the above board there are 2 battleships.

<p><b>Invalid Example:</b><br />
<pre>...X
XXXX
...X
</pre>
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
<p></p>
<p><b>Follow up:</b><br>Could you do it in <b>one-pass</b>, using only <b>O(1) extra memory</b> and <b>without modifying</b> the value of the board?</p>
## Solutions:

```c++
class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int count = 0;
        int m = board.size();
        if (m == 0) return 0;
        int n = board[0].size();
        if (n == 0) return 0;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'X' && (j - 1 < 0 || board[i][j-1] != 'X') && ( i - 1 < 0 || board[i-1][j] != 'X'))  ++count;
            }
        }
        
        return count;
    }
};
```

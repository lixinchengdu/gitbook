# 130. Surrounded Regions

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search, Union Find*

* *Similar Questions:*

  * [Number of Islands](number-of-islands.md)

  * [Walls and Gates](walls-and-gates.md)

## Problem:

<p>Given a 2D board containing <code>&#39;X&#39;</code> and <code>&#39;O&#39;</code> (<strong>the letter O</strong>), capture all regions surrounded by <code>&#39;X&#39;</code>.</p>

<p>A region is captured by flipping all <code>&#39;O&#39;</code>s into <code>&#39;X&#39;</code>s in that surrounded region.</p>

<p><strong>Example:</strong></p>

<pre>
X X X X
X O O X
X X O X
X O X X
</pre>

<p>After running your function, the board should be:</p>

<pre>
X X X X
X X X X
X X X X
X O X X
</pre>

<p><strong>Explanation:</strong></p>

<p>Surrounded regions shouldn&rsquo;t be on the border, which means that any <code>&#39;O&#39;</code>&nbsp;on the border of the board are not flipped to <code>&#39;X&#39;</code>. Any <code>&#39;O&#39;</code>&nbsp;that is not on the border and it is not connected to an <code>&#39;O&#39;</code>&nbsp;on the border will be flipped to <code>&#39;X&#39;</code>. Two cells are connected if they are adjacent cells connected horizontally or vertically.</p>

## Solutions:

```c++
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size();
        if (m == 0) return;
        int n = board[0].size();
        if (n == 0) return;
        
        vector<vector<bool>> visited(m, vector<bool> (n, false));
        
        for (int i = 0; i < m; ++i) {
            dfs(board, i, 0, visited);
            dfs(board, i, n - 1, visited);
        }
        
        for (int j = 0; j < n; ++j) {
            dfs(board, 0, j, visited);
            dfs(board, m - 1, j, visited);
        }
        
        for (int i = 1; i < m - 1; ++i) {
            for (int j = 1; j < n - 1; ++j) {
                if (board[i][j] == 'O' && !visited[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }
    
    void dfs(vector<vector<char>>& board, int row, int col, vector<vector<bool>>& visited) {
        int m = board.size();
        int n = board[0].size();
        if (row < 0 || row >= m || col < 0 || col >= n || board[row][col] == 'X' || visited[row][col])    return;
        visited[row][col] = true;
        dfs(board, row + 1, col, visited);
        dfs(board, row - 1, col, visited);
        dfs(board, row, col - 1, visited);
        dfs(board, row, col + 1, visited);
    }
};
```

# 529. Minesweeper

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>Let&#39;s play the minesweeper game (<a href="https://en.wikipedia.org/wiki/Minesweeper_(video_game)">Wikipedia</a>, <a href="http://minesweeperonline.com">online game</a>)!</p>

<p>You are given a 2D char matrix representing the game board. <b>&#39;M&#39;</b> represents an <b>unrevealed</b> mine, <b>&#39;E&#39;</b> represents an <b>unrevealed</b> empty square, <b>&#39;B&#39;</b> represents a <b>revealed</b> blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, <b>digit</b> (&#39;1&#39; to &#39;8&#39;) represents how many mines are adjacent to this <b>revealed</b> square, and finally <b>&#39;X&#39;</b> represents a <b>revealed</b> mine.</p>

<p>Now given the next click position (row and column indices) among all the <b>unrevealed</b> squares (&#39;M&#39; or &#39;E&#39;), return the board after revealing this position according to the following rules:</p>

<ol>
	<li>If a mine (&#39;M&#39;) is revealed, then the game is over - change it to <b>&#39;X&#39;</b>.</li>
	<li>If an empty square (&#39;E&#39;) with <b>no adjacent mines</b> is revealed, then change it to revealed blank (&#39;B&#39;) and all of its adjacent <b>unrevealed</b> squares should be revealed recursively.</li>
	<li>If an empty square (&#39;E&#39;) with <b>at least one adjacent mine</b> is revealed, then change it to a digit (&#39;1&#39; to &#39;8&#39;) representing the number of adjacent mines.</li>
	<li>Return the board when no more squares will be revealed.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 

[[&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;],
 [&#39;E&#39;, &#39;E&#39;, &#39;M&#39;, &#39;E&#39;, &#39;E&#39;],
 [&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;],
 [&#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;, &#39;E&#39;]]

Click : [3,0]

<b>Output:</b> 

[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;M&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]

<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png" style="width: 100%; max-width: 400px" />
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 

[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;M&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]

Click : [1,2]

<b>Output:</b> 

[[&#39;B&#39;, &#39;1&#39;, &#39;E&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;X&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;1&#39;, &#39;1&#39;, &#39;1&#39;, &#39;B&#39;],
 [&#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;, &#39;B&#39;]]

<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png" style="width: 100%; max-width: 400px" />
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The range of the input matrix&#39;s height and width is [1,50].</li>
	<li>The click position will only be an unrevealed square (&#39;M&#39; or &#39;E&#39;), which also means the input board contains at least one clickable square.</li>
	<li>The input board won&#39;t be a stage when game is over (some mines have been revealed).</li>
	<li>For simplicity, not mentioned rules should be ignored in this problem. For example, you <b>don&#39;t</b> need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int m = board.size();
        if (m == 0) return {};
        int n = board[0].size();
        if (n == 0) return {};
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        
        dfs(board, click[0], click[1]);
        return board;
    }
    
private:
    void dfs(vector<vector<char>>& board, int row, int col) {
        int m = board.size();
        int n = board[0].size();
        if (row < 0 || row >= m || col < 0 || col >= n || isdigit(board[row][col]) || board[row][col] == 'B' || board[row][col] == 'M') return;
        else {
            int count = 0;
            for (int i = -1; i <= 1; ++i) {
                for (int j = -1; j <= 1; ++j) {
                    if (i == 0 && j == 0)   continue;
                    if (row + i < 0 || row + i >= m || col + j < 0 || col +  j >= n) continue;
                    count += (board[row+i][col+j] == 'M' ? 1 : 0);
                }
            }
            
            if (count > 0) {
                board[row][col] = '0' + count;
            } else {
                board[row][col] = 'B';
                for (int i = -1; i <= 1; ++i) {
                    for (int j = -1; j <= 1; ++j) {
                        if (i == 0 && j == 0)   continue;
                        if (row + i < 0 || row + i >= m || col + j < 0 || col +  j >= n) continue;
                        if (board[row+i][col+j] != 'M') {
                            dfs(board, row+i, col+j);
                        }
                    }
                }
            }
        }
    }
    
};
```

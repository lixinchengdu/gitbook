# 79. Word Search

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Word Search II](word-search-ii.md)

## Problem:

<p>Given a 2D board and a word, find if the word exists in the grid.</p>

<p>The word can be constructed from letters of sequentially adjacent cell, where &quot;adjacent&quot; cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.</p>

<p><strong>Example:</strong></p>

<pre>
board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

Given word = &quot;<strong>ABCCED</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>SEE</strong>&quot;, return <strong>true</strong>.
Given word = &quot;<strong>ABCB</strong>&quot;, return <strong>false</strong>.
</pre>

## Solutions:

```c++
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if (word.length() == 0) return true;
        int m = board.size();
        if (m == 0) return false;
        int n = board[0].size();
        if (n == 0) return false;
        
        // there is on path!
        
        vector<vector<bool>> visited (m, vector<bool>(n, false));
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (helper(board, m, n, i, j, visited, word, 0)) return true;
            }
        }
        return false;
    }
    
    bool helper(vector<vector<char>>& board, int m, int n, int i, int j, vector<vector<bool>>& visited, string& word, int pos) {
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j])  return false;
        if (word[pos] != board[i][j])   return false;
        visited[i][j] = true;
        if (pos == word.length() - 1)   return true; 
       
        for (int d = 0; d < 4; ++d) {
            if(helper(board, m, n, i + directions[d][0], j + directions[d][1], visited, word, pos + 1))    return true;
        }
        visited[i][j] = false;
        return false;
    }
    
private:
    int directions[4][2] = {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
};
```

# 695. Max Area of Island

* *Difficulty: Medium*

* *Topics: Array, Depth-first Search*

* *Similar Questions:*

  * [Number of Islands](number-of-islands.md)

  * [Island Perimeter](island-perimeter.md)

## Problem:

<p>Given a non-empty 2D array <code>grid</code> of 0&#39;s and 1&#39;s, an <b>island</b> is a group of <code>1</code>&#39;s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.</p>

<p>Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)</p>

<p><b>Example 1:</b></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>
Given the above grid, return <code>6</code>. Note the answer is not 11, because the island must be connected 4-directionally.

<p><b>Example 2:</b></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>
Given the above grid, return <code>0</code>.

<p><b>Note:</b> The length of each dimension in the given <code>grid</code> does not exceed 50.</p>

## Solutions:

```c++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        
        vector<vector<bool>> visited(m, vector<bool> (n, false));
        int ret = 0;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] && !visited[i][j]) {
                    ret = max(ret, dfs(grid, visited, i, j));
                }
            }
        }
        
        return ret;
    }
private:
    int dfs(const vector<vector<int>>& grid, vector<vector<bool>>& visited, int row, int col) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (row < 0 || row >= m || col < 0 || col >= n || !grid[row][col] || visited[row][col]) return 0;
        visited[row][col] = true;
        
        int ret = 1;
        ret += dfs(grid, visited, row + 1, col);
        ret += dfs(grid, visited, row - 1, col);
        ret += dfs(grid, visited, row, col + 1);
        ret += dfs(grid, visited, row, col - 1);
        
        return ret;
    }
    
};
```

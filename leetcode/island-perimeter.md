# 463. Island Perimeter

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Max Area of Island](max-area-of-island.md)

  * [Flood Fill](flood-fill.md)

  * [Coloring A Border](coloring-a-border.md)

## Problem:

<p>You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.</p>

<p>Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn&#39;t have &quot;lakes&quot; (water inside that isn&#39;t connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don&#39;t exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong>
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

<strong>Output:</strong> 16

<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image below:

<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
</pre>

## Solutions:

```c++
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j]) {
                    return dfs(grid, visited, i, j);
                }
            }
        }
        
        return 0;
    }

private:
    int dfs(vector<vector<int>>& grid, vector<vector<bool>>& visited, int row, int col) {
        int m = grid.size();
        int n = grid[0].size();
        
        if (row < 0 || row >= m || col < 0 || col >= n || !grid[row][col])  return 1;
        if (visited[row][col])  return 0;
        
        visited[row][col] = true;
        int ret = 0;
        ret += dfs(grid, visited, row + 1, col);
        ret += dfs(grid, visited, row - 1, col);
        ret += dfs(grid, visited, row, col + 1);
        ret += dfs(grid, visited, row, col - 1);
        
        return ret;
    }
    
};
```

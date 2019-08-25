# 200. Number of Islands

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search, Union Find*

* *Similar Questions:*

  * [Surrounded Regions](surrounded-regions.md)

  * [Walls and Gates](walls-and-gates.md)

  * [Number of Islands II](number-of-islands-ii.md)

  * [Number of Connected Components in an Undirected Graph](number-of-connected-components-in-an-undirected-graph.md)

  * [Number of Distinct Islands](number-of-distinct-islands.md)

  * [Max Area of Island](max-area-of-island.md)

## Problem:

<p>Given a 2d grid map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong>
11110
11010
11000
00000

<strong>Output:</strong>&nbsp;1
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong>
11000
11000
00100
00011

<strong>Output: </strong>3
</pre>
## Solutions:

```c++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (visited[i][j] || grid[i][j] == '0') continue;
                ++count;
                dfs(grid, visited, m, n, i, j);
            }
        }
        
        return count;
    }
    
    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int m, int n, int i, int j) {
        if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || grid[i][j] == '0') return;
        visited[i][j] = true;
        for (int d = 0; d < 4; ++d) {
            dfs(grid, visited, m, n, i + directions[d][0], j + directions[d][1]);
        }
    }
    
private:
    int directions[4][2] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
};
```

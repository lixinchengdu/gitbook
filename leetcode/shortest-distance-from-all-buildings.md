# 317. Shortest Distance from All Buildings

* *Difficulty: Hard*

* *Topics: Breadth-first Search*

* *Similar Questions:*

  * [Walls and Gates](walls-and-gates.md)

  * [Best Meeting Point](best-meeting-point.md)

  * [As Far from Land as Possible](as-far-from-land-as-possible.md)

## Problem:

<p>You want to build a house on an <i>empty</i> land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values <b>0</b>, <b>1</b> or <b>2</b>, where:</p>

<ul>
	<li>Each <b>0</b> marks an empty land which you can pass by freely.</li>
	<li>Each <b>1</b> marks a building which you cannot pass through.</li>
	<li>Each <b>2</b> marks an obstacle which you cannot pass through.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

<strong>Output:</strong> 7 

<strong>Explanation:</strong> Given three buildings at <code>(0,0)</code>, <code>(0,4)</code>, <code>(2,2)</code>, and an obstacle at <code>(0,2),
             t</code>he point <code>(1,2)</code> is an ideal empty land to build a house, as the total 
&nbsp;            travel distance of 3+3+1=7 is minimal. So return 7.</pre>

<p><b>Note:</b><br />
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.</p>

## Solutions:

```c++
class Solution {
public:
    int shortestDistance(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return -1;
        int n = grid[0].size();
        if (n == 0) return -1;
        
        vector<vector<bool>> reachable(m, vector<bool>(n, true));
        int emptyCount = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    ++emptyCount;
                }
            }
        }
        
        if (emptyCount == 0)    return -1;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 1)    continue;
                auto visited = bfs(grid, i, j);
                matrixAdd(m, n, reachable, visited);
            }
        }
        
        int minDistance = INT_MAX;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] <= 0 && reachable[i][j]) {
                    minDistance = min(minDistance, -grid[i][j]);
                }
            }
        }
        
        return minDistance == INT_MAX ? -1 : minDistance;
    }
    
private:
    void matrixAdd(int m, int n, vector<vector<bool>>& reachable, vector<vector<bool>>& visited) {
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                reachable[i][j] = reachable[i][j] && visited[i][j];
            }
        }
    }
    
    
    int directions[4][2] {
        {1, 0},
        {-1, 0},
        {0, 1},
        {0, -1}
    };
    
    vector<vector<bool>> bfs(vector<vector<int>>& grid, int row, int col) {
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        
        int count = 0;
        int distance = 0;
        
        queue<pair<int, int>> q;
        
        q.push({row, col});
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto coord = q.front(); q.pop();
                grid[coord.first][coord.second] -= distance;
                
                for (int d = 0; d < 4; ++d) {
                    int newRow = coord.first + directions[d][0];
                    int newCol = coord.second + directions[d][1];
                    if (newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && grid[newRow][newCol] <= 0 && !visited[newRow][newCol]) {
                        q.push({newRow, newCol});
                        visited[newRow][newCol] = true;
                        ++count;
                    }
                }
                
            }
            ++distance;
        }
        
        return visited;
        
    }
    
};
```

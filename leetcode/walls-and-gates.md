# 286. Walls and Gates

* *Difficulty: Medium*

* *Topics: Breadth-first Search*

* *Similar Questions:*

  * [Surrounded Regions](surrounded-regions.md)

  * [Number of Islands](number-of-islands.md)

  * [Shortest Distance from All Buildings](shortest-distance-from-all-buildings.md)

  * [Robot Room Cleaner](robot-room-cleaner.md)

  * [Rotting Oranges](rotting-oranges.md)

## Problem:

<p>You are given a <i>m x n</i> 2D grid initialized with these three possible values.</p>

<ol>
	<li><code>-1</code> - A wall or an obstacle.</li>
	<li><code>0</code> - A gate.</li>
	<li><code>INF</code> - Infinity means an empty room. We use the value <code>2<sup>31</sup> - 1 = 2147483647</code> to represent <code>INF</code> as you may assume that the distance to a gate is less than <code>2147483647</code>.</li>
</ol>

<p>Fill each empty room with the distance to its <i>nearest</i> gate. If it is impossible to reach a gate, it should be filled with <code>INF</code>.</p>

<p><strong>Example:&nbsp;</strong></p>

<p>Given the 2D grid:</p>

<pre>
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
</pre>

<p>After running your function, the 2D grid should be:</p>

<pre>
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
</pre>

## Solutions:

```c++
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        int INF = INT_MAX;
        queue<pair<int, int>> q;
        int m = rooms.size();
        if (m == 0) return;
        int n = rooms[0].size();
        if (n == 0) return;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (rooms[i][j] == 0) {
                    q.push({i + 1, j});
                    q.push({i - 1, j});
                    q.push({i, j + 1});
                    q.push({i, j - 1});
                }
            }
        }
        
        int distance = 0;
        while (!q.empty()) {
            ++distance;
            int size = q.size();
            for (int k = 0; k < size; ++k) {
                int row = q.front().first;
                int col = q.front().second;
                q.pop();
                
                if (row < 0 || row >= m || col < 0 || col >= n || rooms[row][col] != INF)  continue;
                rooms[row][col] = distance;
                q.push({row + 1, col});
                q.push({row - 1, col});
                q.push({row, col - 1});
                q.push({row, col + 1});
            }
        }
    }
};
```

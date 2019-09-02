# 741. Cherry Pickup

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Minimum Path Sum](minimum-path-sum.md)

  * [Dungeon Game](dungeon-game.md)

## Problem:

<p>In a N x N <code>grid</code> representing a field of cherries, each cell is one of three possible integers.</p>

<p>&nbsp;</p>

<ul>
	<li>0 means the cell is empty, so you can pass through;</li>
	<li>1 means the cell contains a cherry, that you can pick up and pass through;</li>
	<li>-1 means the cell contains a thorn that blocks your way.</li>
</ul>

<p>&nbsp;</p>

<p>Your task is to collect maximum number of cherries possible by following the rules below:</p>

<p>&nbsp;</p>

<ul>
	<li>Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);</li>
	<li>After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;</li>
	<li>When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);</li>
	<li>If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.</li>
</ul>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
<b>Output:</b> 5
<b>Explanation:</b> 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>grid</code> is an <code>N</code> by <code>N</code> 2D array, with <code>1 &lt;= N &lt;= 50</code>.</li>
	<li>Each <code>grid[i][j]</code> is an integer in the set <code>{-1, 0, 1}</code>.</li>
	<li>It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.</li>
	<li>
	<p>&nbsp;</p>
	</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int cherryPickup(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        unordered_map<int, int> cache;
        int ret = helper(grid, m, n, m - 1, n - 1, m - 1, n - 1, cache);
        return ret == -1 ? 0 : ret;
    }
    
private:
    int helper(const vector<vector<int>>& grid, int m, int n, int x1, int y1, int x2, int y2, unordered_map<int, int>& cache) {
        if (x1 == 0 && y1 == 0 && x2 == 0 && y2 == 0)   return grid[x1][y1];
        int digest = positionDigest(m, n, x1, y1, x2, y2);
        if (cache.count(digest) > 0)    return cache[digest];
        int ret = 0;
        if (grid[x1][y1] == 1) ++ret;
        if (grid[x2][y2] == 1) ++ret;
        if (x1 == x2 && y1 == y2 && grid[x1][y1] == 1) {
            ret -= 1;
        }
        
        int lastValue = -1;
        for (int i = 0; i < 2; ++i) {
            for (int j = 0;j < 2; ++j) {
                int prevX1 = x1 + direction[i][0];
                int prevY1 = y1 + direction[i][1];
                int prevX2 = x2 + direction[j][0];
                int prevY2 = y2 + direction[j][1];
                
                if (prevX1 >= 0 && prevY1 >= 0 && grid[prevX1][prevY1] != -1 && prevX2 >= 0 && prevY2 >= 0 && grid[prevX2][prevY2] != -1) {
                    lastValue = max(lastValue, helper(grid, m, n, prevX1, prevY1, prevX2, prevY2, cache));
                }
            }
        }
        if (lastValue == -1)    ret = -1;
        else {
            ret += lastValue;
        }
        
        cache[digest] = ret;
        return ret;
        
    }
    
    int positionDigest(int m, int n, int x1, int y1, int x2, int y2) {
        int gridNum = m * n;
        int position1 = x1 * n + y1;
        int position2 = x2 * n + y2;
        
        return position1 * gridNum + position2;
    }
    
    int direction[2][2] = {
        {-1, 0},
        {0, -1}
    };
    
};
```

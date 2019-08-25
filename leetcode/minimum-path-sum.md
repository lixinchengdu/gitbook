# 64. Minimum Path Sum

* *Difficulty: Medium*

* *Topics: Array, Dynamic Programming*

* *Similar Questions:*

  * [Unique Paths](unique-paths.md)

  * [Dungeon Game](dungeon-game.md)

  * [Cherry Pickup](cherry-pickup.md)

## Problem:

<p>Given a <em>m</em> x <em>n</em> grid filled with non-negative numbers, find a path from top left to bottom right which <em>minimizes</em> the sum of all numbers along its path.</p>

<p><strong>Note:</strong> You can only move either down or right at any point in time.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; [1,3,1],
  [1,5,1],
  [4,2,1]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Because the path 1&rarr;3&rarr;1&rarr;1&rarr;1 minimizes the sum.
</pre>

## Solutions:

```c++
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        dp[0][0] = grid[0][0];
        
        for (int i = 1; i < m; ++i) {
            dp[i][0] += grid[i][0] + dp[i-1][0];
        }
        
        for (int j = 1; j < n; ++j) {
            dp[0][j] += grid[0][j] + dp[0][j-1];
        }
        
        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

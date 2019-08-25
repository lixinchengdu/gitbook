# 329. Longest Increasing Path in a Matrix

* *Difficulty: Hard*

* *Topics: Depth-first Search, Topological Sort, Memoization*

* *Similar Questions:*

## Problem:

<p>Given an integer matrix, find the length of the longest increasing path.</p>

<p>From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong>nums = 
[
  [<font color="red">9</font>,9,4],
  [<font color="red">6</font>,6,8],
  [<font color="red">2</font>,<font color="red">1</font>,1]
] 
<strong>Output:</strong> 4 
<strong>Explanation:</strong> The longest increasing path is <code>[1, 2, 6, 9]</code>.
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong> nums = 
[
  [<font color="red">3</font>,<font color="red">4</font>,<font color="red">5</font>],
  [3,2,<font color="red">6</font>],
  [2,2,1]
] 
<strong>Output: </strong>4 
<strong>Explanation: </strong>The longest increasing path is <code>[3, 4, 5, 6]</code>. Moving diagonally is not allowed.
</pre>

## Solutions:

```c++
class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        unordered_map<int, int> memory;
        int m = matrix.size();
        if (m == 0) return 0;
        int n = matrix[0].size();
        if (n == 0) return 0;
        
        int ret = 0;
        
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < n; ++col) {
                ret = max(ret, dfs(matrix, m, n, row, col, memory));
            }
        }
        
        return ret;
    }
    
    int dfs(const vector<vector<int>>&matrix, int m , int n, int row, int col, unordered_map<int, int>& memory) {
        int coord = n * row + col;
        if (memory.count(coord) > 0) {
            return memory[coord];
        } else {
            int maxPathLen = 1;
            for (int d = 0; d < 4; ++d) {
                int nextRow = row + directions[d][0];
                int nextCol = col + directions[d][1];
                if (nextRow < 0 || nextRow >= m || nextCol < 0 || nextCol >= n)  continue;
                if (matrix[nextRow][nextCol] <= matrix[row][col]) continue;
                maxPathLen = max(maxPathLen, 1 + dfs(matrix, m, n, nextRow, nextCol, memory));
            }
            memory[coord] = maxPathLen;
            return maxPathLen;
        }
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

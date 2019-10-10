# 542. 01 Matrix

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.</p>

<p>The distance between two adjacent cells is 1.</p>

<p>&nbsp;</p>

<p><b>Example 1: </b></p>

<pre>
<strong>Input:</strong>
[[0,0,0],
 [0,1,0],
 [0,0,0]]

<strong>Output:</strong>
[[0,0,0],
&nbsp;[0,1,0],
&nbsp;[0,0,0]]
</pre>

<p><b>Example 2: </b></p>

<pre>
<b>Input:</b>
[[0,0,0],
 [0,1,0],
 [1,1,1]]

<strong>Output:</strong>
[[0,0,0],
 [0,1,0],
 [1,2,1]]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The number of elements of the given matrix will not exceed 10,000.</li>
	<li>There are at least one 0 in the given matrix.</li>
	<li>The cells are adjacent in only four directions: up, down, left and right.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return {};
        int n = matrix[0].size();
        if (n == 0) return {};
        
        queue<pair<int, int>> q;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }
        
        vector<vector<int>> ret(m, vector<int> (n, -1));
        
        int level = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                auto coord = q.front(); q.pop();
                int row = coord.first;
                int col = coord.second;
                if (row < 0 || row >= m || col < 0 || col >= n || ret[row][col] != -1)  continue;
                if (matrix[row][col] == 0) {
                    ret[row][col] = 0;
                } else {
                    ret[row][col] = level;
                }
                
                q.push({row + 1, col});
                q.push({row - 1, col});
                q.push({row, col + 1});
                q.push({row, col - 1});
            }
            
            ++level;
            
        }
        
        return ret;
        
    }
};
```

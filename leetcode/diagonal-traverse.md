# 498. Diagonal Traverse

* *Difficulty: Medium*

* *Topics: *

* *Similar Questions:*

## Problem:

<p>Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

<b>Output:</b>  [1,2,4,7,5,3,6,8,9]

<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/diagonal_traverse.png" style="width: 220px;" />
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<p>The total number of elements of the given matrix will not exceed 10,000.</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return {};
        int n = matrix[0].size();
        if (n == 0) return {};
        
        vector<int> ret;
        int row = 0;
        int col = 0;
        
        int direction[2] = {-1, 1};
        while (row < m && col < n) {
            ret.push_back(matrix[row][col]);
            if (row + direction[0] >= 0 && row + direction[0] < m && col + direction[1] >= 0 && col + direction[1] < n) {
                row = row + direction[0];
                col = col + direction[1];
            } else {
                direction[0] = -direction[0];
                direction[1] = -direction[1];
                if (row == 0) {
                    ++col;
                } else if (row == m - 1) {
                    ++col;
                } else if (col == 0) {
                    ++row;
                } else if (col == n - 1) {
                    ++row;
                }
                
                if (!(row>= 0 && row < m && col >= 0 && col < n)) {
                    row = row + direction[0];
                    col = col + direction[1];
                }
            }
        }
        
        return ret;
    }
};
```

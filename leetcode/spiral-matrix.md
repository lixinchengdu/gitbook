# 54. Spiral Matrix

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Spiral Matrix II](spiral-matrix-ii.md)

## Problem:

<p>Given a matrix of <em>m</em> x <em>n</em> elements (<em>m</em> rows, <em>n</em> columns), return all elements of the matrix in spiral order.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong>
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return {};
        int n = matrix[0].size();
        if (n == 0) return {};
        
        vector<int> ret;
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;
        
        int row = 0;
        int col = -1;
        
        int d = 0;
        
        for (;;) {
            // to right
            if (col + 1 > right)    return ret;
            while (col < right) {
                ret.push_back(matrix[row][++col]);
            }
            ++top;
            
            // to bottom
            if (row + 1 > bottom)   return ret;
            while (row < bottom) {
                ret.push_back(matrix[++row][col]);
            }
            --right;
            
            // to left
            if (col - 1 < left) return ret;
            while (col > left) {
                ret.push_back(matrix[row][--col]);
            }
            --bottom;
            
            //to top
            if (row - 1 < top)  return ret;
            while (row > top) {
                ret.push_back(matrix[--row][col]);
            }
            ++left;
        }
    }
    
};
```

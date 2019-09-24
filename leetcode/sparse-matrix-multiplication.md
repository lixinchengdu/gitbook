# 311. Sparse Matrix Multiplication

* *Difficulty: Medium*

* *Topics: Hash Table*

* *Similar Questions:*

## Problem:

<p>Given two <a href="https://en.wikipedia.org/wiki/Sparse_matrix" target="_blank">sparse matrices</a> <b>A</b> and <b>B</b>, return the result of <b>AB</b>.</p>

<p>You may assume that <b>A</b>&#39;s column number is equal to <b>B</b>&#39;s row number.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:

</b><strong>A</strong> = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

<strong>B</strong> = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

<strong>Output:</strong>

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
<b>AB</b> = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& A, vector<vector<int>>& B) {
        int m = A.size();
        if (m == 0) return {};
        int k = A[0].size();
        if (k == 0) return {};
        int n = B[0].size();
        if (n == 0) return {};
        
        vector<vector<int>> matrix(m, vector<int>(n, 0));
        
        for (int row = 0; row < m; ++row) {
            for (int col = 0; col < k; ++col) {
                if (A[row][col] == 0)   continue;
                for (int i = 0; i < n; ++i) {
                    matrix[row][i] += A[row][col] * B[col][i];
                }
            }
        }
        
        return matrix;
    }
};
```

# 240. Search a 2D Matrix II

* *Difficulty: Medium*

* *Topics: Binary Search, Divide and Conquer*

* *Similar Questions:*

  * [Search a 2D Matrix](search-a-2d-matrix.md)

## Problem:

<p>Write an efficient algorithm that searches for a value in an <i>m</i> x <i>n</i> matrix. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p><strong>Example:</strong></p>

<p>Consider the following matrix:</p>

<pre>
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
</pre>

<p>Given&nbsp;target&nbsp;=&nbsp;<code>5</code>, return&nbsp;<code>true</code>.</p>

<p>Given&nbsp;target&nbsp;=&nbsp;<code>20</code>, return&nbsp;<code>false</code>.</p>

## Solutions:

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0) return false;
        int n = matrix[0].size();
        if (n == 0) return false;
        
        int i = m - 1;
        int j = 0;
        while (i >= 0 && j < n) {
            if (matrix[i][j] == target) return true;
            else if (matrix[i][j] < target) {
                ++j;
            } else {
                --i;
            }
        }
        
        return false;
    }
};
```

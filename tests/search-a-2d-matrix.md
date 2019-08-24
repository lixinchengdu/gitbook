# 74. Search a 2D Matrix

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Search a 2D Matrix II](./tests/search-a-2d-matrix.md)

## Problem:

<p>Write an efficient algorithm that searches for a value in an <em>m</em> x <em>n</em> matrix. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted from left to right.</li>
	<li>The first integer of each row is greater than the last integer of the previous row.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
<strong>Output:</strong> false</pre>

## Solutions:

```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        if (m == 0) return false;
        int n = matrix[0].size();
        if (n == 0) return false;
        
        int low = 0;
        int high = m*n -1;
        while (low + 1 < high)
        {
            int mid = low + (high-low)/2;
            int row = mid/n;
            int col = mid%n;
            int val = matrix[row][col];
            if (val == target)  return true;
            else if (val > target)  high = mid;
            else low = mid;
        }
        if (matrix[low/n][low%n] == target) return true;
        if (matrix[high/n][high%n] == target)   return true;
        return false;
        
    }
};
```

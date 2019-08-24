# 48. Rotate Image

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

## Problem:

<p>You are given an <em>n</em> x <em>n</em> 2D matrix representing an image.</p>

<p>Rotate the image by 90 degrees (clockwise).</p>

<p><strong>Note:</strong></p>

<p>You have to rotate the image <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>, which means you have to modify the input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the rotation.</p>

<p><strong>Example 1:</strong></p>

<pre>
Given <strong>input matrix</strong> = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix <strong>in-place</strong> such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
Given <strong>input matrix</strong> =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix <strong>in-place</strong> such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int round = n/2;
        for (int k = 0; k < round; ++k) {
            int count = n - 2*k -1;
            for (int c = 0; c < count; ++c) {
                int i = k;
                int j = k + c;
                
                int temp = matrix[i][j];
                
                for (int time = 0 ; time < 3; ++time) {
                    int newi = n - 1 - j;
                    int newj = i;
                    matrix[i][j] = matrix[newi][newj];
                    i = newi;
                    j = newj;
                }
                matrix[i][j] = temp;  
            }
        } 
    }
};
```

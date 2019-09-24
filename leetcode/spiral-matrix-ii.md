# 59. Spiral Matrix II

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Spiral Matrix](spiral-matrix.md)

## Problem:

<p>Given a positive integer <em>n</em>, generate a square matrix filled with elements from 1 to <em>n</em><sup>2</sup> in spiral order.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong>
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int top = 0;
        int down = n - 1;
        int left = 0;
        int right = n - 1;
        
        vector<vector<int>> matrix(n, vector<int>(n, 0));
        int row = 0;
        int col = 0;
        int val = 1;
        
        matrix[row][col] = val++;
        while (true) {
            if (col + 1 > right)    return matrix;
            while (col + 1 <= right) {
                ++col;
                matrix[row][col] = val++;
            }
            ++top;
            
            if (row + 1 > down) return matrix;
            while (row + 1 <= down) {
                ++row;
                matrix[row][col] = val++;
            }
            --right;
            
            if (col - 1 < left) return matrix;
            while (col - 1 >= left) {
                --col;
                matrix[row][col] = val++;
            }
            --down;
            
            if (row - 1 < top) return matrix;
            while (row - 1 >= top) {
                --row;
                matrix[row][col] = val++;
            }
            ++left;
        }
    }
    
private:
    int directions[4][2] = {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1}
    };
};
```

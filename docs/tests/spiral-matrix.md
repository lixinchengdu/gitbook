# 54. Spiral Matrix

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Spiral Matrix II](./tests/spiral-matrix.md)

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
    int direction[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ret;
        int m = matrix.size();
        if (m == 0) return ret;
        int n = matrix[0].size();
        if (n == 0) return ret;
        
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        int directIndex = 0;
        int x = 0;
        int y = 0;
        while (true) {
            ret.push_back(matrix[y][x]);
            visited[y][x] = true;
             //cout << "x:" << x + direction[directIndex][1] << " y:" << y + direction[directIndex][0]<< "!" << matrix[y][x] << endl;
            //cout << (x + direction[directIndex][1] < n) << endl;
            if (x + direction[directIndex][1] >= 0 && x + direction[directIndex][1] < n && y + direction[directIndex][0] >= 0 && y + direction[directIndex][0] < m && !visited[y + direction[directIndex][0]][x + direction[directIndex][1]]) {
                x += direction[directIndex][1];
                y += direction[directIndex][0];
            } else {
                //cout << "ha " << endl;
                directIndex = (directIndex + 1) % 4;
                x += direction[directIndex][1];
                y += direction[directIndex][0];
                //cout << "haha" << endl;
               //cout << "x:" << x << " y:" << y << "!" << matrix[y][x] << endl;
                if ( y < 0 || y >= m || x < 0 || x >= n || visited[y][x])  return ret;
            }
        }
    }
};
```

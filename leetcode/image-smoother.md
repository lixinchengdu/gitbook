# 661. Image Smoother

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

## Problem:

<p>Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<b>Output:</b>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<b>Explanation:</b>
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value in the given matrix is in the range of [0, 255].</li>
<li>The length and width of the given matrix are in the range of [1, 150].</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int m = M.size();
        if (m == 0) return {};
        int n = M[0].size();
        if (n == 0) return {};
        
        vector<vector<int>> ret (m, vector<int> (n, 0));
        
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                int count = 0;
                int gray = 0;
                
                for (int dx = -1; dx <= 1; ++dx) {
                    for (int dy = -1; dy <= 1; ++dy) {
                        if (x + dx < 0 || x + dx >= m || y + dy < 0 || y + dy >= n) continue;
                        ++count;
                        gray += M[x+dx][y+dy];
                    }
                }
                
                ret[x][y] = gray / count;
                
            }
        }
        
        return ret;
    }
};
```

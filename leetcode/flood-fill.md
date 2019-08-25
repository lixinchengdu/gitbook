# 733. Flood Fill

* *Difficulty: Easy*

* *Topics: Depth-first Search*

* *Similar Questions:*

  * [Island Perimeter](island-perimeter.md)

## Problem:

<p>
An <code>image</code> is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
</p><p>
Given a coordinate <code>(sr, sc)</code> representing the starting pixel (row and column) of the flood fill, and a pixel value <code>newColor</code>, "flood fill" the image.
</p><p>
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.
</p><p>
At the end, return the modified image.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<b>Output:</b> [[2,2,2],[2,2,0],[2,0,1]]
<b>Explanation:</b> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>image</code> and <code>image[0]</code> will be in the range <code>[1, 50]</code>.</li>
<li>The given starting pixel will satisfy <code>0 <= sr < image.length</code> and <code>0 <= sc < image[0].length</code>.</li>
<li>The value of each color in <code>image[i][j]</code> and <code>newColor</code> will be an integer in <code>[0, 65535]</code>.</li>
</p>
## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int m = image.size();
        if (m == 0) return {};
        int n = image[0].size();
        if (n == 0) return {};
        
        if (sr < 0 || sr >= m || sc < 0 || sc >= n) return {};
        if (image[sr][sc] == newColor)  return image;
        helper(image, sr, sc, m, n, image[sr][sc], newColor);
        
        return image;
    }
    
    void helper(vector<vector<int>>& image, int sr, int sc, int m, int n, int color, int newColor) {
        image[sr][sc] = newColor;
        if (sr + 1 < m && image[sr + 1][sc] == color)   helper(image, sr + 1, sc, m, n, color, newColor);
        if (sr - 1 >= 0 && image[sr - 1][sc] == color)  helper(image, sr - 1, sc, m, n, color, newColor);
        if (sc + 1 < n && image[sr][sc + 1] == color)   helper(image, sr, sc + 1, m, n, color, newColor);
        if (sc - 1 >= 0 && image[sr][sc - 1] == color)  helper(image, sr, sc - 1, m, n, color, newColor);
    }
};
```

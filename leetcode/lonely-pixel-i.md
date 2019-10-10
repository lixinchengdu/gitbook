# 531. Lonely Pixel I

* *Difficulty: Medium*

* *Topics: Array, Depth-first Search*

* *Similar Questions:*

  * [Lonely Pixel II](lonely-pixel-ii.md)

## Problem:

<p>Given a picture consisting of black and white pixels, find the number of <b>black</b> lonely pixels.</p>

<p>The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively. </p>

<p>A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

<b>Output:</b> 3
<b>Explanation:</b> All the three 'B's are black lonely pixels.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The range of width and height of the input 2D array is [1,500].</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int findLonelyPixel(vector<vector<char>>& picture) {
        int m = picture.size();
        if (m == 0) return 0;
        int n = picture[0].size();
        if (n == 0) return 0;
        
        int ret = 0;
        
        for (int row = 0; row < m; ++row) {
            int blackIdx = -1;
            int blackCount = 0;
            for (int col = 0; col < n; ++col) {
                if (picture[row][col] == 'B') {
                    blackIdx = col;
                    ++blackCount;
                    if (blackCount > 1) break;
                }
            }
            
            if (blackCount == 1) {
                int i;
                for (i = 0; i < m; ++i) {
                    if (i == row)   continue;
                    if (picture[i][blackIdx] == 'B')    break;
                }
                if (i == m) ++ret;
            }        
        }
        
        return ret;
    }
};
```

# 302. Smallest Rectangle Enclosing Black Pixels

* *Difficulty: Hard*

* *Topics: Binary Search*

* *Similar Questions:*

## Problem:

<p>An image is represented by a binary matrix with <code>0</code> as a white pixel and <code>1</code> as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location <code>(x, y)</code> of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
  &quot;0010&quot;,
  &quot;0110&quot;,
  &quot;0100&quot;
]
and <code>x = 0<font face="sans-serif, Arial, Verdana, Trebuchet MS">, </font></code><code>y = 2</code>

<strong>Output:</strong> 6
</pre>

## Solutions:

```c++
class Solution {
public:
    int minArea(vector<vector<char>>& image, int x, int y) {
        int m = image.size();
        if (m == 0) return 0;
        int n = image[0].size();
        if (n == 0) return 0;
        
        int up = searchByRow(image, 0, x, m, n, true);
        int down = searchByRow(image, x, m - 1, m, n, false);
        int right = searchByColumn(image, y, n - 1, m, n, true);
        int left = searchByColumn(image, 0, y, m, n, false);
        
        return (down - up + 1) * (right - left + 1);
        
    }
private:
    int searchByRow(vector<vector<char>>& image, int up, int down, int m, int n, bool upwards) {
        while (up + 1 < down) {
            int mid = up + (down - up) / 2;
            if (pixelInRow(image, mid, m, n)) {
                if (upwards) {
                    down = mid;
                } else {
                    up = mid;
                }
            } else {
                if (upwards) {
                    up = mid;
                } else {
                    down = mid;
                }
            }
        }
        
        if (upwards) {
            return pixelInRow(image, up, m, n) ? up : down;
        } else {
            return pixelInRow(image, down, m, n) ? down : up;
        }
    }
    
    int searchByColumn(vector<vector<char>>& image, int left, int right, int m, int n, bool forwards) {
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (pixelInColumn(image, mid, m, n)) {
                if (forwards) {
                    left = mid;
                } else {
                    right = mid;
                }
            } else {
                if (forwards) {
                    right = mid;
                } else {
                    left = mid;
                }
            }
        }
        
        if (forwards) {
            return pixelInColumn(image, right, m, n) ? right : left;
        } else {
            return pixelInColumn(image, left, m, n) ? left : right;
        }
    }
    
    bool pixelInRow(vector<vector<char>>& image, int row, int m, int n) {
        for (int i = 0; i < n; ++i) {
            if (image[row][i] == '1')   return true;
        }
        
        return false;
    }
    
    bool pixelInColumn(vector<vector<char>>& image, int col, int m, int n) {
        for (int i = 0; i < m; ++i) {
            if (image[i][col] == '1')   return true;
        }
        
        return false;
    }
    
};
```

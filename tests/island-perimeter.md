# 463. Island Perimeter

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Max Area of Island](./tests/island-perimeter.md)

  * [Flood Fill](./tests/island-perimeter.md)

  * [Coloring A Border](./tests/island-perimeter.md)

## Problem:

<p>You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.</p>

<p>Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).</p>

<p>The island doesn&#39;t have &quot;lakes&quot; (water inside that isn&#39;t connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don&#39;t exceed 100. Determine the perimeter of the island.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong>
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

<strong>Output:</strong> 16

<strong>Explanation:</strong> The perimeter is the 16 yellow stripes in the image below:

<img src="https://assets.leetcode.com/uploads/2018/10/12/island.png" style="width: 221px; height: 213px;" />
</pre>

## Solutions:

```c++
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = m? grid[0].size() : 0;
        int count = 0;
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j])
                {
                    if (i-1 < 0 || i-1 >= 0 && grid[i-1][j] == 0)   count++;
                    if (i+1 >= m || i+1 < m && grid[i+1][j] == 0)   count++;
                    if (j-1 < 0 || j-1 >= 0 && grid[i][j-1] == 0)   count++;
                    if (j+1 >= n || j+1 < n && grid[i][j+1] == 0)   count++;
                }
            }
        }
        return count;
    }
};
```

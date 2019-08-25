# 296. Best Meeting Point

* *Difficulty: Hard*

* *Topics: Math, Sort*

* *Similar Questions:*

  * [Shortest Distance from All Buildings](shortest-distance-from-all-buildings.md)

  * [Minimum Moves to Equal Array Elements II](minimum-moves-to-equal-array-elements-ii.md)

## Problem:

<p>A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using <a href="http://en.wikipedia.org/wiki/Taxicab_geometry" target="_blank">Manhattan Distance</a>, where distance(p1, p2) = <code>|p2.x - p1.x| + |p2.y - p1.y|</code>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

<strong>Output: 6 

Explanation: </strong>Given three people living at <code>(0,0)</code>, <code>(0,4)</code>, and <code>(2,2)</code>:
&nbsp;            The point <code>(0,2)</code> is an ideal meeting point, as the total travel distance 
&nbsp;            of 2+2+2=6 is minimal. So return 6.</pre>

## Solutions:

```c++
class Solution {
public:
    int minTotalDistance(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<int> x, y;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 1) {
                    x.push_back(i);
                    y.push_back(j);
                }
            }
        }
        
        sort(y.begin(), y.end()); // sorting!!!!!!!
        
        return minTotalDistanceAtOneDimension(x) + minTotalDistanceAtOneDimension(y);
    }
    
private:
    int minTotalDistanceAtOneDimension(vector<int>& points) { // it is median!!! not average!!!
        int distance = 0;
        int i = 0;
        int j = points.size() - 1;
        while (i < j) {
            distance += points[j] - points[i];
            i++;
            j--;
        }
        cout << distance << endl;
        return distance;
    }
};
```

# 469. Convex Polygon

* *Difficulty: Medium*

* *Topics: Math*

* *Similar Questions:*

## Problem:

<p>Given a list of points that form a polygon when joined sequentially, find if this polygon is convex <a href="https://en.wikipedia.org/wiki/Convex_polygon" target="_blank">(Convex polygon definition)</a>.</p>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>There are at least 3 and at most 10,000 points.</li>
	<li>Coordinates are in the range -10,000 to 10,000.</li>
	<li>You may assume the polygon formed by given points is always a simple polygon<a href="https://en.wikipedia.org/wiki/Simple_polygon" target="_blank"> (Simple polygon definition)</a>. In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise <b>don&#39;t intersect each other</b>.</li>
</ol>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:<img src="https://assets.leetcode.com/uploads/2018/10/13/polygon_convex.png" style="width: 100px; height: 100px;" />
</pre>

<p><b>Example 2:</b></p>

<pre>
[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:<img src="https://assets.leetcode.com/uploads/2018/10/13/polygon_not_convex.png" style="width: 100px; height: 100px;" />
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isConvex(vector<vector<int>>& points) {
        int direction = 0;
        int n = points.size();
        for (int i = 0; i < points.size(); ++i) {
            int newDirection = orientation(points[i%n], points[(i+1)%n], points[(i+2)%n]);
            if (newDirection == 0)  continue;
            if (newDirection * direction < 0)   return false;
            direction = newDirection;
        }
        return true;
    }
    
    int orientation(vector<int>& a, vector<int>& b, vector<int>& c) {
        vector<int> v1 = {b[0] - a[0], b[1] - a[1]};
        vector<int> v2 = {c[0] - b[0], c[1] - b[1]};
        
        int prodDiff = v1[0] * v2[1] - v1[1] * v2[0];
        if (prodDiff > 0)   return 1;
        else if (prodDiff < 0)   return -1;
        else return 0;
    }
};
```

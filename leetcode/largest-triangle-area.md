# 830. Largest Triangle Area

* *Difficulty: Easy*

* *Topics: Math*

* *Similar Questions:*

  * [Largest Perimeter Triangle](largest-perimeter-triangle.md)

## Problem:

<p>You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The five points are show in the figure below. The red triangle is the largest.
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>No points will be duplicated.</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>Answers within&nbsp;<code>10^-6</code>&nbsp;of the true value will be accepted as correct.</li>
</ul>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        int n = points.size();
        double ret = 0;
        for (int i = 0; i < points.size(); ++i) {
            for (int j = i + 1; j < points.size(); ++j) {
                for (int k = j + 1; k < points.size(); ++k) {
                    ret = max(ret, area(points[i], points[j], points[k]));     
                }
            }
        }
        
        return ret;
    }
    
private:
    inline double area(vector<int>& p1, vector<int>& p2, vector<int>& p3) {
        // (p2[0] - p1[0], p2[1] - p1[1]) cross product (p3[0] - p1[0], p3[1] - p1[1])
        return 0.5 * abs(((p2[0] - p1[0]) * (p3[1] - p1[1])) - ((p2[1] - p1[1]) * (p3[0] - p1[0])));
    }
    
};
```

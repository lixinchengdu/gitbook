# 447. Number of Boomerangs

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Line Reflection](line-reflection.md)

## Problem:

<p>Given <i>n</i> points in the plane that are all pairwise distinct, a &quot;boomerang&quot; is a tuple of points <code>(i, j, k)</code> such that the distance between <code>i</code> and <code>j</code> equals the distance between <code>i</code> and <code>k</code> (<b>the order of the tuple matters</b>).</p>

<p>Find the number of boomerangs. You may assume that <i>n</i> will be at most <b>500</b> and coordinates of points are all in the range <b>[-10000, 10000]</b> (inclusive).</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b>
[[0,0],[1,0],[2,0]]

<b>Output:</b>
2

<b>Explanation:</b>
The two boomerangs are <b>[[1,0],[0,0],[2,0]]</b> and <b>[[1,0],[2,0],[0,0]]</b>
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int ret = 0;
        for (int i = 0; i < points.size(); ++i) {
            map<int, int> distances;
            for (int j = 0; j < points.size(); ++j) {
                if (i == j) continue;
                ++distances[computeDistance(points[i], points[j])];
            }
            for (auto it = distances.begin(); it != distances.end(); ++it) {
                ret += (it -> second) * (it ->second - 1);
            }
        }
        return ret;
    }
    
private:
    int computeDistance(vector<int>& p1, vector<int>& p2) {
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]);
    }
    
};
```

# 149. Max Points on a Line

* *Difficulty: Hard*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Line Reflection](line-reflection.md)

## Problem:

<p>Given <em>n</em> points on a 2D plane, find the maximum number of points that lie on the same straight line.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
^
|
| &nbsp; &nbsp; &nbsp; &nbsp;o
| &nbsp; &nbsp; o
| &nbsp;o &nbsp;
+-------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3  4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
^
|
|  o
| &nbsp;&nbsp;&nbsp;&nbsp;o&nbsp;&nbsp;      o
| &nbsp;&nbsp;&nbsp;&nbsp;   o
| &nbsp;o &nbsp;      o
+-------------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3 &nbsp;4 &nbsp;5 &nbsp;6
</pre>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>

## Solutions:

```c++
class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int ret = 0;
        for (int i = 0; i < points.size(); ++i) {
            map<pair<int, int>, int> lines;
            int verticleCount = 0; // dedicated 
            int horizonCount = 0; // dedicated
            int selfCount = 1;
            for (int j = i + 1; j < points.size(); ++j) {
                if (points[j][0] == points[i][0] && points[j][1] == points[i][1])   ++selfCount;
                else if (points[j][0] == points[i][0])  ++verticleCount;
                else if (points[j][1] == points[i][1])  ++horizonCount;
                else {
                    ++lines[simplify(points[j][1] - points[i][1], points[j][0] - points[i][0])];
                }
            }
            
            int count = max(verticleCount, horizonCount);
            for (auto line : lines) {
                count = max(count, line.second);
            }
            
            count += selfCount;
            
            ret = max(ret, count);
        }
        
        return ret;
    }
    
    pair<int, int> simplify(int a, int b) {
        if (a < 0) { // every a should be not negtive
            a = -a;
            b = -b;
        }
        
        int divisor = gcd(a, abs(b)); // both number should be positive
        return {a/divisor, b/divisor};  // not times sign
    }
    
    int gcd (int a, int b) {
        
        if (a < b)  return gcd(b, a);
        if (b == 0) return a;           
        return gcd(b, a%b);
    }
};
```

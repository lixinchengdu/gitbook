# 118. Pascal's Triangle

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Pascal's Triangle II](pascals-triangle-ii.md)

## Problem:

<p>Given a non-negative integer&nbsp;<em>numRows</em>, generate the first <em>numRows</em> of Pascal&#39;s triangle.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 5
<strong>Output:</strong>
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ret;
        if (numRows < 1)    return ret;
        ret.push_back({1});
        
        for (int i = 1; i < numRows; ++i) {
            vector<int> row (i + 1, 1);
            for (int j = 1; j < i; ++j) {
                row[j] = ret.back()[j-1] + ret.back()[j];
            }
            ret.push_back(row);
        }
        
        return ret;
    }
};
```

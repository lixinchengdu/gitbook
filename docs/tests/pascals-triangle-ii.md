# 119. Pascal's Triangle II

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Pascal's Triangle](./tests/pascals-triangle-ii.md)

## Problem:

<p>Given a non-negative&nbsp;index <em>k</em>&nbsp;where <em>k</em> &le;&nbsp;33, return the <em>k</em><sup>th</sup>&nbsp;index row of the Pascal&#39;s triangle.</p>

<p>Note that the row index starts from&nbsp;0.</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" /><br />
<small>In Pascal&#39;s triangle, each number is the sum of the two numbers directly above it.</small></p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 3
<strong>Output:</strong> [1,3,3,1]
</pre>

<p><strong>Follow up:</strong></p>

<p>Could you optimize your algorithm to use only <em>O</em>(<em>k</em>) extra space?</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> dp(rowIndex + 1, 1);
        for (int i = 2; i <= rowIndex; ++i) {
            for (int j = i - 1; j >= 1; --j) {
                dp[j] = dp[j] + dp[j-1];
            }
        }
        return dp;
    }
    
   
};
```

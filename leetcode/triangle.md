# 120. Triangle

* *Difficulty: Medium*

* *Topics: Array, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.</p>

<p>For example, given the following triangle</p>

<pre>
[
     [<strong>2</strong>],
    [<strong>3</strong>,4],
   [6,<strong>5</strong>,7],
  [4,<strong>1</strong>,8,3]
]
</pre>

<p>The minimum path sum from top to bottom is <code>11</code> (i.e., <strong>2</strong> + <strong>3</strong> + <strong>5</strong> + <strong>1</strong> = 11).</p>

<p><strong>Note:</strong></p>

<p>Bonus point if you are able to do this using only <em>O</em>(<em>n</em>) extra space, where <em>n</em> is the total number of rows in the triangle.</p>

## Solutions:

```c++
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if (triangle.size() == 0)   return 0;
        int level = triangle.size();
        vector<int> dp (level, INT_MAX);
        dp[0] = 0;
        for (auto& values : triangle) {
            for (int i = values.size() - 1; i >= 1; --i) {
                dp[i] = values[i] + min(dp[i-1], dp[i]);
            }
            dp[0] = values[0] + dp[0];
        }
        
        int ret = INT_MAX;
        
        for (auto bottom : dp) {
            ret = min(ret, bottom);
        }
        
        return ret;
        
    }
};
```

# 256. Paint House

* *Difficulty: Easy*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [House Robber](house-robber.md)

  * [House Robber II](house-robber-ii.md)

  * [Paint House II](paint-house-ii.md)

  * [Paint Fence](paint-fence.md)

## Problem:

<p>There are a row of <i>n</i> houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.</p>

<p>The cost of painting each house with a certain color is represented by a <code><i>n</i> x <i>3</i></code> cost matrix. For example, <code>costs[0][0]</code> is the cost of painting house 0 with color red; <code>costs[1][2]</code> is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.</p>

<p><b>Note:</b><br />
All costs are positive integers.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [[17,2,17],[16,16,5],[14,3,19]]
<strong>Output:</strong> 10
<strong>Explanation: </strong>Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
&nbsp;            Minimum cost: 2 + 5 + 3 = 10.
</pre>

## Solutions:

```c++
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        vector<vector<int>> dp(2, vector<int> (3, 0));
        
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
        
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < 3; ++j) {
                dp[i%2][j] = min(dp[(i-1)%2][(j+1)%3], dp[(i-1)%2][(j+2)%3]) + costs[i][j]; 
            }
        }
        
        return min(dp[(n-1)%2][0], min(dp[(n-1)%2][1], dp[(n-1)%2][2]));
    }
};
```

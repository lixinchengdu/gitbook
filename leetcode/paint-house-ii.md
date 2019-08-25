# 265. Paint House II

* *Difficulty: Hard*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Product of Array Except Self](product-of-array-except-self.md)

  * [Sliding Window Maximum](sliding-window-maximum.md)

  * [Paint House](paint-house.md)

  * [Paint Fence](paint-fence.md)

## Problem:

<p>There are a row of <i>n</i> houses, each house can be painted with one of the <i>k</i> colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.</p>

<p>The cost of painting each house with a certain color is represented by a <code><i>n</i> x <i>k</i></code> cost matrix. For example, <code>costs[0][0]</code> is the cost of painting house 0 with color 0; <code>costs[1][2]</code> is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.</p>

<p><b>Note:</b><br />
All costs are positive integers.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [[1,5,3],[2,9,4]]
<strong>Output:</strong> 5
<strong>Explanation: </strong>Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
&nbsp;            Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
</pre>

<p><b>Follow up:</b><br />
Could you solve it in <i>O</i>(<i>nk</i>) runtime?</p>

## Solutions:

```c++
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        int k = costs[0].size();
        if (k == 0) return 0;
        if (k == 1) { // check the situation when there is only one color.
            if (n == 1) return costs[0][0]; 
            return -1;
        }
        
        costs.push_back(vector<int>(k, 0));
        ++n;
        
        

        vector<vector<int>> dp (n + 1, vector<int>(k, 0));

        int least1 = 0;
        int color1 = -1;
        int least2 = 0;
        int color2 = -1;

        for (int i = 1; i <= n; ++i) {
            int curLeast1 = INT_MAX;
            int curColor1 = -1;
            int curLeast2 = INT_MAX;
            int curColor2 = -1;

            for (int j = 0; j < k; ++j) {
                if (j == color1) {
                    dp[i][j] = costs[i-1][j] + least2;
                } else {
                    dp[i][j] = costs[i-1][j] + least1;
                }
                
                if (dp[i][j] < curLeast1) {
                    curLeast2 = curLeast1;
                    curColor2 = curColor1;
                    curLeast1 = dp[i][j];
                    curColor1 = j;
                } else if (dp[i][j] < curLeast2) {
                    curLeast2 = dp[i][j];
                    curColor2 = j;
                }

            }
            cout << endl;

            least1 = curLeast1;
            color1 = curColor1;
            least2 = curLeast2;
            color2 = curColor2;

        }

        return least1;
    }
};
```

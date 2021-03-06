# 410. Split Array Largest Sum

* *Difficulty: Hard*

* *Topics: Binary Search, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given an array which consists of non-negative integers and an integer <i>m</i>, you can split the array into <i>m</i> non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these <i>m</i> subarrays.
</p>

<p><b>Note:</b><br />
If <i>n</i> is the length of array, assume the following constraints are satisfied:
<ul>
<li>1 &le; <i>n</i> &le; 1000</li>
<li>1 &le; <i>m</i> &le; min(50, <i>n</i>)</li>
</ul>
</p>

<p><b>Examples: </b>
<pre>
Input:
<b>nums</b> = [7,2,5,10,8]
<b>m</b> = 2

Output:
18

Explanation:
There are four ways to split <b>nums</b> into two subarrays.
The best way is to split it into <b>[7,2,5]</b> and <b>[10,8]</b>,
where the largest sum among the two subarrays is only 18.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n = nums.size();
        
        // not finalize
        vector<vector<long>> dp(m + 1, vector<long>(n + 1, INT_MAX));
        dp[0][0] = 0;
        
        for (int i = 1; i <= m; ++i) {
            for (int j = i; j <= n; ++j) {
                long sum = 0;
                dp[i][j] = INT_MAX;
                for (int k = 0; k <= j - i; ++k) {
                    sum += nums[j - 1 - k];
                    dp[i][j] = min(dp[i][j], max(sum, dp[i-1][j - k -1] ));
                }
                //cout << i << " " << j << " " << dp[i][j] << endl;
            }
        }
        
        
        return dp[m][n];
        
        //dp[i][j] = min(dp[i-1][0..k], sigma(nums[k..j]))
    }
};
```

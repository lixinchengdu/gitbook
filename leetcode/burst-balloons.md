# 312. Burst Balloons

* *Difficulty: Hard*

* *Topics: Divide and Conquer, Dynamic Programming*

* *Similar Questions:*

  * [Minimum Cost to Merge Stones](minimum-cost-to-merge-stones.md)

## Problem:

<p>Given <code>n</code> balloons, indexed from <code>0</code> to <code>n-1</code>. Each balloon is painted with a number on it represented by array <code>nums</code>. You are asked to burst all the balloons. If the you burst balloon <code>i</code> you will get <code>nums[left] * nums[i] * nums[right]</code> coins. Here <code>left</code> and <code>right</code> are adjacent indices of <code>i</code>. After the burst, the <code>left</code> and <code>right</code> then becomes adjacent.</p>

<p>Find the maximum coins you can collect by bursting the balloons wisely.</p>

<p><b>Note:</b></p>

<ul>
	<li>You may imagine <code>nums[-1] = nums[n] = 1</code>. They are not real therefore you can not burst them.</li>
	<li>0 &le; <code>n</code> &le; 500, 0 &le; <code>nums[i]</code> &le; 100</li>
</ul>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[3,1,5,8]</code>
<b>Output:</b> <code>167 
<strong>Explanation: </strong></code>nums = [3,1,5,8] --&gt; [3,5,8] --&gt;   [3,8]   --&gt;  [8]  --&gt; []
&nbsp;            coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
</pre>
## Solutions:

```c++
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = 1; i < n - 1; ++i) {
            dp[i][i] = nums[i] * nums[i-1] * nums[i+1];
        }
        
        dp[0][0] = nums[0] * nums[1];
        dp[n-1][n-1] = nums[n-2] * nums[n-1];
        
        for (int l = 2; l <= n; ++l) {
            for (int i = 0; i < n; ++i) {
                 if (i + l - 1 >= n) break;
                for (int mid = i; mid <= i + l - 1; ++mid) {
                    dp[i][i + l - 1] = max(dp[i][i + l - 1], nums[mid] * (i - 1 >= 0 ? nums[i-1] : 1) * (i + l < n ? nums[i + l] : 1) 
                                           + (mid - 1 >= i ? dp[i][mid - 1] : 0) + (mid + 1 <= i + l - 1 ? dp[mid + 1][i + l - 1] : 0));
                }
            }
        }
        
        return dp[0][n-1];
    }
};
```

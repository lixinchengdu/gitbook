# 213. House Robber II

* *Difficulty: Medium*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [House Robber](house-robber.md)

  * [Paint House](paint-house.md)

  * [Paint Fence](paint-fence.md)

  * [House Robber III](house-robber-iii.md)

  * [Non-negative Integers without Consecutive Ones](non-negative-integers-without-consecutive-ones.md)

  * [Coin Path](coin-path.md)

## Problem:

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight <strong>without alerting the police</strong>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
&nbsp;            because they are adjacent houses.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
&nbsp;            Total amount you can rob = 1 + 3 = 4.</pre>

## Solutions:

```c++


class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (nums.size() == 0 )  return 0;
        if (nums.size() == 1)   return nums[0]; // this case is very important. Think about [1];
        int maxValue = 0;
        
        vector<int> dp(n + 1, 0);
        
        dp[0] = 0;
        dp[1] = nums[0];
        
        for (int i = 2; i <= n - 1; ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        
        maxValue = max(maxValue, dp[n-1]);
        
        dp[1] = 0;
        for (int i = 2; i <= n; ++i) {
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]);
        }
        
        maxValue = max(maxValue, dp[n]);
        
        return maxValue;
    }
};


```

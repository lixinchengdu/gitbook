# 198. House Robber

* *Difficulty: Easy*

* *Topics: Dynamic Programming*

* *Similar Questions:*

  * [Maximum Product Subarray](./tests/house-robber.md)

  * [House Robber II](./tests/house-robber.md)

  * [Paint House](./tests/house-robber.md)

  * [Paint Fence](./tests/house-robber.md)

  * [House Robber III](./tests/house-robber.md)

  * [Non-negative Integers without Consecutive Ones](./tests/house-robber.md)

  * [Coin Path](./tests/house-robber.md)

  * [Delete and Earn](./tests/house-robber.md)

## Problem:

<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and <b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight <b>without alerting the police</b>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
&nbsp;            Total amount you can rob = 1 + 3 = 4.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,7,9,3,1]
<strong>Output:</strong> 12
<strong>Explanation:</strong> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
&nbsp;            Total amount you can rob = 2 + 9 + 1 = 12.
</pre>

## Solutions:

```c++
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> opt(n);
        for (int i = n-1; i >= 0; i--)
        {
            if (i == n-1)   opt[i] = nums[i];
            if (i == n-2)   opt[i] = max(nums[i], opt[i+1]);
            if (i != n-1 && i != n-2)
            {
                opt[i]=max(nums[i]+opt[i+2], opt[i+1]);
            }
        }
        return opt[0];
    }
};
```

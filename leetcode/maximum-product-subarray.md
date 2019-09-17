# 152. Maximum Product Subarray

* *Difficulty: Medium*

* *Topics: Array, Dynamic Programming*

* *Similar Questions:*

  * [Maximum Subarray](maximum-subarray.md)

  * [House Robber](house-robber.md)

  * [Product of Array Except Self](product-of-array-except-self.md)

  * [Maximum Product of Three Numbers](maximum-product-of-three-numbers.md)

  * [Subarray Product Less Than K](subarray-product-less-than-k.md)

## Problem:

<p>Given an integer array&nbsp;<code>nums</code>, find the contiguous subarray within an array (containing at least one number) which has the largest product.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,-2,4]
<strong>Output:</strong> <code>6</code>
<strong>Explanation:</strong>&nbsp;[2,3] has the largest product 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong>&nbsp;The result cannot be 2, because [-2,-1] is not a subarray.</pre>

## Solutions:

```c++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        vector<int> maxValue (n, 0);
        vector<int> minValue (n, 0);
        
        maxValue[0] = nums[0];
        minValue[0] = nums[0];
        
        for (int i = 1; i < nums.size(); ++i) {
            maxValue[i] = max(nums[i], max(minValue[i-1] * nums[i], maxValue[i-1] * nums[i]));
            minValue[i] = min(nums[i], min(minValue[i-1] * nums[i], maxValue[i-1] * nums[i]));
        }
        
        int ret = maxValue[0];
        for (int i = 1; i < nums.size(); ++i) {
            ret = max(ret, maxValue[i]);
        }
        
        return ret;
    }
};
```

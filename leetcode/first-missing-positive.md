# 41. First Missing Positive

* *Difficulty: Hard*

* *Topics: Array*

* *Similar Questions:*

  * [Missing Number](missing-number.md)

  * [Find the Duplicate Number](find-the-duplicate-number.md)

  * [Find All Numbers Disappeared in an Array](find-all-numbers-disappeared-in-an-array.md)

  * [Couples Holding Hands](couples-holding-hands.md)

## Problem:

<p>Given an unsorted integer array, find the smallest missing&nbsp;positive integer.</p>

<p><strong>Example 1:</strong></p>

<pre>
Input: [1,2,0]
Output: 3
</pre>

<p><strong>Example 2:</strong></p>

<pre>
Input: [3,4,-1,1]
Output: 2
</pre>

<p><strong>Example 3:</strong></p>

<pre>
Input: [7,8,9,11,12]
Output: 1
</pre>

<p><strong>Note:</strong></p>

<p>Your algorithm should run in <em>O</em>(<em>n</em>) time and uses constant extra space.</p>

## Solutions:

```c++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            int pendingVal = nums[i];
            nums[i] = -1;
            while (pendingVal >= 1 && pendingVal <= n && nums[pendingVal - 1] != pendingVal) {
                swap(pendingVal, nums[pendingVal - 1]);
            }
        }
        
        for (int i = 1; i <= n; ++i) {
            if (nums[i-1] != i) return i;
        }
        return n+1;
    }
};
```

#### More concise solution
From [Grandyang] (https://www.cnblogs.com/grandyang/p/4395963.html) 
```c++
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {
                swap(nums[i], nums[nums[i] - 1]);
            }
        }
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
};
```

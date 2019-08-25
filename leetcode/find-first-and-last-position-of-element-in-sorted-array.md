# 34. Find First and Last Position of Element in Sorted Array

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [First Bad Version](first-bad-version.md)

## Problem:

<p>Given an array of integers <code>nums</code> sorted in ascending order, find the starting and ending position of a given <code>target</code> value.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of <em>O</em>(log <em>n</em>).</p>

<p>If the target is not found in the array, return <code>[-1, -1]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>Output:</strong> [3,4]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>Output:</strong> [-1,-1]</pre>

## Solutions:

```c++
bool searchLeft(vector<int>& nums, int index, int target) {
    return nums[index] >= target;
}

bool searchRight(vector<int>& nums, int index, int target) {
    return nums[index] > target || index == nums.size() - 1 || (nums[index] == target && nums[index + 1] > target);
}

class Solution {
public:
    typedef bool (*check) (vector<int>&, int, int);
    
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0)   return {-1, -1};
        int leftBound = search(nums, 0, nums.size() - 1, target, &searchLeft);
        int rightBound = search(nums, 0, nums.size() - 1, target, &searchRight);
        return {nums[leftBound] == target ? leftBound : - 1, nums[rightBound] == target ? rightBound : - 1};
    }
    
    int search(vector<int>& nums, int left, int right, int target, check fn) {
        while (left < right) {
            int mid = left + (right - left) /2 ;
            if ((*fn) (nums, mid, target)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return left;
    }
};
```

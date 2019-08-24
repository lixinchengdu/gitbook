# 34. Find First and Last Position of Element in Sorted Array

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [First Bad Version](./tests/find-first-and-last-position-of-element-in-sorted-array.md)

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
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector <int> ret;
        ret.push_back(lowBound(nums,target));
        ret.push_back(highBound(nums,target));
        return ret;
    }
    
    int lowBound(vector<int>& nums, int target)
    {
        int n = nums.size();
        int low = 0;
        int high = n-1;
        if (n == 0) return -1;
        while (low + 1 < high)
        {
            int mid = low + (high - low)/2;
            if (nums[mid] >= target)    high = mid;
            else low = mid;
        }
        if (nums[low] == target)    return low;
        else if (nums[high] == target)  return high;
        else return -1;
    }
     int highBound(vector<int>& nums, int target)
    {
        int n = nums.size();
        if (n == 0) return -1;
        int low = 0;
        int high = n-1;
        while (low + 1 < high)
        {
            int mid = low + (high - low)/2;
            if (nums[mid] <= target)    low = mid;
            else high = mid;
        }
        if (nums[high] == target)    return high;
        else if (nums[low] == target)  return low;
        else return -1;
    }
    
};
```

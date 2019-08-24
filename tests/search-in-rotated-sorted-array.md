# 33. Search in Rotated Sorted Array

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Search in Rotated Sorted Array II](./tests/search-in-rotated-sorted-array.md)

  * [Find Minimum in Rotated Sorted Array](./tests/search-in-rotated-sorted-array.md)

## Problem:

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., <code>[0,1,2,4,5,6,7]</code> might become <code>[4,5,6,7,0,1,2]</code>).</p>

<p>You are given a target value to search. If found in the array return its index, otherwise return <code>-1</code>.</p>

<p>You may assume no duplicate exists in the array.</p>

<p>Your algorithm&#39;s runtime complexity must be in the order of&nbsp;<em>O</em>(log&nbsp;<em>n</em>).</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>Output:</strong> -1</pre>

## Solutions:

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0)   return -1;
        return searchHelper (nums, 0, nums.size()-1, target);
    }
    
    int searchHelper (vector<int>& nums, int low, int high, int target)
    {
        if (low > high) return -1;
        int mid = (low + high)/2;
        if (nums[mid] == target) return mid;
        if (nums[low] < nums[high])
        {
            if (nums[mid] > target) return searchHelper(nums, low, mid-1, target);
            else return searchHelper (nums, mid+1, high, target);
        }
        else
        {
            int firstHalf = searchHelper (nums, low, mid-1, target);
            if (firstHalf != -1)    return firstHalf;
            else
            {
                return searchHelper (nums, mid+1, high, target);
            }
        }
    }
    
};
```

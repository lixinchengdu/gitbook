# 153. Find Minimum in Rotated Sorted Array

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md)

  * [Find Minimum in Rotated Sorted Array II](find-minimum-in-rotated-sorted-array-ii.md)

## Problem:

<p>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.</p>

<p>(i.e., &nbsp;<code>[0,1,2,4,5,6,7]</code>&nbsp;might become &nbsp;<code>[4,5,6,7,0,1,2]</code>).</p>

<p>Find the minimum element.</p>

<p>You may assume no duplicate exists in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,4,5,1,2] 
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,5,6,7,0,1,2]
<strong>Output:</strong> 0
</pre>

## Solutions:

```c++
class Solution {
public:
    typedef bool (*check)(vector<int>&, int index);
    
    static bool checkMin(vector<int>& nums, int index) {
        return nums[index] < nums[0];
    }
    
    int findMin(vector<int>& nums) {
        if (nums.size() == 0)   return -1;
        if (nums.size() == 1)   return nums[0];
        if (nums[0] < nums.back())  return nums[0];
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left)/2;
            if (checkMin(nums, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        
        return nums[left];
    }
};
```

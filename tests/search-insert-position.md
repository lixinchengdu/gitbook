# 35. Search Insert Position

* *Difficulty: Easy*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [First Bad Version](./tests/search-insert-position.md)

## Problem:

<p>Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You may assume no duplicates in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 5
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 2
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 7
<strong>Output:</strong> 4
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> [1,3,5,6], 0
<strong>Output:</strong> 0
</pre>

## Solutions:

```c++
int binarySearch (vector<int>& nums, int target, int low, int high);
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        return binarySearch (nums, target, 0, nums.size()-1);
    }
};

int binarySearch (vector<int>& nums, int target, int low, int high)
{
    if (high < low)
        return low;
    int mid = (low+high)/2;
    if (nums[mid] == target)
        return mid;
    else
    {
       if (target > nums[mid])
        return binarySearch(nums, target, mid+1, high);
        else
        return binarySearch(nums, target, low, mid-1);
        
    }
}
```

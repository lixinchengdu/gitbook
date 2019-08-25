# 162. Find Peak Element

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Peak Index in a Mountain Array](peak-index-in-a-mountain-array.md)

## Problem:

<p>A peak element is an element that is greater than its neighbors.</p>

<p>Given an input array <code>nums</code>, where <code>nums[i] &ne; nums[i+1]</code>, find a peak element and return its index.</p>

<p>The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.</p>

<p>You may imagine that <code>nums[-1] = nums[n] = -&infin;</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[1,2,3,1]</code>
<strong>Output:</strong> 2
<strong>Explanation:</strong> 3 is a peak element and your function should return the index number 2.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <strong>nums</strong> = <code>[</code>1,2,1,3,5,6,4]
<strong>Output:</strong> 1 or 5 
<strong>Explanation:</strong> Your function can return either index number 1 where the peak element is 2, 
&nbsp;            or index number 5 where the peak element is 6.
</pre>

<p><strong>Note:</strong></p>

<p>Your solution should be in logarithmic complexity.</p>

## Solutions:

```c++
class Solution {
public:
    int findPeakElement(vector<int>& nums) { // this problem does not eliminate the scenario [1]
        int left = 0;
        int right = nums.size() - 1;
        while (left + 1 < right) {
            int mid = left + (right - left)/2;
            if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid + 1])   return mid;
            if (nums[mid] < nums[mid - 1]) right = mid;
            else left = mid;
        }
        
        if (left == 0) {
            if (nums.size() > left + 1 && nums[left + 1] < nums[left])   return left;
            else return right;
        } else {
            if (nums.size() > left + 1 && left -1 >= 0 && nums[left] > nums[left - 1] && nums[left] > nums[left + 1]) return left;
            else return right;
        }
    }
};
```

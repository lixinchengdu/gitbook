# 215. Kth Largest Element in an Array

* *Difficulty: Medium*

* *Topics: Divide and Conquer, Heap*

* *Similar Questions:*

  * [Wiggle Sort II](wiggle-sort-ii.md)

  * [Top K Frequent Elements](top-k-frequent-elements.md)

  * [Third Maximum Number](third-maximum-number.md)

  * [Kth Largest Element in a Stream](kth-largest-element-in-a-stream.md)

  * [K Closest Points to Origin](k-closest-points-to-origin.md)

## Problem:

<p>Find the <strong>k</strong>th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,1,5,6,4] </code>and k = 2
<strong>Output:</strong> 5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,3,1,2,4,5,5,6] </code>and k = 4
<strong>Output:</strong> 4</pre>

<p><strong>Note: </strong><br />
You may assume k is always valid, 1 &le; k &le; array&#39;s length.</p>

## Solutions:

```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        return helper(nums, 0, nums.size() - 1, nums.size() - k);
    }
    
    int helper(vector<int>& nums, int left, int right, int k) {
        int oldLeft = left;
        int oldRight = right;
        if (left == right && left == k) return nums[k];
        
        int pivotal = nums[left];
        while (left <= right) {
            while (left <= right && nums[left] < pivotal) { // if the operation is <=, the program would run in infinite loop. Consider [2, 1], the program could not progress. 
                ++left;
            }

            while (left <= right && nums[right] > pivotal) {
                --right;
            }

            if (left <= right) {
                swap(nums[left], nums[right]);
                ++left;
                --right;
            }
        }
        
        if (k <= right) {
            return helper(nums, oldLeft, right, k);
        } else if (k >= left) {
            return helper(nums, left, oldRight, k);
        } else {
            return nums[k];
        }
        
    }
};
```

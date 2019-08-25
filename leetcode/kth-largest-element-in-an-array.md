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

## Proof Sketch

The post loop-invariant is that: 
1. All elements left to `left` (exclusive) is smaller or equal to `pivotal`.
2. All elements right to `right` (exclusive) is greater or equal to `pivotal`. 

Therefore, after the crossing of `left` and `right`, all elements right/left to `left`/`right` (inclusive) are greater/smaller or equal to `pivotal`. It is possible that after crossing, `left` and `right` are **NOT** adjacent when both `left` and `right` are pointed to `pivotal` in the last iteration. Therefore, `else {return nums[k];}` is essential when `k` happens to be the `pivotal`.

## Common Pitfalls

1. `while (left < right)`. The loop invariant may not hold any more. For example `[5, 6, 4]`, after first iteration, both `left` and `right` point to the middle element. The while loop exists but `6` is not equal to `pivotal`.  

2. `pivotal` is not equal to any element in the array. In this case, it is possible to result in infinite recursions. To avoid this situation, the next pitfall should also be avoided. 

3. `nums[left] <= pivotal`. In this case, the infinite-recursion happens for some cases like `[2, 1]`. The edge case is evil because swap happens at the boundary which makes no progress. 

If the last two pitfalls are avoided, it is guaranteed that the algorithm would make progress because one non-boundary swap is guaranteed. 

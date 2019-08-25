# 33. Search in Rotated Sorted Array

* *Difficulty: Medium*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Search in Rotated Sorted Array II](search-in-rotated-sorted-array-ii.md)

  * [Find Minimum in Rotated Sorted Array](find-minimum-in-rotated-sorted-array.md)

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
    /**
     * @param A: an integer rotated sorted array
     * @param target: an integer to be searched
     * @return: an integer
     */
    int search(vector<int> &A, int target) {
        // write your code here
        if (A.size() == 0)  return -1;
        int left = 0;
        int right = A.size() - 1;
        while (left + 1 < right) {
            int mid = left + ((right - left) >> 1);
            if (A[mid] == target)  return mid;
            if (A[left] < A[right]) {
                if (A[mid] < target) {
                    left = mid;
                } else {
                    right = mid;
                }
            } else {
                if (A[mid] > A[left]) {
                    if (A[mid] > target && A[left] <= target) {
                        right = mid;
                    } else {
                        left = mid;
                    }
                } else {
                    if (A[mid] < target && A[right] >= target) {
                        left = mid;
                    } else {
                        right = mid;
                    }
                }
            }
        }
        
        
        if (A[left] == target)  return left;
        if (A[right] == target) return right;
        return -1;
    }
};
```

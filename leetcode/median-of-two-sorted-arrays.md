# 4. Median of Two Sorted Arrays

* *Difficulty: Hard*

* *Topics: Array, Binary Search, Divide and Conquer*

* *Similar Questions:*

## Problem:

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>

<p><b>Example 1:</b></p>

<pre>
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
</pre>

<p><b>Example 2:</b></p>

<pre>
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
</pre>

## Solutions:

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        int n = n1 + n2;
        if (n % 2 == 0) {
            return (smallK(n/2, nums1, 0, n1 - 1, nums2, 0, n2 - 1) + smallK(n/2 + 1, nums1, 0, n1 - 1, nums2, 0, n2 - 1)) / double(2);
        } else {
            return smallK(n/2 + 1, nums1, 0, n1 - 1, nums2, 0, n2 - 1);
        }
    }
    
    // k starting from 1
    int smallK(int k, vector<int>& nums1, int left1, int right1, vector<int>& nums2, int left2, int right2) {
        if (left1 > right1) return nums2[left2 + k - 1];
        if (left2 > right2) return nums1[left1 + k - 1];
        
        if (k == 1) {
            return min(nums1[left1], nums2[left2]);
        }
        
        if (k/2 > right1 - left1 + 1) {
            return smallK(k - k/2, nums1, left1, right1, nums2, left2 + k/2, right2);
        }
        
        if (k/2 > right2 - left2 + 1) {
            return smallK(k - k/2, nums1, left1 + k/2, right1, nums2, left2, right2);
        }
        
        if (nums1[left1 + k/2 - 1] < nums2[left2 + k/2 - 1]) {
            return smallK(k - k/2, nums1, left1 + k/2, right1, nums2, left2, right2);
        } else {
            return smallK(k - k/2, nums1, left1, right1, nums2, left2 + k/2, right2);
        }    
    }
};
```

# 88. Merge Sorted Array

* *Difficulty: Easy*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)

  * [Squares of a Sorted Array](squares-of-a-sorted-array.md)

  * [Interval List Intersections](interval-list-intersections.md)

## Problem:

<p>Given two sorted integer arrays <em>nums1</em> and <em>nums2</em>, merge <em>nums2</em> into <em>nums1</em> as one sorted array.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of elements initialized in <em>nums1</em> and <em>nums2</em> are <em>m</em> and <em>n</em> respectively.</li>
	<li>You may assume that <em>nums1</em> has enough space (size that is greater or equal to <em>m</em> + <em>n</em>) to hold additional elements from <em>nums2</em>.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

<strong>Output:</strong>&nbsp;[1,2,2,3,5,6]
</pre>

## Solutions:

```c++
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        nums1.resize(m + n);
        int cur = m + n - 1;
        int i1 = m - 1;
        int i2 = n - 1;
        
        while (i1 >= 0 || i2 >= 0) {
            if (i1 < 0) {
                nums1[cur--] = nums2[i2--];
            } else if (i2 < 0) {
                break;
            } else {
                if (nums1[i1] >= nums2[i2]) {
                    nums1[cur--] = nums1[i1--];
                } else {
                    nums1[cur--] = nums2[i2--];
                }
            }
        }
    }
};
```

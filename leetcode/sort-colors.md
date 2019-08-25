# 75. Sort Colors

* *Difficulty: Medium*

* *Topics: Array, Two Pointers, Sort*

* *Similar Questions:*

  * [Sort List](sort-list.md)

  * [Wiggle Sort](wiggle-sort.md)

  * [Wiggle Sort II](wiggle-sort-ii.md)

## Problem:

<p>Given an array with <em>n</em> objects colored red, white or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>&nbsp;</strong>so that objects of the same color are adjacent, with the colors in the order red, white and blue.</p>

<p>Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.</p>

<p><strong>Note:</strong>&nbsp;You are not suppose to use the library&#39;s sort function for this problem.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A rather straight forward solution is a two-pass algorithm using counting sort.<br />
	First, iterate the array counting number of 0&#39;s, 1&#39;s, and 2&#39;s, then overwrite array with total number of 0&#39;s, then 1&#39;s and followed by 2&#39;s.</li>
	<li>Could you come up with a&nbsp;one-pass algorithm using only constant space?</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        
        for (int i = left; i <= right; ) { // not include ++i to continue swap if necessary; otherwise [1, 2, 0] fails; 
            if (nums[i] == 0 && i != left) { // remember the second check; otherwise [] would fail
                swap(nums[i], nums[left]);
                ++left;
            } else if (nums[i] == 2 && i != right) { // remember the second check; otherwise [] would fail
                swap(nums[i], nums[right]);
                --right;
            } else {
                ++i;
            }
        }
    }
};
```

# 287. Find the Duplicate Number

* *Difficulty: Medium*

* *Topics: Array, Two Pointers, Binary Search*

* *Similar Questions:*

  * [First Missing Positive](./tests/find-the-duplicate-number.md)

  * [Single Number](./tests/find-the-duplicate-number.md)

  * [Linked List Cycle II](./tests/find-the-duplicate-number.md)

  * [Missing Number](./tests/find-the-duplicate-number.md)

  * [Set Mismatch](./tests/find-the-duplicate-number.md)

## Problem:

<p>Given an array <i>nums</i> containing <i>n</i> + 1 integers where each integer is between 1 and <i>n</i> (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[1,3,4,2,2]</code>
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [3,1,3,4,2]
<b>Output:</b> 3</pre>

<p><b>Note:</b></p>

<ol>
	<li>You <b>must not</b> modify the array (assume the array is read only).</li>
	<li>You must use only constant, <i>O</i>(1) extra space.</li>
	<li>Your runtime complexity should be less than <em>O</em>(<em>n</em><sup>2</sup>).</li>
	<li>There is only one duplicate number in the array, but it could be repeated more than once.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int pre = -1;
        for (const auto& num : nums) {
            if (num == pre) return num;
            pre = num;
        }
    }
};
```

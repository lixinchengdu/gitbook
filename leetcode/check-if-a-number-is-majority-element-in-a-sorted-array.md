# 1102. Check If a Number Is Majority Element in a Sorted Array

* *Difficulty: Easy*

* *Topics: Array, Binary Search*

* *Similar Questions:*

  * [Majority Element](majority-element.md)

  * [Majority Element II](majority-element-ii.md)

## Problem:

<p>Given an array <code>nums</code> sorted in <strong>non-decreasing</strong> order, and a number <code>target</code>, return <code>True</code> if and only if <code>target</code> is a majority element.</p>

<p>A <em>majority element</em> is an element that appears <strong>more than <code>N/2</code></strong> times in an array of length <code>N</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[2,4,5,5,5,5,5,6,6]</span>, target = <span id="example-input-1-2">5</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 &gt; 9/2 is true.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[10,100,101,101]</span>, target = <span id="example-input-2-2">101</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 &gt; 4/2 is false.
</pre>

<p>&nbsp;</p>

<p><span><strong>Note:</strong></span></p>

<ol>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^9</code></li>
	<li><code>1 &lt;= target &lt;= 10^9</code></li>
</ol>

## Solutions:

```c++
class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        if (nums.size() == 0)   return false;
        int l1 = 0;
        int l2 = 0;
        int r1 = nums.size() - 1;
        int r2 = nums.size() - 1;
        
        while (true) {   
            if (l1 <= r1) {
                int mid = l1 + (r1 - l1) / 2;
                if (nums[mid] >= target) {
                    r1 = mid;
                } else {
                    l1 = mid + 1;
                }
            }
            
            if (l1 > r1)    return false;
            
            if (l2 <= r2) {
                int mid = r2 - (r2 - l2) / 2;
                if (nums[mid] <= target) {
                    l2 = mid;
                } else {
                    r2 = mid - 1;
                }
            }
            if (l2 > r2)    return false;
            
            if (l2 - r1 + 1 > int(nums.size() / 2)) { // trap! 
                return true;
            }
            if (r2 - l1 + 1 <= int(nums.size() / 2)) { // trap!
                return false;
            }
        }
    }
};
```

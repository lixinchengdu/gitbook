# 349. Intersection of Two Arrays

* *Difficulty: Easy*

* *Topics: Hash Table, Two Pointers, Binary Search, Sort*

* *Similar Questions:*

  * [Intersection of Two Arrays II](intersection-of-two-arrays-ii.md)

## Problem:

<p>Given two arrays, write a function to compute their intersection.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-1-1">[1,2,2,1]</span>, nums2 = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums1 = <span id="example-input-2-1">[4,9,5]</span>, nums2 = <span id="example-input-2-2">[9,4,9,8,4]</span>
<strong>Output: </strong><span id="example-output-2">[9,4]</span></pre>
</div>

<p><b>Note:</b></p>

<ul>
	<li>Each element in the result must be unique.</li>
	<li>The result can be in any order.</li>
</ul>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> nums (nums1.begin(), nums1.end());
        unordered_set<int> ret;
        for (auto num : nums2) {
            if (nums.count(num) > 0) {
                ret.insert(num);
            }
        }
        
        return vector<int>(ret.begin(), ret.end());
    }
};
```

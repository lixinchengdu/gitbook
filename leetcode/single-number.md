# 136. Single Number

* *Difficulty: Easy*

* *Topics: Hash Table, Bit Manipulation*

* *Similar Questions:*

  * [Single Number II](single-number-ii.md)

  * [Single Number III](single-number-iii.md)

  * [Missing Number](missing-number.md)

  * [Find the Duplicate Number](find-the-duplicate-number.md)

  * [Find the Difference](find-the-difference.md)

## Problem:

<p>Given a <strong>non-empty</strong>&nbsp;array of integers, every element appears <em>twice</em> except for one. Find that single one.</p>

<p><strong>Note:</strong></p>

<p>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,1,2,1,2]
<strong>Output:</strong> 4
</pre>

## Solutions:

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ret = 0;
        for (auto num : nums) {
            ret ^= num;
        }
        
        return ret;
    }
};
```

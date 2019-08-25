# 137. Single Number II

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Single Number](single-number.md)

  * [Single Number III](single-number-iii.md)

## Problem:

<p>Given a <strong>non-empty</strong>&nbsp;array of integers, every element appears <em>three</em> times except for one, which appears exactly once. Find that single one.</p>

<p><strong>Note:</strong></p>

<p>Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,2,3,2]
<strong>Output:</strong> 3
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [0,1,0,1,0,1,99]
<strong>Output:</strong> 99</pre>

## Solutions:

```c++
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0;
        int tens = 0;
        
        for (auto num : nums) {
            ones = ones ^ num;
   
            int carry = (~ones) & num;
            tens = tens ^ carry;
            
            int mask = ones & tens;
            ones = ones & (~mask);
            tens = tens & (~mask);
        }
        
        return ones;
    }
};
```

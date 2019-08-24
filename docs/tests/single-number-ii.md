# 137. Single Number II

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

  * [Single Number](./tests/single-number-ii.md)

  * [Single Number III](./tests/single-number-ii.md)

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
        int newOnes = 0;
        int twos = 0;
        for (auto num: nums)
        {
            newOnes = ones ^ num; //cout << bool(newOnes) << endl;
            twos = ((~newOnes) & num)|twos; //cout << bool(twos) << endl;
            ones = newOnes ^ (newOnes&twos); //cout << bool(ones) << endl;
            twos = (twos) ^ (newOnes&twos); //cout << bool(twos) << endl;
        }
        return ones;
    }
};
```

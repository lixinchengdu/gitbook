# 268. Missing Number

* *Difficulty: Easy*

* *Topics: Array, Math, Bit Manipulation*

* *Similar Questions:*

  * [First Missing Positive](first-missing-positive.md)

  * [Single Number](single-number.md)

  * [Find the Duplicate Number](find-the-duplicate-number.md)

  * [Couples Holding Hands](couples-holding-hands.md)

## Problem:

<p>Given an array containing <i>n</i> distinct numbers taken from <code>0, 1, 2, ..., n</code>, find the one that is missing from the array.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [3,0,1]
<b>Output:</b> 2
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [9,6,4,2,3,5,7,0,1]
<b>Output:</b> 8
</pre>

<p><b>Note</b>:<br />
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?</p>
## Solutions:

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            kick(nums, i);
        }
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] != i) {
                return i;
            }
        }
        
        return n;
    }
    
    void kick(vector<int>& nums, int i) {
        int val = nums[i];
        nums[i] = -1;
        
        while (val < nums.size() && val >= 0) {
            swap(val, nums[val]);
        }
    }
};
```

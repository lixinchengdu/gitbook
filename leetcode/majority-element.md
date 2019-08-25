# 169. Majority Element

* *Difficulty: Easy*

* *Topics: Array, Divide and Conquer, Bit Manipulation*

* *Similar Questions:*

  * [Majority Element II](majority-element-ii.md)

  * [Check If a Number Is Majority Element in a Sorted Array](check-if-a-number-is-majority-element-in-a-sorted-array.md)

## Problem:

<p>Given an array of size <i>n</i>, find the majority element. The majority element is the element that appears <b>more than</b> <code>&lfloor; n/2 &rfloor;</code> times.</p>

<p>You may assume that the array is non-empty and the majority element always exist in the array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [3,2,3]
<strong>Output:</strong> 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [2,2,1,1,1,2,2]
<strong>Output:</strong> 2
</pre>

## Solutions:

```c++
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 0)   return -1;
        int count = 0;
        int majority = nums[0];
        for (auto num : nums) {
            if (num == majority) {
                ++count;
            } else {
                if (--count == 0) {
                    majority = num;
                    count = 1;
                }
            }
        }
        
        return majority;
    }
};
```

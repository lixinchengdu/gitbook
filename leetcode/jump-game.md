# 55. Jump Game

* *Difficulty: Medium*

* *Topics: Array, Greedy*

* *Similar Questions:*

  * [Jump Game II](jump-game-ii.md)

## Problem:

<p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Determine if you are able to reach the last index.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [2,3,1,1,4]
<strong>Output:</strong> true
<strong>Explanation:</strong> Jump 1 step from index 0 to 1, then 3 steps to the last index.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [3,2,1,0,4]
<strong>Output:</strong> false
<strong>Explanation:</strong> You will always arrive at index 3 no matter what. Its maximum
&nbsp;            jump length is 0, which makes it impossible to reach the last index.
</pre>

## Solutions:

```c++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 0)   return false;
        int distance = 0;
        for (int i = 0; i <= distance; ++i) {
            distance = max(distance, i + nums[i]);
            if (distance >= nums.size() - 1) return true;
        }
        
        return false;
    }
};
```

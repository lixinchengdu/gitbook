# 45. Jump Game II

* *Difficulty: Hard*

* *Topics: Array, Greedy*

* *Similar Questions:*

  * [Jump Game](jump-game.md)

## Problem:

<p>Given an array of non-negative integers, you are initially positioned at the first index of the array.</p>

<p>Each element in the array represents your maximum jump length at that position.</p>

<p>Your goal is to reach the last index in the minimum number of jumps.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,3,1,1,4]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.</pre>

<p><strong>Note:</strong></p>

<p>You can assume that you can always reach the last index.</p>

## Solutions:

```c++
class Solution {
public:
    int jump(vector<int>& nums) {
        int start = 0;
        int reachable = 0;
        int count = 0;
        for (;;) {
            if (reachable >= nums.size() - 1)   return count;
            int nextReachable = 0;
            for (int i = start; i <= reachable; ++i) {
                nextReachable = max(nextReachable, i + nums[i]);
            }
            start = reachable + 1;
            reachable = nextReachable;
            ++count;
        }
        
    }
};
```

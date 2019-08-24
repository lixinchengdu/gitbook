# 494. Target Sum

* *Difficulty: Medium*

* *Topics: Dynamic Programming, Depth-first Search*

* *Similar Questions:*

  * [Expression Add Operators](./tests/target-sum.md)

## Problem:

<p>
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols <code>+</code> and <code>-</code>. For each integer, you should choose one from <code>+</code> and <code>-</code> as its new symbol.
</p> 

<p>Find out how many ways to assign symbols to make sum of integers equal to target S.  
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums is [1, 1, 1, 1, 1], S is 3. 
<b>Output:</b> 5
<b>Explanation:</b> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array is positive and will not exceed 20. </li>
<li>The sum of elements in the given array will not exceed 1000.</li>
<li>Your output answer is guaranteed to be fitted in a 32-bit integer.</li>
</ol>
</p>
## Solutions:

```c++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        return findTargetHelper (nums, S, 0, nums.size());
    }
    
    int findTargetHelper (vector <int>& nums, int S, int pos, int n)
    {
        if (n == pos) return 0;
        if (n == pos + 1) {if (nums[pos] == S && S == 0)  return 2; return abs(nums[pos]) == abs(S)? 1:0;}
        pair <int, int> dataPoint;
        dataPoint.first = S;
        dataPoint.second = pos;
        if (immediateResult.find(dataPoint) != immediateResult.end())   return immediateResult[dataPoint];
        int result;
        result = findTargetHelper (nums, S - nums[pos], pos + 1, n) + findTargetHelper (nums, S + nums[pos], pos + 1, n);
        pair <int, int> immediate;
        immediate.first = S;
        immediate.second = pos;
        immediateResult[immediate] = result;
        return result;
    }
    map <pair<int, int>, int> immediateResult;
    
};
```

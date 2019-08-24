# 523. Continuous Subarray Sum

* *Difficulty: Medium*

* *Topics: Math, Dynamic Programming*

* *Similar Questions:*

  * [Subarray Sum Equals K](./tests/continuous-subarray-sum.md)

## Problem:

<p>Given a list of <b>non-negative</b> numbers and a target <b>integer</b> k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of <b>k</b>, that is, sums up to n*k where n is also an <b>integer</b>.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [23, 2, 4, 6, 7],  k=6
<b>Output:</b> True
<b>Explanation:</b> Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [23, 2, 6, 4, 7],  k=6
<b>Output:</b> True
<b>Explanation:</b> Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The length of the array won&#39;t exceed 10,000.</li>
	<li>You may assume the sum of all the numbers is in the range of a signed 32-bit integer.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        set <int>   sumSet;
        int sum = 0;
       // int prevprevSum;
        int prevSum;
        for (auto num: nums)
        {
            prevSum = sum;
            sum += num;
            if (k!=0)
                sum %= k;
            if (sumSet.find(sum) != sumSet.end())   return true;
            sumSet.insert(prevSum);
        }
        return false;
    }
};
```

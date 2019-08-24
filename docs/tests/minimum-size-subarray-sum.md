# 209. Minimum Size Subarray Sum

* *Difficulty: Medium*

* *Topics: Array, Two Pointers, Binary Search*

* *Similar Questions:*

  * [Minimum Window Substring](./tests/minimum-size-subarray-sum.md)

  * [Maximum Size Subarray Sum Equals k](./tests/minimum-size-subarray-sum.md)

  * [Maximum Length of Repeated Subarray](./tests/minimum-size-subarray-sum.md)

## Problem:

<p>Given an array of <strong>n</strong> positive integers and a positive integer <strong>s</strong>, find the minimal length of a <b>contiguous</b> subarray of which the sum &ge; <strong>s</strong>. If there isn&#39;t one, return 0 instead.</p>

<p><strong>Example:&nbsp;</strong></p>

<pre>
<strong>Input:</strong> <code>s = 7, nums = [2,3,1,2,4,3]</code>
<strong>Output:</strong> 2
<strong>Explanation: </strong>the subarray <code>[4,3]</code> has the minimal length under the problem constraint.</pre>

<div class="spoilers"><b>Follow up:</b></div>

<div class="spoilers">If you have figured out the <i>O</i>(<i>n</i>) solution, try coding another solution of which the time complexity is <i>O</i>(<i>n</i> log <i>n</i>).&nbsp;</div>

## Solutions:

```c++
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int sum = 0;
        int ret = INT_MAX;
        for (int r = 0, l = -1; r < nums.size(); ++r) {
            sum += nums[r];
           // if (sum >= s) {
           //     ret = min(ret, r - l);
           // } 
            while (sum >= s) {
                //if (sum >= s) {
                    ret = min(ret, r - l);
               // }
                sum -= nums[++l];
            }
        }
        return ret == INT_MAX? 0 : ret;
    }
};
```

# 209. Minimum Size Subarray Sum

* *Difficulty: Medium*

* *Topics: Array, Two Pointers, Binary Search*

* *Similar Questions:*

  * [Minimum Window Substring](minimum-window-substring.md)

  * [Maximum Size Subarray Sum Equals k](maximum-size-subarray-sum-equals-k.md)

  * [Maximum Length of Repeated Subarray](maximum-length-of-repeated-subarray.md)

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
        int left = 0;
        int len = INT_MAX;
        
        for (int right = 0; right < nums.size(); ++right) {
            sum += nums[right];
            
            while (left <= right && sum >= s) {
                len = min(len, right - left + 1);
                sum -= nums[left];
                ++left;
            }
            
        }
        
        return len == INT_MAX ? 0 : len;
    }
};
```

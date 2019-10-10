# 674. Longest Continuous Increasing Subsequence

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence.md)

  * [Minimum Window Subsequence](minimum-window-subsequence.md)

## Problem:

<p>
Given an unsorted array of integers, find the length of longest <code>continuous</code> increasing subsequence (subarray).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,3,5,4,7]
<b>Output:</b> 3
<b>Explanation:</b> The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [2,2,2,2,2]
<b>Output:</b> 1
<b>Explanation:</b> The longest continuous increasing subsequence is [2], its length is 1. 
</pre>
</p>

<p><b>Note:</b>
Length of the array will not exceed 10,000.
</p>
## Solutions:

```c++
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        if (nums.size() == 0)   return 0;
        int left = 0;
        int ret = 1;
        int right = 1;
        for (right = 1; right < nums.size(); ++right) {
            if (nums[right] > nums[right - 1]) {
                ret = max(ret, right - left + 1);
            } else {
                left = right;
            }
        }
        
        ret = max(ret, right - left);
        
        return ret;
    }
};
```

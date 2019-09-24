# 300. Longest Increasing Subsequence

* *Difficulty: Medium*

* *Topics: Binary Search, Dynamic Programming*

* *Similar Questions:*

  * [Increasing Triplet Subsequence](increasing-triplet-subsequence.md)

  * [Russian Doll Envelopes](russian-doll-envelopes.md)

  * [Maximum Length of Pair Chain](maximum-length-of-pair-chain.md)

  * [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence.md)

  * [Minimum ASCII Delete Sum for Two Strings](minimum-ascii-delete-sum-for-two-strings.md)

## Problem:

<p>Given an unsorted array of integers, find the length of longest increasing subsequence.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[10,9,2,5,3,7,101,18]
</code><b>Output: </b>4 
<strong>Explanation: </strong>The longest increasing subsequence is <code>[2,3,7,101]</code>, therefore the length is <code>4</code>. </pre>

<p><strong>Note: </strong></p>

<ul>
	<li>There may be more than one LIS combination, it is only necessary for you to return the length.</li>
	<li>Your algorithm should run in O(<i>n<sup>2</sup></i>) complexity.</li>
</ul>

<p><b>Follow up:</b> Could you improve it to O(<i>n</i> log <i>n</i>) time complexity?</p>

## Solutions:

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0)   return 0;
        map<int, int> dp;
        for (auto& num : nums) {
            if (dp.empty()) {
                dp[num] = 1;
                continue;
            }
            if (dp.count(num))  continue;
            auto it = dp.lower_bound(num);
            if (it == dp.end()) {
                dp[num] = prev(it)->second + 1;
            } else {
                dp[num] = it->second;
                dp.erase(it);
            }
        }
        
        return dp.rbegin()->second;
        
    }
};
```

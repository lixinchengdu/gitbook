# 368. Largest Divisible Subset

* *Difficulty: Medium*

* *Topics: Math, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a set of <b>distinct</b> positive integers, find the largest subset such that every pair (S<sub>i</sub>, S<sub>j</sub>) of elements in this subset satisfies:</p>

<p>S<sub>i</sub> % S<sub>j</sub> = 0 or S<sub>j</sub> % S<sub>i</sub> = 0.</p>

<p>If there are multiple solutions, return any subset is fine.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-1">[1,2] </span>(of course, [1,3] will also be ok)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,4,8]</span>
<strong>Output: </strong><span id="example-output-2">[1,2,4,8]</span>
</pre>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        if (nums.size() == 0)   return {}; // this is essential; otherwiseret.push_back(nums[index]); is incorrect
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<int> dp(n, 1);
        
        for (int i = 1; i < nums.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[i] % nums[j] == 0) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
        }
        
        int index = 0;
        int maxVal = 0;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (dp[i] > maxVal) {
                index = i;
                maxVal = dp[i];
            }
        }
        
        vector<int> ret;
        ret.push_back(nums[index]);
        --index;
        while (index >= 0) {
            if (ret.back() % nums[index] == 0 && dp[index] +  ret.size() == maxVal) {
                ret.push_back(nums[index]);
            }
            
            --index;
        }
        
        return ret;
        
    }
};
```

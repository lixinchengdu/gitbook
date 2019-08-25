# 18. 4Sum

* *Difficulty: Medium*

* *Topics: Array, Hash Table, Two Pointers*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [3Sum](3sum.md)

  * [4Sum II](4sum-ii.md)

## Problem:

<p>Given an array <code>nums</code> of <em>n</em> integers and an integer <code>target</code>, are there elements <em>a</em>, <em>b</em>, <em>c</em>, and <em>d</em> in <code>nums</code> such that <em>a</em> + <em>b</em> + <em>c</em> + <em>d</em> = <code>target</code>? Find all unique quadruplets in the array which gives the sum of <code>target</code>.</p>

<p><strong>Note:</strong></p>

<p>The solution set must not contain duplicate quadruplets.</p>

<p><strong>Example:</strong></p>

<pre>
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        if (nums.size() < 4)    return {};
        sort(nums.begin(), nums.end());
        
        vector<vector<int>> ret;
        for (int a = 0; a < nums.size() - 3; ++a) {
            if (a > 0 && nums[a] == nums[a - 1])    continue;
            for (int b = a + 1; b < nums.size() - 2; ++b) {
                if (b > a + 1 && nums[b] == nums[b-1])  continue;
                int c = b + 1;
                int d = nums.size() - 1;
                while (c < d) {
                    int val = nums[a] + nums[b] + nums[c] + nums[d];
                    if (val == target) {
                        ret.push_back({nums[a], nums[b], nums[c], nums[d]});
                        do {
                        ++c;
                        --d;
                        } while (c < d && nums[c] == nums[c-1] && nums[d] == nums[d+1]);
                    } else if (val < target) {
                        ++c;
                    } else {
                        --d;
                    }
                }
            }
        }
        
        return ret;
        
    }
};
```

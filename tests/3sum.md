# 15. 3Sum

* *Difficulty: Medium*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [Two Sum](./tests/3sum.md)

  * [3Sum Closest](./tests/3sum.md)

  * [4Sum](./tests/3sum.md)

  * [3Sum Smaller](./tests/3sum.md)

## Problem:

<p>Given an array <code>nums</code> of <em>n</em> integers, are there elements <em>a</em>, <em>b</em>, <em>c</em> in <code>nums</code> such that <em>a</em> + <em>b</em> + <em>c</em> = 0? Find all unique triplets in the array which gives the sum of zero.</p>

<p><strong>Note:</strong></p>

<p>The solution set must not contain duplicate triplets.</p>

<p><strong>Example:</strong></p>

<pre>
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (i - 1 >= 0 && nums[i] == nums[i-1]) continue;
            int left = i + 1;
            int right = nums.size() - 1;
            for (left = i + 1; left < right; ++left) {
                if (left != (i + 1) && nums[left] == nums[left -1] ) continue;
                while (left + 1 < right && nums[i] + nums[left] + nums[right] > 0) right --; 
                    if (nums[i] + nums[left] + nums[right] == 0) {
                        ret.push_back({nums[i], nums[left], nums[right]});
                    }
            }
        }
        return ret;
    }
};
```

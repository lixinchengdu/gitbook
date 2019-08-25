# 15. 3Sum

* *Difficulty: Medium*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [3Sum Closest](3sum-closest.md)

  * [4Sum](4sum.md)

  * [3Sum Smaller](3sum-smaller.md)

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
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i-1]) continue; // deduplication
            int sum = -nums[i];
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                if (nums[left] + nums[right] == sum) {
                    if (result.size() == 0 || result.back()[1] != nums[left] || result.back()[2] != nums[right]) // deduplication
                        result.push_back({nums[i], nums[left], nums[right]});
                    left++;
                    right--;
                } else if (nums[left] + nums[right] > sum) {
                    right--;
                } else {
                    left++;
                }
            }
        }
        
        return result;
    }
};
```

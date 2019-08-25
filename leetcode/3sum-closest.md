# 16. 3Sum Closest

* *Difficulty: Medium*

* *Topics: Array, Two Pointers*

* *Similar Questions:*

  * [3Sum](3sum.md)

  * [3Sum Smaller](3sum-smaller.md)

## Problem:

<p>Given an array <code>nums</code> of <em>n</em> integers and an integer <code>target</code>, find three integers in <code>nums</code>&nbsp;such that the sum is closest to&nbsp;<code>target</code>. Return the sum of the three integers. You may assume that each input would have exactly one solution.</p>

<p><strong>Example:</strong></p>

<pre>
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

## Solutions:

```c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        if (nums.size() < 3)    return 0;
        int ret = nums[0] + nums[1] + nums[2];
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size() - 2; ++i) {
            int left = i + 1;
            int right = nums.size() - 1;
            
            while (left < right) {
                int diff = (nums[i] + nums[left] + nums[right] - target);
                if (abs(diff) < abs(ret - target)) {
                    ret = nums[i] + nums[left] + nums[right];
                }
                if (diff == 0)  return ret;
                if (diff < 0) {
                    ++left;
                } else {
                    --right;
                }
            }
        }
        
        return ret;
    }
};
```

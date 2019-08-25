# 90. Subsets II

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Subsets](subsets.md)

## Problem:

<p>Given a collection of integers that might contain duplicates, <strong><em>nums</em></strong>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,2]
<strong>Output:</strong>
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        
        vector<int> path;
        vector<vector<int>> ret;
        
        helper(nums, 0, path, ret);
            
        return ret;
    }
    
    void helper(vector<int>& nums, int pos, vector<int>& path, vector<vector<int>>& ret) {
        if (pos == nums.size()) {
            ret.push_back(path);
            return;
        }
        
        path.push_back(nums[pos]);
        helper(nums, pos + 1, path, ret);
        path.pop_back();
        
        while (pos + 1 < nums.size() && nums[pos + 1] == nums[pos]) ++pos;
        helper(nums, pos + 1, path, ret);
    }
};
```

# 78. Subsets

* *Difficulty: Medium*

* *Topics: Array, Backtracking, Bit Manipulation*

* *Similar Questions:*

  * [Subsets II](subsets-ii.md)

  * [Generalized Abbreviation](generalized-abbreviation.md)

  * [Letter Case Permutation](letter-case-permutation.md)

## Problem:

<p>Given a set of <strong>distinct</strong> integers, <em>nums</em>, return all possible subsets (the power set).</p>

<p><strong>Note:</strong> The solution set must not contain duplicate subsets.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong>
[
  [3],
&nbsp; [1],
&nbsp; [2],
&nbsp; [1,2,3],
&nbsp; [1,3],
&nbsp; [2,3],
&nbsp; [1,2],
&nbsp; []
]</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> path;
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
        
        helper(nums, pos + 1, path, ret);
    }
};
```

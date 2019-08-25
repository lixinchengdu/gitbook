# 46. Permutations

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Next Permutation](next-permutation.md)

  * [Permutations II](permutations-ii.md)

  * [Permutation Sequence](permutation-sequence.md)

  * [Combinations](combinations.md)

## Problem:

<p>Given a collection of <strong>distinct</strong> integers, return all possible permutations.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]
<strong>Output:</strong>
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        vector<int> path;
        helper(nums, 0, ret);
        return ret;
    }
    
    void helper(vector<int>& nums, int pos, vector<vector<int>>& ret) {
        if (nums.size() == pos) {
            ret.push_back(nums);
            return;
        }
        
        for (int i = pos; i < nums.size(); ++i) {
            swap(nums[pos], nums[i]);
            helper(nums, pos + 1, ret);
            swap(nums[pos], nums[i]);
        }
    }
};
```

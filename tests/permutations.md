# 46. Permutations

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Next Permutation](./tests/permutations.md)

  * [Permutations II](./tests/permutations.md)

  * [Permutation Sequence](./tests/permutations.md)

  * [Combinations](./tests/permutations.md)

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
        helper (nums, 0);
        return result;
    }
    
    void helper (vector <int>& nums, int start)
    {
        if (start == nums.size())
        {
            result.push_back(nums);
            return;
        }
        for (int i = start; i < nums.size(); i++)
        {
            swap(nums[start], nums[i]);
            helper (nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }
    
    vector <vector <int> > result;
    vector <int> path;
};
```

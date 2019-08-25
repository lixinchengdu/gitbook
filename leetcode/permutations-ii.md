# 47. Permutations II

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Next Permutation](next-permutation.md)

  * [Permutations](permutations.md)

  * [Palindrome Permutation II](palindrome-permutation-ii.md)

  * [Number of Squareful Arrays](number-of-squareful-arrays.md)

## Problem:

<p>Given a collection of numbers that might contain duplicates, return all possible unique permutations.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,1,2]
<strong>Output:</strong>
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        //sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        
        helper(nums, 0, ret);
        return ret;
    }
    
    void helper(vector<int>& nums, int pos, vector<vector<int>>& ret) {
        if (pos == nums.size()) {
            ret.push_back(nums);
            return;
        }
        
        unordered_set<int> seen; //Use index is not able to deduplicate. for example [0,0,1,2]. If the last element swap with the first, the list becomes [2, 0, 1, 0], which elements with the same value are not adjecent. 
        for (int i = pos; i < nums.size(); ++i) {
            if (seen.count(nums[i]) > 0)    continue;
            seen.insert(nums[i]);
            swap(nums[pos], nums[i]);
            helper(nums, pos + 1, ret);
            swap(nums[pos], nums[i]);
        }
    }
};
```

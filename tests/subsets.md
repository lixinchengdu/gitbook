# 78. Subsets

* *Difficulty: Medium*

* *Topics: Array, Backtracking, Bit Manipulation*

* *Similar Questions:*

  * [Subsets II](./tests/subsets.md)

  * [Generalized Abbreviation](./tests/subsets.md)

  * [Letter Case Permutation](./tests/subsets.md)

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
        helper(nums, 0);
        return res;
    }
    
private:
    vector <vector <int> >  res;
    vector <int>    path;
    void helper (vector <int>& nums, int start)
    {
        if (nums.size() == start)   {res.push_back(path);   return;}
        else
        {
            path.push_back(nums[start]);
            helper(nums, start+1);
            path.pop_back();
            helper(nums, start+1);
        }
        
    }
    
};
```

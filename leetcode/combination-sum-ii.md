# 40. Combination Sum II

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Combination Sum](combination-sum.md)

## Problem:

<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates =&nbsp;<code>[10,1,2,7,6,1,5]</code>, target =&nbsp;<code>8</code>,
<strong>A solution set is:</strong>
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
<strong>A solution set is:</strong>
[
&nbsp; [1,2,2],
&nbsp; [5]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector<vector<int>> ret;
        helper(candidates, 0, target, path, ret);
        return ret;
    }
    
    void helper(vector<int>& candidates, int pos, int target, vector<int>& path, vector<vector<int>>& ret) {
        if (target < 0) return;
        if (pos == candidates.size()) {
            if (target == 0) {
                ret.push_back(path);
            }
            return;
        }
        
        int val = candidates[pos];
        path.push_back(val);
        helper(candidates, pos + 1, target - val, path, ret);
        path.pop_back();
        while (pos + 1 < candidates.size() && candidates[pos + 1] == candidates[pos]) ++pos;
        helper(candidates, pos + 1, target, path, ret);
    }
};
```

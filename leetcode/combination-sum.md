# 39. Combination Sum

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)

  * [Combination Sum II](combination-sum-ii.md)

  * [Combinations](combinations.md)

  * [Combination Sum III](combination-sum-iii.md)

  * [Factor Combinations](factor-combinations.md)

  * [Combination Sum IV](combination-sum-iv.md)

## Problem:

<p>Given a <strong>set</strong> of candidate numbers (<code>candidates</code>) <strong>(without duplicates)</strong> and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sums to <code>target</code>.</p>

<p>The <strong>same</strong> repeated number may be chosen from <code>candidates</code>&nbsp;unlimited number of times.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers (including <code>target</code>) will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>A solution set is:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>A solution set is:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector<vector<int>> ret;
        helper(candidates, 0, target, path, ret);
        
        return ret;
    }
    
    void helper(vector<int>& candidates, int pos, int target, vector<int>& path, vector<vector<int>>& ret) {  
        if (target < 0) return;
        if (target == 0) {
            ret.push_back(path);
            return;
        }
        if (pos == candidates.size())   return;
        
        path.push_back(candidates[pos]);
        helper(candidates, pos, target - candidates[pos], path, ret);
        path.pop_back();
        helper(candidates, pos + 1, target, path, ret);
    }
};
```

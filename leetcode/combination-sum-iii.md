# 216. Combination Sum III

* *Difficulty: Medium*

* *Topics: Array, Backtracking*

* *Similar Questions:*

  * [Combination Sum](combination-sum.md)

## Problem:

<div>
<p>Find all possible combinations of <i><b>k</b></i> numbers that add up to a number <i><b>n</b></i>, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All numbers will be positive integers.</li>
	<li>The solution set must not contain duplicate combinations.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 7
<strong>Output:</strong> [[1,2,4]]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <i><b>k</b></i> = 3, <i><b>n</b></i> = 9
<strong>Output:</strong> [[1,2,6], [1,3,5], [2,3,4]]
</pre>
</div>
## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        vector<vector<int>> ret;
        helper(1, n, k, path, ret);
        return ret;
    }
    
    void helper(int pos, int target, int k, vector<int>& path, vector<vector<int>>& ret) {
        if (target < 0) return;
        if (pos == 10) {
            if (target == 0 && k == 0) {
                ret.push_back(path);
            }
            return;
        }
        path.push_back(pos);
        helper(pos + 1, target - pos, k - 1, path, ret);
        path.pop_back();
        helper(pos + 1, target, k, path, ret);
    }
};
```

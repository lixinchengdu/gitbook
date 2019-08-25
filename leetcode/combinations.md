# 77. Combinations

* *Difficulty: Medium*

* *Topics: Backtracking*

* *Similar Questions:*

  * [Combination Sum](combination-sum.md)

  * [Permutations](permutations.md)

## Problem:

<p>Given two integers <em>n</em> and <em>k</em>, return all possible combinations of <em>k</em> numbers out of 1 ... <em>n</em>.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;n = 4, k = 2
<strong>Output:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<int> path;
        vector<vector<int>> ret;
        helper(n, k, 1, path, ret);
        return ret;
    }
    
    void helper(int n, int k, int pos, vector<int>& path, vector<vector<int>>& ret) {
        if (path.size() == k) {
            ret.push_back(path);
            return;
        }
        
        if (pos > n || n - pos + 1 + path.size() < k) {
            return;
        }
        
        path.push_back(pos);
        helper(n, k, pos + 1, path, ret);      
        path.pop_back();
        helper(n, k, pos + 1, path, ret);
    }
};
```

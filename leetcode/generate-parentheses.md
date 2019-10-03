# 22. Generate Parentheses

* *Difficulty: Medium*

* *Topics: String, Backtracking*

* *Similar Questions:*

  * [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md)

  * [Valid Parentheses](valid-parentheses.md)

## Problem:

<p>
Given <i>n</i> pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
</p>

<p>
For example, given <i>n</i> = 3, a solution set is:
</p>
<pre>
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
</pre>
## Solutions:

```c++
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ret;
        if (n == 0) return ret;
        string path;
        
        helper(2 * n, 0, path, ret);
        return ret;
    }
    
    void helper(int remain, int left, string& path, vector<string>& ret) {
        if (remain == 0 && left == 0) {
            ret.push_back(path);
            return;
        }
        if (left < 0) {
            return;
        }
        if (remain < left) {
            return;
        }
        
        path.push_back('(');
        helper(remain - 1, left + 1, path, ret);
        path.pop_back();
        path.push_back(')');
        helper(remain - 1, left - 1, path, ret);
        path.pop_back();
        
    }
};
```

#### More intuitive solution

From [Huahua](https://zxi.mytechroad.com/blog/searching/leetcode-22-generate-parentheses/)

```c++
// Author: Huahua
// Running time: 0 ms
class Solution {
public:
  vector<string> generateParenthesis(int n) {
    vector<string> ans;
    string cur;
    if (n > 0) dfs(n, n, cur, ans);
    return ans;
  }
private:
  void dfs(int l, int r, string& s, vector<string>& ans) {
    if (l + r == 0) {
      ans.push_back(s);
      return;
    }
    if (r < l) return;
    if (l > 0) {
      dfs(l - 1, r, s += "(", ans);
      s.pop_back();
    }
    if (r > 0) {
      dfs(l, r - 1, s += ")", ans);
      s.pop_back();
    }
  }
};
```

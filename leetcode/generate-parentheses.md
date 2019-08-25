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

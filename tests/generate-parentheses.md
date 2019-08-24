# 22. Generate Parentheses

* *Difficulty: Medium*

* *Topics: String, Backtracking*

* *Similar Questions:*

  * [Letter Combinations of a Phone Number](./tests/generate-parentheses.md)

  * [Valid Parentheses](./tests/generate-parentheses.md)

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
    void RecGenParenthesis(string prefix, int left, int right);
    vector<string> generateParenthesis(int n) {
        string a;
        RecGenParenthesis ("", n, n);
        return Parenthesis;
        
    }
private: vector<string> Parenthesis;
};

void Solution::RecGenParenthesis(string prefix, int left, int right)
{
    if (left == 0 && right == 0 )
    {
       
        Parenthesis.push_back(prefix);
        return;
    }
    if (left == 0)
    {
       
        RecGenParenthesis(prefix+")", left, right-1);
        
    }
    else{
    if (left == right)
    {
        
        RecGenParenthesis(prefix+"(", left-1, right);
        
    }
    else
    {
       
        RecGenParenthesis(prefix+"(", left-1, right);
        RecGenParenthesis(prefix+")", left, right-1);
    }
    }
    
}
```

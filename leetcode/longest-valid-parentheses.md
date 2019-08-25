# 32. Longest Valid Parentheses

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Valid Parentheses](valid-parentheses.md)

## Problem:

<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, find the length of the longest valid (well-formed) parentheses substring.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()&quot;</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;<code>)()())</code>&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is <code>&quot;()()&quot;</code>
</pre>

## Solutions:

```c++
class Solution { //gready method need to consider two scenarios
public:
    int longestValidParentheses(string s) {
        string reversed = s;
        reverse(reversed.begin(), reversed.end());
        replace(reversed.begin(), reversed.end(), '(', '=');
        replace(reversed.begin(), reversed.end(), ')', '(');
        replace(reversed.begin(), reversed.end(), '=', ')');
        
    
        return max(longestValidParenthesesHelper(s), longestValidParenthesesHelper(reversed));
    }
    
    int longestValidParenthesesHelper(string s) {
        int ret = 0;
        int balance = 0;
        int left = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                ++balance;
            } else {
                --balance;
                if (balance == 0) {
                    ret = max(ret, i - left + 1);
                } else if (balance < 0) {
                    left = i + 1;
                    balance = 0;
                }
            }
        }
        
        return ret;
    }
    
};
```

# 20. Valid Parentheses

* *Difficulty: Easy*

* *Topics: String, Stack*

* *Similar Questions:*

  * [Generate Parentheses](generate-parentheses.md)

  * [Longest Valid Parentheses](longest-valid-parentheses.md)

  * [Remove Invalid Parentheses](remove-invalid-parentheses.md)

  * [Check If Word Is Valid After Substitutions](check-if-word-is-valid-after-substitutions.md)

## Problem:

<p>Given a string containing just the characters <code>&#39;(&#39;</code>, <code>&#39;)&#39;</code>, <code>&#39;{&#39;</code>, <code>&#39;}&#39;</code>, <code>&#39;[&#39;</code> and <code>&#39;]&#39;</code>, determine if the input string is valid.</p>

<p>An input string is valid if:</p>

<ol>
	<li>Open brackets must be closed by the same type of brackets.</li>
	<li>Open brackets must be closed in the correct order.</li>
</ol>

<p>Note that an empty string is&nbsp;also considered valid.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;()&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;()[]{}&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;(]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> &quot;([)]&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> &quot;{[]}&quot;
<strong>Output:</strong> true
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (auto c : s) {
            switch(c) {
                case '(':
                case '{':
                case '[':
                    stk.push(c);
                    break;
                case ')':
                    if (stk.empty() || stk.top() != '(') return false;
                    stk.pop();
                    break;
                case '}':
                    if (stk.empty() || stk.top() != '{') return false;
                    stk.pop();
                    break;
                case ']':
                    if (stk.empty() || stk.top() != '[') return false;
                    stk.pop();
                    break;
                default:
                    continue;
            }
        }
        
        return stk.empty();
    }
};
```

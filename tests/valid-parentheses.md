# 20. Valid Parentheses

* *Difficulty: Easy*

* *Topics: String, Stack*

* *Similar Questions:*

  * [Generate Parentheses](./tests/valid-parentheses.md)

  * [Longest Valid Parentheses](./tests/valid-parentheses.md)

  * [Remove Invalid Parentheses](./tests/valid-parentheses.md)

  * [Check If Word Is Valid After Substitutions](./tests/valid-parentheses.md)

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
        stack <char> symStack;
        for (int i = 0; i < s.length(); i++)
        {
            if (isOpen(s[i]))   symStack.push(s[i]);
            else
            {   
                if (symStack.empty())   return false;
                if (match(symStack.top(), s[i]))   symStack.pop();
                else    return false;
            }
        }
        if (symStack.empty())  return true;
        return false;
    }
    
    bool isOpen (char c)
    {
        return c == '(' || c == '{' || c == '[';
    }
    
    bool match(char open, char close)
    {
        return ((open == '(' && close == ')') || (open == '[' && close == ']') || (open == '{' && close == '}')) ;
    }
};
```

# 224. Basic Calculator

* *Difficulty: Hard*

* *Topics: Math, Stack*

* *Similar Questions:*

  * [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.md)

  * [Basic Calculator II](basic-calculator-ii.md)

  * [Different Ways to Add Parentheses](different-ways-to-add-parentheses.md)

  * [Expression Add Operators](expression-add-operators.md)

  * [Basic Calculator III](basic-calculator-iii.md)

## Problem:

<p>Implement a basic calculator to evaluate a simple expression string.</p>

<p>The expression string may contain open <code>(</code> and closing parentheses <code>)</code>, the plus <code>+</code> or minus sign <code>-</code>, <b>non-negative</b> integers and empty spaces <code> </code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;1 + 1&quot;
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot; 2-1 + 2 &quot;
<strong>Output:</strong> 3</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot;(1+(4+5+2)-3)+(6+8)&quot;
<strong>Output:</strong> 23</pre>
<b>Note:</b>

<ul>
	<li>You may assume that the given expression is always valid.</li>
	<li><b>Do not</b> use the <code>eval</code> built-in library function.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int calculate(string s) {
        stack<int> stk;
        int sign = 1;
        int val = 0;
        stk.push(0);
        for (int i = 0; i < s.length(); ++i) {
            switch(s[i]) {
                case '+': {
                    stk.top() = stk.top() + sign * val;
                    sign = 1; // reset
                    val = 0;
                    break;
                }
                case '-': {
                    stk.top() = stk.top() + sign * val;
                    sign = -1; // reset
                    val = 0;
                    break;
                }
                case ' ': {
                    break;
                }
                case '(': {
                    stk.push(sign);
                    sign = 1; // reset
                    val = 0;
                    stk.push(0);
                    break;
                }
                case ')': {
                    stk.top() = stk.top() + sign * val;
                    int expVal = stk.top();
                    stk.pop();
                    expVal = expVal * stk.top();
                    stk.pop();
                    stk.top() += expVal;
                    val = 0; // reset
                    sign = 1;
                    break;
                }
                default: {
                    val = val * 10 - '0' + s[i] ;
                    break;
                }
            }
           
        }
        
        return stk.top() + val * sign; // including all
    }
};
```

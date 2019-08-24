# 150. Evaluate Reverse Polish Notation

* *Difficulty: Medium*

* *Topics: Stack*

* *Similar Questions:*

  * [Basic Calculator](./tests/evaluate-reverse-polish-notation.md)

  * [Expression Add Operators](./tests/evaluate-reverse-polish-notation.md)

## Problem:

<p>Evaluate the value of an arithmetic expression in <a href="http://en.wikipedia.org/wiki/Reverse_Polish_notation" target="_blank">Reverse Polish Notation</a>.</p>

<p>Valid operators are <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>. Each operand may be an integer or another expression.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Division between two integers should truncate toward zero.</li>
	<li>The given RPN expression is always valid. That means the expression would always evaluate to a result and there won&#39;t&nbsp;be any&nbsp;divide&nbsp;by zero operation.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [&quot;2&quot;, &quot;1&quot;, &quot;+&quot;, &quot;3&quot;, &quot;*&quot;]
<strong>Output:</strong> 9
<strong>Explanation:</strong> ((2 + 1) * 3) = 9
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [&quot;4&quot;, &quot;13&quot;, &quot;5&quot;, &quot;/&quot;, &quot;+&quot;]
<strong>Output:</strong> 6
<strong>Explanation:</strong> (4 + (13 / 5)) = 6
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> [&quot;10&quot;, &quot;6&quot;, &quot;9&quot;, &quot;3&quot;, &quot;+&quot;, &quot;-11&quot;, &quot;*&quot;, &quot;/&quot;, &quot;*&quot;, &quot;17&quot;, &quot;+&quot;, &quot;5&quot;, &quot;+&quot;]
<strong>Output:</strong> 22
<strong>Explanation:</strong> 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
</pre>

## Solutions:

```c++
class Solution {
public:
    int evalRPN(vector<string> &tokens) {
     vector<int> stack;
     int result;
     while (!tokens.empty())
    {
        string head;
        head=tokens.front();
        tokens.erase(tokens.begin());
        if((head>="0" && head<="9") || (head.length()>1) )
        {
            int value=atoi(head.c_str());
            stack.push_back(value);
        }
        else
        {
            int left;
            int right;
            right=stack.back();
            stack.pop_back();
            left=stack.back();
            stack.pop_back();
            char c_head=head.c_str()[0];
            switch(c_head)
            {
                case '+': 
                    result=left+right;
                    stack.push_back(result);
                    break;
                case '-':
                    result=left-right;
                    stack.push_back(result);
                    break;
                case '*':
                    result=left*right;
                    stack.push_back(result);
                    break;
                case '/':
                    result=left/right;
                    stack.push_back(result);
                    break;
            }
        }
    }
    return stack.back();
    }
};
```

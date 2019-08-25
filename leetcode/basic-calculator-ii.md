# 227. Basic Calculator II

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

  * [Basic Calculator](basic-calculator.md)

  * [Expression Add Operators](expression-add-operators.md)

  * [Basic Calculator III](basic-calculator-iii.md)

## Problem:

<p>Implement a basic calculator to evaluate a simple expression string.</p>

<p>The expression string contains only <b>non-negative</b> integers, <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code> operators and empty spaces <code> </code>. The integer division should truncate toward zero.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;3+2*2&quot;
<strong>Output:</strong> 7
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot; 3/2 &quot;
<strong>Output:</strong> 1</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> &quot; 3+5 / 2 &quot;
<strong>Output:</strong> 5
</pre>

<p><b>Note:</b></p>

<ul>
	<li>You may assume that the given expression is always valid.</li>
	<li><b>Do not</b> use the <code>eval</code> built-in library function.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int calculate(string s) {
        int sum = 0;
        int val = 0;
        char lastChar = '+';
        vector<int> v;
        for (int i = 0; i <= s.length(); ++i) {
            if (i != s.length()) {
                if (s[i] == ' ') {
                    continue;
                }
                if (isdigit(s[i])) {
                    val = val * 10 + (s[i] - '0');
                    continue;
                }
            }
            
            switch(lastChar) {
                case '+': 
                    v.push_back(val);
                    break;
                case '-': 
                    v.push_back(-val);
                    break;
                case '*': 
                    v.back() *= val;
                    break;
                case '/': 
                    v.back() /= val;
                    break;
            }
            
            val = 0;
            if (i != s.length()) {
                lastChar = s[i];
            }
        }
        
        for (auto val : v) {
            sum += val;
        }
        
        return sum;
    }
};
```

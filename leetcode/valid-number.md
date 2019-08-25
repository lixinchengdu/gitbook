# 65. Valid Number

* *Difficulty: Hard*

* *Topics: Math, String*

* *Similar Questions:*

  * [String to Integer (atoi)](string-to-integer-atoi.md)

## Problem:

<p>Validate if a given string can be interpreted as&nbsp;a decimal number.</p>

<p>Some examples:<br />
<code>&quot;0&quot;</code> =&gt; <code>true</code><br />
<code>&quot; 0.1 &quot;</code> =&gt; <code>true</code><br />
<code>&quot;abc&quot;</code> =&gt; <code>false</code><br />
<code>&quot;1 a&quot;</code> =&gt; <code>false</code><br />
<code>&quot;2e10&quot;</code> =&gt; <code>true</code><br />
<code>&quot; -90e3&nbsp; &nbsp;&quot;</code> =&gt; <code>true</code><br />
<code>&quot; 1e&quot;</code> =&gt; <code>false</code><br />
<code>&quot;e3&quot;</code> =&gt; <code>false</code><br />
<code>&quot; 6e-1&quot;</code> =&gt; <code>true</code><br />
<code>&quot; 99e2.5&nbsp;&quot;</code> =&gt; <code>false</code><br />
<code>&quot;53.5e93&quot;</code> =&gt; <code>true</code><br />
<code>&quot; --6 &quot;</code> =&gt; <code>false</code><br />
<code>&quot;-+3&quot;</code> =&gt; <code>false</code><br />
<code>&quot;95a54e53&quot;</code> =&gt; <code>false</code></p>

<p><strong>Note:</strong> It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:</p>

<ul>
	<li>Numbers 0-9</li>
	<li>Exponent - &quot;e&quot;</li>
	<li>Positive/negative sign - &quot;+&quot;/&quot;-&quot;</li>
	<li>Decimal point - &quot;.&quot;</li>
</ul>

<p>Of course, the context of these characters also matters in the input.</p>

<p><strong>Update (2015-02-10):</strong><br />
The signature of the <code>C++</code> function had been updated. If you still see your function signature accepts a <code>const char *</code> argument, please click the reload button to reset your code definition.</p>

## Solutions:

```c++
class Solution {
public:
    bool isNumber(string s) {
        bool sign = false;
        bool dot = false;
        bool exponent = false;
        bool num = false;
        
        int left = 0;
        while (left < s.length() && s[left] == ' ')  ++left;
        
        int right = s.length() - 1;
        while (right >= 0 && s[right] == ' ') --right;
        
        if (left > right)   return false;
        
        for (int i = left; i <= right; ++i) {
            char c = s[i];
            if (isdigit(c)) {
                sign = true;
                num = true;
               // if (c == '0' && i -1 >= 0 && s[i-1] == '0' && !dot) return false;
            }            
            else if (c == '+' || c == '-') {
                if (sign)   return false;
                sign = true;
            }            
            else if (c == 'e') {
                if (exponent)   return false;
                if (!num)   return false;
                sign = false;
                dot = true;
                exponent = true;
                num = false;
            }  
            else if (c == '.') {
                if (dot)    return false;
                dot = true;
                sign = true;
            }
            else {
                return false;
            }
        }
        
        return s[right] != 'e' && num;
    }
};
```

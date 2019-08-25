# 1197. Parsing A Boolean Expression

* *Difficulty: Hard*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Return the result of evaluating a given boolean <code>expression</code>, represented as a string.</p>

<p>An expression can either be:</p>

<ul>
	<li><code>&quot;t&quot;</code>, evaluating to <code>True</code>;</li>
	<li><code>&quot;f&quot;</code>, evaluating to <code>False</code>;</li>
	<li><code>&quot;!(expr)&quot;</code>, evaluating to the logical NOT of the inner expression <code>expr</code>;</li>
	<li><code>&quot;&amp;(expr1,expr2,...)&quot;</code>, evaluating to the logical AND of 2 or more inner expressions <code>expr1, expr2, ...</code>;</li>
	<li><code>&quot;|(expr1,expr2,...)&quot;</code>, evaluating to the logical OR of 2 or more inner expressions <code>expr1, expr2, ...</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;!(f)&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;|(f,t)&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;&amp;(t,f)&quot;
<strong>Output:</strong> false
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> expression = &quot;|(&amp;(t,f,t),!(t))&quot;
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= expression.length &lt;= 20000</code></li>
	<li><code>expression[i]</code>&nbsp;consists of characters in <code>{&#39;(&#39;, &#39;)&#39;, &#39;&amp;&#39;, &#39;|&#39;, &#39;!&#39;, &#39;t&#39;, &#39;f&#39;, &#39;,&#39;}</code>.</li>
	<li><code>expression</code> is a valid expression representing a boolean, as given in the description.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    bool negate(string& expression, int& pos) {
        bool ret = !helper(expression, pos);
        ++pos; // remove )
        return ret;
    }
    
    bool logicAdd(string& expression, int& pos) {
        bool ret = true;
        do {
            ret = helper(expression, pos) && ret;
        } while (expression[pos++] == ',');
        return ret;
    } 

    bool logicOr(string& expression, int& pos) {
        bool ret = false;
        do {
            ret = helper(expression, pos) || ret;
        } while (expression[pos++] == ',');
        return ret;
    } 

    bool parseBoolExpr(string expression) {
        int pos = 0;
        return helper(expression, pos);
    }

    bool helper(string& expression, int& pos) {
        //bool ret;
        //for (;pos < expression.length(); ++pos) {
            char c = expression[pos];
            if (c == '!') {
                ++pos; // remove !
                ++pos; // remove (
                return negate(expression, pos);
            } 

            if (c == '&') {
                ++pos; // remove &
                ++pos; // remove (
                return logicAdd(expression, pos);
            }

            if (c == '|') {
                ++pos; // remove |
                ++pos; // remove (
                return logicOr(expression, pos);
            }

            ++pos;
            if (c == 't') {
                return true;
            }
            else return false;
        //}
    }
};
```

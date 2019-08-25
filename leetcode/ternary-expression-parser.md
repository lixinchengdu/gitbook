# 439. Ternary Expression Parser

* *Difficulty: Medium*

* *Topics: Stack, Depth-first Search*

* *Similar Questions:*

  * [Mini Parser](mini-parser.md)

  * [Remove Comments](remove-comments.md)

  * [Parse Lisp Expression](parse-lisp-expression.md)

## Problem:

<p>Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. You can always assume that the given expression is valid and only consists of digits <code>0-9</code>, <code>?</code>, <code>:</code>, <code>T</code> and <code>F</code> (<code>T</code> and <code>F</code> represent True and False respectively).

<p><b>Note:</b>
<ol>
<li>The length of the given string is &le; 10000.</li>
<li>Each number will contain only one digit.</li>
<li>The conditional expressions group right-to-left (as usual in most languages).</li>
<li>The condition will always be either <code>T</code> or <code>F</code>. That is, the condition will never be a digit.</li>
<li>The result of the expression will always evaluate to either a digit <code>0-9</code>, <code>T</code> or <code>F</code>.</li>
</ol>
</p>

<p>
<b>Example 1:</b>
<pre>
<b>Input:</b> "T?2:3"

<b>Output:</b> "2"

<b>Explanation:</b> If true, then result is 2; otherwise result is 3.
</pre>
</p>

<p>
<b>Example 2:</b>
<pre>
<b>Input:</b> "F?1:T?4:5"

<b>Output:</b> "4"

<b>Explanation:</b> The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
</pre>
</p>

<p>
<b>Example 3:</b>
<pre>
<b>Input:</b> "T?T?F:5:3"

<b>Output:</b> "F"

<b>Explanation:</b> The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    string parseTernary(string expression) {
        if (expression.length() == 0)   return "";
        int pos = 0;
        return helper(expression, pos);
    }

    string helper(string& expression, int& pos) {
        char c = expression[pos];
        if ((c == 'T' || c == 'F') && (pos + 1 < expression.length()) && (expression[pos + 1] == '?')) {
            ++pos; // remove 'T' or 'F'
            ++pos; // remove '?'
            string left = helper(expression, pos);
            ++pos; // remove ':'
            string right = helper(expression, pos);
            return c == 'T' ? left : right;
        }

        ++pos; // remove base case 
        return string(1, c);
    }
};
```

# 1298. Reverse Substrings Between Each Pair of Parentheses

* *Difficulty: Medium*

* *Topics: Stack*

* *Similar Questions:*

## Problem:

<p>Given a string <code>s</code> that consists of lower case English letters and brackets.&nbsp;</p>

<p>Reverse the strings&nbsp;in each&nbsp;pair of matching parentheses, starting&nbsp;from the innermost one.</p>

<p>Your result should <strong>not</strong> contain any bracket.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(abcd)&quot;
<strong>Output:</strong> &quot;dcba&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(u(love)i)&quot;
<strong>Output:</strong> &quot;iloveu&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(ed(et(oc))el)&quot;
<strong>Output:</strong> &quot;leetcode&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a(bcdefghijkl(mno)p)q&quot;
<strong>Output:</strong> &quot;apmnolkjihgfedcbq&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> only contains lower case English characters and parentheses.</li>
	<li>It&#39;s guaranteed that all parentheses are balanced.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    string reverseParentheses(string s) {
        int pos = 0;
        return helper(s, pos);
    }
    
private:
    string helper(const string& s, int& pos) {
        string ret;
        while (pos < s.length()) {
            if (s[pos] == '(') {
                string inner = helper(s, ++pos);
                reverse(inner.begin(), inner.end());
                ret.append(inner);
            } else if (s[pos] == ')') {
                ++pos;
                return ret;
            } else {
                ret.push_back(s[pos++]);
            }
        }
        return ret;
    }
    
};
```

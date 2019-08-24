# 10. Regular Expression Matching

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming, Backtracking*

* *Similar Questions:*

  * [Wildcard Matching](./tests/regular-expression-matching.md)

## Problem:

<p>Given an input string (<code>s</code>) and a pattern (<code>p</code>), implement regular expression matching with support for <code>&#39;.&#39;</code> and <code>&#39;*&#39;</code>.</p>

<pre>
&#39;.&#39; Matches any single character.
&#39;*&#39; Matches zero or more of the preceding element.
</pre>

<p>The matching should cover the <strong>entire</strong> input string (not partial).</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>s</code>&nbsp;could be empty and contains only lowercase letters <code>a-z</code>.</li>
	<li><code>p</code> could be empty and contains only lowercase letters <code>a-z</code>, and characters like&nbsp;<code>.</code>&nbsp;or&nbsp;<code>*</code>.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;a&quot; does not match the entire string &quot;aa&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aa&quot;
p = &quot;a*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&#39;*&#39; means zero or more of the preceding&nbsp;element, &#39;a&#39;. Therefore, by repeating &#39;a&#39; once, it becomes &quot;aa&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;ab&quot;
p = &quot;.*&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;&quot;.*&quot; means &quot;zero or more (*) of any character (.)&quot;.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;aab&quot;
p = &quot;c*a*b&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong>&nbsp;c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches &quot;aab&quot;.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong>
s = &quot;mississippi&quot;
p = &quot;mis*is*p*.&quot;
<strong>Output:</strong> false
</pre>

## Solutions:

```c++
class Solution {
public:
    bool isMatch(string s, string p) {
        int n1 = s.length();
        int n2 = p.length();
        if (n1 == 0 && n2 == 0) return true;
        return helper (s, 0, p, 0);
    }
    
    bool helper (string& s, int sPos, string& p, int pPos)
    {
        //cout << sPos <<endl;
        //cout << pPos << endl;
        if (sPos == s.length() && pPos == p.length())   return true;
        if (pPos == p.length()) return false; 
        if (p.length() - pPos == 1)
        {
            if (p[pPos] == '.' || s[sPos] == p[pPos]) return helper(s, sPos+1, p, pPos+1);
            else return false;
        }
        else
        {
            if (p[pPos+1] != '*')
            {
                if (sPos < s.length() && (p[pPos] == s[sPos]||p[pPos] == '.')) return helper(s, sPos+1, p, pPos+1);
                else    return false;
            }
            else
            {
                if (sPos == s.length()) return helper(s, sPos, p, pPos+2);
                if (s[sPos] != p[pPos] && p[pPos] != '.') return helper(s, sPos, p, pPos + 2);
                else
                {
                    return helper(s, sPos+1, p, pPos) || helper(s, sPos, p, pPos+2);
                }
            }
            
        }
    }
    
};
```

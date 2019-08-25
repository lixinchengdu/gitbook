# 161. One Edit Distance

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

  * [Edit Distance](edit-distance.md)

## Problem:

<p>Given two strings <b><i>s</i></b>&nbsp;and <b><i>t</i></b>, determine if they are both one edit distance apart.</p>

<p><strong>Note:</strong>&nbsp;</p>

<p>There are 3 possiblities to satisify one edit distance apart:</p>

<ol>
	<li>Insert a&nbsp;character into <strong><em>s</em></strong>&nbsp;to get&nbsp;<strong><em>t</em></strong></li>
	<li>Delete a&nbsp;character from&nbsp;<strong><em>s</em></strong>&nbsp;to get&nbsp;<strong><em>t</em></strong></li>
	<li>Replace a character of&nbsp;<strong><em>s</em></strong>&nbsp;to get&nbsp;<strong><em>t</em></strong></li>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <strong><em>s</em></strong> = &quot;ab&quot;, <strong><em>t</em></strong> = &quot;acb&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can insert &#39;c&#39; into <strong><em>s</em></strong>&nbsp;to get&nbsp;<strong><em>t.</em></strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <strong><em>s</em></strong> = &quot;cab&quot;, <strong><em>t</em></strong> = &quot;ad&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> We cannot get <strong><em>t </em></strong>from <strong><em>s </em></strong>by only one step.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> <strong><em>s</em></strong> = &quot;1203&quot;, <strong><em>t</em></strong> = &quot;1213&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> We can replace &#39;0&#39; with &#39;1&#39; to get&nbsp;<strong><em>t.</em></strong></pre>

## Solutions:

```c++
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if (s.length() == t.length()) {
            return isOneReplace(s, t);
        } else {
            if (s.length() - t.length() == 1) {
                return isOneDelete(s, t);
            } else if (t.length() - s.length() == 1) {
                return isOneDelete(t, s);
            } else {
                return false;
            }
        }
    }
    
    bool isOneReplace(string& s, string& t) {
        int diff = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != t[i]) {
                if (++diff > 1) return false;
            }
        }
        
        return diff == 1;
    }
    
    bool isOneDelete(string& s, string& t) {
        int i = 0;
        while (i < t.length() && s[i] == t[i]) ++i;
        if (i == t.length())    return true;
        
        while (i < t.length() && s[i+1] == t[i]) ++i;
        return i == t.length();
    }
};
```

# 165. Compare Version Numbers

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Compare two version numbers <em>version1</em> and <em>version2</em>.<br />
If <code><em>version1</em> &gt; <em>version2</em></code> return <code>1;</code>&nbsp;if <code><em>version1</em> &lt; <em>version2</em></code> return <code>-1;</code>otherwise return <code>0</code>.</p>

<p>You may assume that the version strings are non-empty and contain only digits and the <code>.</code> character.</p>
<p>The <code>.</code> character does not represent a decimal point and is used to separate number sequences.</p>
<p>For instance, <code>2.5</code> is not &quot;two and a half&quot; or &quot;half way to version three&quot;, it is the fifth second-level revision of the second first-level revision.</p>
<p>You may assume the default revision number for each level of a version number to be <code>0</code>. For example, version number <code>3.4</code> has a revision number of <code>3</code> and <code>4</code> for its first and second level revision number. Its third and fourth level revision number are both <code>0</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;0.1&quot;, <code><em>version2</em></code> = &quot;1.1&quot;
<strong>Output:</strong> -1</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input: </strong><code><em>version1</em></code> = &quot;1.0.1&quot;, <code><em>version2</em></code> = &quot;1&quot;
<strong>Output:</strong> 1</pre>

<p><strong>Example 3:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;7.5.2.4&quot;, <code><em>version2</em></code> = &quot;7.5.3&quot;
<strong>Output:</strong> -1</pre>

<p><strong>Example 4:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;1.01&quot;, <code><em>version2</em></code> = &quot;1.001&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> Ignoring leading zeroes, both “01” and “001" represent the same number “1”</pre>

<p><strong>Example 5:</strong></p>
<pre>
<strong>Input:</strong> <code><em>version1</em></code> = &quot;1.0&quot;, <code><em>version2</em></code> = &quot;1.0.0&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> The first version number does not have a third level revision number, which means its third level revision number is default to "0"</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>
<ol>
<li>Version strings are composed of numeric strings separated by dots <code>.</code> and this numeric strings <strong>may</strong> have leading zeroes. </li>
<li>Version strings do not start or end with dots, and they will not be two consecutive dots.</li>
</ol>
## Solutions:

```c++
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int cur1 = 0;
        int cur2 = 0;
        int len1 = version1.length();
        int len2 = version2.length();
        
        while (cur1 < len1 || cur2 < len2) {
            int value1 = 0;
            int value2 = 0;
            
            while (cur1 < len1 && version1[cur1] == '0') {
                ++cur1;
            }
            while (cur1 < len1 && version1[cur1] != '.') {
                value1 = 10 * value1 + version1[cur1] - '0';
                ++cur1;
            }
            
            if (cur1 != len1) {
                ++cur1;
            }
            
            while (cur2 < len2 && version2[cur2] == '0') {
                ++cur2;
            }
            while (cur2 < len2 && version2[cur2] != '.') {
                value2 = 10 * value2 + version2[cur2] - '0';
                ++cur2;
            }
            
            if (cur2 != len2) {
                ++cur2;
            }
            
            if (value1 < value2) {
                return -1;
            } else if (value1 > value2) {
                return 1;
            }
        }
        
        return 0;
        
    }
};
```

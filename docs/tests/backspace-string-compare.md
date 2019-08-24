# 874. Backspace String Compare

* *Difficulty: Easy*

* *Topics: Two Pointers, Stack*

* *Similar Questions:*

## Problem:

<p>Given two&nbsp;strings&nbsp;<code>S</code>&nbsp;and <code>T</code>,&nbsp;return if they are equal when both are typed into empty text editors. <code>#</code> means a backspace character.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;ab#c&quot;</span>, T = <span id="example-input-1-2">&quot;ad#c&quot;</span>
<strong>Output: </strong><span id="example-output-1">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;ac&quot;.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;ab##&quot;</span>, T = <span id="example-input-2-2">&quot;c#d#&quot;</span>
<strong>Output: </strong><span id="example-output-2">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;&quot;.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">&quot;a##c&quot;</span>, T = <span id="example-input-3-2">&quot;#a#c&quot;</span>
<strong>Output: </strong><span id="example-output-3">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;c&quot;.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-4-1">&quot;a#c&quot;</span>, T = <span id="example-input-4-2">&quot;b&quot;</span>
<strong>Output: </strong><span id="example-output-4">false
</span><span><strong>Explanation</strong>: S becomes &quot;c&quot; while T becomes &quot;b&quot;.</span>
</pre>

<p><span><strong>Note</strong>:</span></p>

<ol>
	<li><code><span>1 &lt;= S.length &lt;= 200</span></code></li>
	<li><code><span>1 &lt;= T.length &lt;= 200</span></code></li>
	<li><span><code>S</code>&nbsp;and <code>T</code> only contain&nbsp;lowercase letters and <code>&#39;#&#39;</code> characters.</span></li>
</ol>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Can you solve it in <code>O(N)</code> time and <code>O(1)</code> space?</li>
</ul>
</div>
</div>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    bool backspaceCompare(string S, string T) {
        int i = S.length() - 1;
        int j = T.length() - 1;
        
        while (i >= 0 || j >= 0) {
            int harpCount = 0;
            
            while (i >= 0 && (harpCount > 0 || S[i] == '#')) {
                if (S[i] == '#') {
                    ++harpCount;
                } else {
                    --harpCount;
                }
                --i;
            }
            
           
            
            harpCount = 0;
            
            while (j >= 0 && (harpCount > 0 || T[j] == '#') ){
                if (T[j] == '#') {
                    ++harpCount;
                } else {
                    --harpCount;
                }
                --j;
            }
            
            
            
            
            if (i < 0 && j >= 0)    return false;
            if (j < 0 && i >= 0)    return false;
            if (i < 0 && j < 0) return true;
            if (S[i] != T[j])   return false;
            --i;
            --j;
        }
        
        return true;
    }
};
```

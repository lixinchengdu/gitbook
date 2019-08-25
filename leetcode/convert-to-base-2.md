# 1070. Convert to Base -2

* *Difficulty: Medium*

* *Topics: Math*

* *Similar Questions:*

## Problem:

<p>Given a number <code>N</code>, return a string consisting of <code>&quot;0&quot;</code>s and <code>&quot;1&quot;</code>s&nbsp;that represents its value in base <code><strong>-2</strong></code>&nbsp;(negative two).</p>

<p>The returned string must have no leading zeroes, unless the string is <code>&quot;0&quot;</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">&quot;110&quot;
<strong>Explantion:</strong> (-2) ^ 2 + (-2) ^ 1 = 2</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">3</span>
<strong>Output: </strong><span id="example-output-2">&quot;111&quot;
</span><span id="example-output-1"><strong>Explantion:</strong> (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0</span><span> = 3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">4</span>
<strong>Output: </strong><span id="example-output-3">&quot;100&quot;
</span><span id="example-output-1"><strong>Explantion:</strong> (-2) ^ 2 = 4</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><span><code>0 &lt;= N &lt;= 10^9</code></span></li>
</ol>
</div>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    string baseNeg2(int N) {
        if (N == 0) return "0";
        string ret;
        while (N != 0) {
            if (N % 2 == 0) {
                ret.push_back('0');
                N /= -2;
            } else {
                ret.push_back('1');
                N -= 1;
                N /= -2;
            }
        }
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```

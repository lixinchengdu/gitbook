# 1131. Count Substrings with Only One Distinct Letter

* *Difficulty: Easy*

* *Topics: Math, String*

* *Similar Questions:*

## Problem:

<p>Given a string <code>S</code>,&nbsp;return the number of substrings that have&nbsp;only <strong>one distinct</strong> letter.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aaaba&quot;
<strong>Output:</strong> 8
<strong>Explanation: </strong>The substrings with one distinct letter are &quot;aaa&quot;, &quot;aa&quot;, &quot;a&quot;, &quot;b&quot;.
&quot;aaa&quot; occurs 1 time.
&quot;aa&quot; occurs 2 times.
&quot;a&quot; occurs 4 times.
&quot;b&quot; occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aaaaaaaaaa&quot;
<strong>Output:</strong> 55
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= S.length &lt;= 1000</code></li>
	<li><code>S[i]</code> consists of only lowercase English letters.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int countLetters(string S) {
        int count = 0;
        int consecutive = 1;
        for (int i = 1; i < S.length(); ++i) {
            if (S[i] == S[i-1]) {
                ++consecutive;
            } else {
                count += calculate(consecutive);
                consecutive = 1;
            }
        }
        
        count += calculate(consecutive);
        return count;
    }
    
private:
    int calculate(int num) {
        return num * (num + 1) / 2;
    }
    
};
```

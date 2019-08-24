# 91. Decode Ways

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Decode Ways II](./tests/decode-ways.md)

## Problem:

<p>A message containing letters from <code>A-Z</code> is being encoded to numbers using the following mapping:</p>

<pre>
&#39;A&#39; -&gt; 1
&#39;B&#39; -&gt; 2
...
&#39;Z&#39; -&gt; 26
</pre>

<p>Given a <strong>non-empty</strong> string containing only digits, determine the total number of ways to decode it.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;12&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong>&nbsp;It could be decoded as &quot;AB&quot; (1 2) or &quot;L&quot; (12).
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;226&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong>&nbsp;It could be decoded as &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), or &quot;BBF&quot; (2 2 6).</pre>

## Solutions:

```c++
class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        if (n == 0) return 0;
        int prev = 1;
        int prevprev = 0;
        int now;
        int lastCharValue = 0;
        int nowCharValue;
        int sum;
        for (auto c: s)
        {
            nowCharValue = c - '0';
            if (c == '0')
            {
                if (lastCharValue != 1 && lastCharValue != 2)   return 0;
                now = prevprev;
            }
            else
            {
                sum = lastCharValue*10 + nowCharValue;
                if (sum >= 11 && sum <= 26)
                {
                    now = prevprev + prev;
                }
                else 
                {
                    now = prev;
                }
            }
            prevprev = prev;
            prev = now;
            lastCharValue = nowCharValue;
        }
        return prev;
        /*
        if (n == 0 || n == 1) return 1;
        else if (n >= 2)
        {
            int sum = (s[0] - '0') * 10 + s[1] - '0';
            if (sum >= 11 && sum <= 26 && sum != 20)    prev = 2;
            else prev = 1;
        }
        if (n ==  2)    return prev;
        
        int prevprev = 1;
        */
        
        
    }
};
```

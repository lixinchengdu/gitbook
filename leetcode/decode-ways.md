# 91. Decode Ways

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Decode Ways II](decode-ways-ii.md)

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
    
        int len = s.length();
        vector<int> cache(len, -1);
        
        return helper(s, 0, cache);
    }
    
    int helper(string s, int pos, vector<int>& cache) {
        if (pos > s.length())  return 0;
        if (pos == s.length())  return 1;
        if (cache[pos] != -1)   return cache[pos];
        
        int count = 0;
        
        if (s[pos] == '0')  return 0;
        count += helper(s, pos + 1, cache);
        if (pos + 1 < s.length()) {
            if (10*(s[pos] - '0') + s[pos + 1] - '0' <= 26) {
                count += helper(s, pos + 2, cache);
            }
        }
        
        cache[pos] = count;
        return count;
    }
};
```

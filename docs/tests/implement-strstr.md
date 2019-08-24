# 28. Implement strStr()

* *Difficulty: Easy*

* *Topics: Two Pointers, String*

* *Similar Questions:*

  * [Shortest Palindrome](./tests/implement-strstr.md)

  * [Repeated Substring Pattern](./tests/implement-strstr.md)

## Problem:

<p>Implement <a href="http://www.cplusplus.com/reference/cstring/strstr/" target="_blank">strStr()</a>.</p>

<p>Return the index of the first occurrence of needle in haystack, or <strong>-1</strong> if needle is not part of haystack.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;hello&quot;, needle = &quot;ll&quot;
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;aaaaa&quot;, needle = &quot;bba&quot;
<strong>Output:</strong> -1
</pre>

<p><strong>Clarification:</strong></p>

<p>What should we return when <code>needle</code> is an empty string? This is a great question to ask during an interview.</p>

<p>For the purpose of this problem, we will return 0 when <code>needle</code> is an empty string. This is consistent to C&#39;s&nbsp;<a href="http://www.cplusplus.com/reference/cstring/strstr/" target="_blank">strstr()</a> and Java&#39;s&nbsp;<a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a>.</p>

## Solutions:

```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length() == 0)   return 0;
        for (int i = 0; i < haystack.length(); ++i) {
            bool match = true;
            for (int j = 0; j < needle.length(); ++j) {
                if (haystack[i+j] != needle[j]) {
                    match = false;
                    break;
                }
            }
            if (match)  return i;
        }
        return -1;
    }
};
```

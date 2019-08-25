# 28. Implement strStr()

* *Difficulty: Easy*

* *Topics: Two Pointers, String*

* *Similar Questions:*

  * [Shortest Palindrome](shortest-palindrome.md)

  * [Repeated Substring Pattern](repeated-substring-pattern.md)

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
        if (haystack.length() < needle.length())    return -1;
        if (needle.length() == 0)   return 0;
        
        const unsigned int MOD = 10000; 
        const unsigned int MUL = 10;
        
        unsigned int needleHash = 0;
        for (auto c : needle) {
            needleHash = (needleHash * MUL + c - 'a' + 1) % MOD;
        }
        
        unsigned int haystackHash = 0;
        for (int i = 0; i < needle.length(); ++i) {
            haystackHash = (haystackHash * MUL + haystack[i] - 'a' + 1) % MOD;
        }
        
        unsigned int highHash = 1;
        for (int i = 0; i < needle.length() - 1; ++i) { // be careful! what if needle size is 0;
            highHash = (highHash * MUL) % MOD;
        }
        
        for (int i = 0; i < haystack.length() - needle.length() + 1; ++i) {
            if (needleHash == haystackHash && isEqual(haystack, i, needle)) return i;
            if (i == haystack.length() - needle.length()) return -1;
            haystackHash = ((haystackHash + MOD - highHash * (haystack[i] - 'a' + 1) % MOD ) % MOD * MUL + haystack[i+needle.length()] - 'a' + 1) % MOD; // WARNING: don't overflow
        }
        
        return -1;
        
    }
    
    bool isEqual(const string& haystack, int start, const string& needle) {
        for (int i = 0; i < 0 + needle.length(); ++i) {
            if (haystack[i + start] != needle[i])   return false;
        }
        
        return true;
    }
};
```

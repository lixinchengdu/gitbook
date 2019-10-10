# 459. Repeated Substring Pattern

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Implement strStr()](implement-strstr.md)

  * [Repeated String Match](repeated-string-match.md)

## Problem:

<p>Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;abab&quot;
<b>Output:</b> True
<b>Explanation:</b> It&#39;s the substring &quot;ab&quot; twice.
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;aba&quot;
<b>Output:</b> False
</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> &quot;abcabcabcabc&quot;
<b>Output:</b> True
<b>Explanation:</b> It&#39;s the substring &quot;abc&quot; four times. (And the substring &quot;abcabc&quot; twice.)
</pre>

## Solutions:

```c++
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int len = s.length();
        for (int i = 2; i <= len; ++i) {
            if (len % i == 0 && isPrime(i)) {
                int patternLen = len / i;
                int j = 0;
                for (j = 0; j < patternLen; ++j) {
                    int k = 1;
                    for (k = 1; k < i; ++k) {
                        if (s[k * patternLen + j] != s[j]) break;
                    }
                    if (k != i) break;
                }
                if (j == patternLen)    return true;
            }
        }
        return false;
    }
    
private:
    bool isPrime(int num) {
        for (int i = 2; i <= sqrt(num); ++i) {
            if (num % i == 0)   return false;
        }
        
        return true;
    }
};
```

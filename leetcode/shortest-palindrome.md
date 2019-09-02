# 214. Shortest Palindrome

* *Difficulty: Hard*

* *Topics: String*

* *Similar Questions:*

  * [Longest Palindromic Substring](longest-palindromic-substring.md)

  * [Implement strStr()](implement-strstr.md)

  * [Palindrome Pairs](palindrome-pairs.md)

## Problem:

<p>Given a string <em><b>s</b></em>, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><code>&quot;aacecaaa&quot;</code>
<strong>Output:</strong> <code>&quot;aaacecaaa&quot;</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><code>&quot;abcd&quot;</code>
<strong>Output:</strong> <code>&quot;dcbabcd&quot;</code></pre>
## Solutions:

```c++
class Solution {
public:
    string shortestPalindrome(string s) {
        if (s == "")    return "";
        string r = s;
        reverse(r.begin(), r.end());
        int n = r.length();
        
        int forwardHash = 0;
        int backwardHash = 0;
        int val = 1;
        int MOD = INT_MAX / 31;
        int ret = 0;

        for (int i = 0 ; i < n; ++i) {
            forwardHash = (forwardHash + val * (s[i] - 'a' + 1)) % MOD;
            val = (val * 31) % MOD;
            
            backwardHash = ((backwardHash * 31) % MOD + (s[i] - 'a' + 1)) % MOD;

            if (forwardHash == backwardHash) {
                ret = i;
            }
        }

        return r + s.substr(ret + 1, n - ret - 1);
        
        return "";
    }
};
```

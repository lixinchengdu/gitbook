# 5. Longest Palindromic Substring

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Shortest Palindrome](./tests/longest-palindromic-substring.md)

  * [Palindrome Permutation](./tests/longest-palindromic-substring.md)

  * [Palindrome Pairs](./tests/longest-palindromic-substring.md)

  * [Longest Palindromic Subsequence](./tests/longest-palindromic-substring.md)

  * [Palindromic Substrings](./tests/longest-palindromic-substring.md)

## Problem:

<p>Given a string <strong>s</strong>, find the longest palindromic substring in <strong>s</strong>. You may assume that the maximum length of <strong>s</strong> is 1000.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

## Solutions:

```c++
func longestPalindrome(s string) string {
    ret := 0
    str := ""
    for i := 0; i < len(s); i++ {
        for j := 0; i-j >= 0 && i+j < len(s) && s[i-j] == s[i+j]; j++ {
            if 2*j + 1 > ret {
                ret = 2*j + 1
                str = s[i-j : i+j+1]
            }
        }
        
        for j := 0; i-j >=0 && i+j+1 < len(s) && s[i-j] == s[i+j+1]; j++ {
            if 2*j + 2 > ret {
                ret = 2*j + 2
                str = s[i-j:i+j+2]
            }
        }
    }
    
    return str
}

```

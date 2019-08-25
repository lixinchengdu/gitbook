# 266. Palindrome Permutation

* *Difficulty: Easy*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Longest Palindromic Substring](longest-palindromic-substring.md)

  * [Valid Anagram](valid-anagram.md)

  * [Palindrome Permutation II](palindrome-permutation-ii.md)

  * [Longest Palindrome](longest-palindrome.md)

## Problem:

<p>Given a string, determine if a permutation of the string could form a palindrome.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>&quot;code&quot;</code>
<strong>Output:</strong> false</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>&quot;aab&quot;</code>
<strong>Output:</strong> true</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> <code>&quot;carerac&quot;</code>
<strong>Output:</strong> true</pre>

## Solutions:

```c++
class Solution {
public:
    bool canPermutePalindrome(string s) {
        int charCount[256] = {0};
        for (auto c : s) {
            charCount[c] ^= 0x1;
        }
        int count = 0;
        for (int i = 0; i < 256; ++i) {
            count += charCount[i];
        }

        return s.length() % 2 == 0 ? count == 0 : count == 1;
    }
};
```

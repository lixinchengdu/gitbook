# 5. Longest Palindromic Substring

* *Difficulty: Medium*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

  * [Shortest Palindrome](shortest-palindrome.md)

  * [Palindrome Permutation](palindrome-permutation.md)

  * [Palindrome Pairs](palindrome-pairs.md)

  * [Longest Palindromic Subsequence](longest-palindromic-subsequence.md)

  * [Palindromic Substrings](palindromic-substrings.md)

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
class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.length();
        int length1 = 0;
        int length2 = 0;
        int ret = 0;
        int len = 0;
        
        for (int center = 0; center < n; ++center) { 
            int left1 = center;
            int right1 = center;
            int count1 = 0;
            while (left1 >= 0 && right1 < n && s[left1] == s[right1]) { // increment is not in while loop
                ++count1;
                --left1;
                ++right1;
            }
            
            length1 = 2*count1 - 1;
            if (length1 > len) {
                len = length1;
                ret = left1 + 1;
            }
            
            int count2 = 0;
            int left2 = center;
            int right2 = center + 1;
            while (left2 >= 0 && right2 < n && s[left2] == s[right2]) {
                ++count2;
                --left2;
                ++right2;
            }
            length2 = 2 * count2;
            
            if (length2 > len) {
                len = length2;
                ret = left2 + 1;
            }
        }
        
        return s.substr(ret, len);
    }
};
```

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

## Optimization

It is possible to refactor the two while loops by define a function `getLen(const string& str, int left, int right)`.
For odd-length palindrome, initially `left == right`. 

The following code is taken from [Huahua](https://zxi.mytechroad.com/blog/greedy/leetcode-5-longest-palindromic-substring/)

```c++
// Author: Huahua
class Solution {
public:
  string longestPalindrome(string s) {
    int best_len = 0;
    int start = 0;
    for (int i = 0; i < s.length(); ++i) {
      int l1 = getLen(s, i, i);
      int l2 = getLen(s, i, i + 1);
      int l = max(l1, l2);      
      if (l > best_len) {
        best_len = l;
        start = i - (l - 1) / 2;
      }
    }
    return s.substr(start, best_len);
  }
private:
  int getLen(const string& s, int l, int r) {
    if (s[l] != s[r]) return 1;    
    while (l >= 0 && r <= s.length() - 1 && s[l] == s[r]) {
      --l;
      ++r;
    };
    return r - l - 1;
  }
};
```

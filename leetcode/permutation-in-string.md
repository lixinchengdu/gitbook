# 567. Permutation in String

* *Difficulty: Medium*

* *Topics: Two Pointers, Sliding Window*

* *Similar Questions:*

  * [Minimum Window Substring](minimum-window-substring.md)

  * [Find All Anagrams in a String](find-all-anagrams-in-a-string.md)

## Problem:

<p>Given two strings <b>s1</b> and <b>s2</b>, write a function to return true if <b>s2</b> contains the permutation of <b>s1</b>. In other words, one of the first string&#39;s permutations is the <b>substring</b> of the second string.</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input: </b>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<b>Output: </b>True
<b>Explanation:</b> s2 contains one permutation of s1 (&quot;ba&quot;).
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The input strings only contain lower case letters.</li>
	<li>The length of both given strings is in range [1, 10,000].</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    bool isPermutation(string s1, string s2) {
        if (s1.length() != s2.length()) return false;
        int count[26] = {0};
        for (char c : s1) {
            ++count[c - 'a'];
        }
        for (char c : s2) {
            if (--count[c - 'a'] < 0)   return false;
        }
        return true;
    }
    
    bool checkInclusion(string s1, string s2) {
        map<char, int> charHash;
        for (int i = 0; i < 26; ++i) {
            charHash['a' + i] = i * (i + 1);
        }
        
        if (s2.length() < s1.length())  return false;
        int hash1 = 0;
        for (auto c : s1) {
            hash1 = (hash1 + charHash[c]) % MOD;
        }
        
        int hash2 = 0;
        for (int i = 0; i < s1.length() - 1; ++i) {
            hash2 = (hash2 + charHash[s2[i]]) % MOD;
        }
        
        for (int i = s1.length() - 1; i < s2.length(); ++i) {
            hash2 = (hash2 + charHash[s2[i]]) % MOD;
            if (hash1 == hash2 && isPermutation(s1, s2.substr(i - s1.length() + 1, s1.length()))) {
                return true;
            }
            hash2 = (hash2 + MOD - charHash[s2[i - s1.length() + 1]]) % MOD; 
        }
        
        return false;
    }
    
private:
    int MOD = INT_MAX/2;
};
```

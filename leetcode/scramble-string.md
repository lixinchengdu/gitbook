# 87. Scramble String

* *Difficulty: Hard*

* *Topics: String, Dynamic Programming*

* *Similar Questions:*

## Problem:

<p>Given a string <em>s1</em>, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.</p>

<p>Below is one possible representation of <em>s1</em> = <code>&quot;great&quot;</code>:</p>

<pre>
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
</pre>

<p>To scramble the string, we may choose any non-leaf node and swap its two children.</p>

<p>For example, if we choose the node <code>&quot;gr&quot;</code> and swap its two children, it produces a scrambled string <code>&quot;rgeat&quot;</code>.</p>

<pre>
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
</pre>

<p>We say that <code>&quot;rgeat&quot;</code> is a scrambled string of <code>&quot;great&quot;</code>.</p>

<p>Similarly, if we continue to swap the children of nodes <code>&quot;eat&quot;</code> and <code>&quot;at&quot;</code>, it produces a scrambled string <code>&quot;rgtae&quot;</code>.</p>

<pre>
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
</pre>

<p>We say that <code>&quot;rgtae&quot;</code> is a scrambled string of <code>&quot;great&quot;</code>.</p>

<p>Given two strings <em>s1</em> and <em>s2</em> of the same length, determine if <em>s2</em> is a scrambled string of <em>s1</em>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;great&quot;, s2 = &quot;rgeat&quot;
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s1 = &quot;abcde&quot;, s2 = &quot;caebd&quot;
<strong>Output:</strong> false</pre>

## Solutions:

```c++
class Solution {
public:
    bool isScramble(string s1, string s2) {
        int len1 = s1.length();
        int len2 = s2.length();
        
        map<vector<int>, bool> cache;
        return helper(s1, s2, 0, 0, len1, cache);
    }
    
    bool helper(string s1, string s2, int idx1, int idx2, int len, map<vector<int>, bool>& cache) {
        if (cache.find({idx1, idx2, len}) != cache.end()) {
            return cache[{idx1, idx2, len}];
        }
        
        bool ret = false;
        
        if (stringEqual(s1, s2, idx1, idx2, len)) {
            cache[{idx1, idx2, len}] = true;
            return true;
        }
        
        for (int part1 = 1; part1 <= len - 1; ++part1) {
            if (helper(s1, s2, idx1, idx2, part1, cache) && helper(s1, s2, idx1 + part1, idx2 + part1, len - part1, cache)) {
                cache[{idx1, idx2, len}] = true;
                return true;
            }
            
            if (helper(s1, s2, idx1, idx2 + len - part1, part1, cache) && helper(s1, s2, idx1 + part1, idx2, len - part1, cache)) {
                cache[{idx1, idx2, len}] = true;
                return true;
            }
        }
        
        cache[{idx1, idx2, len}] = false;
        return false;
    }
    
    bool stringEqual(string s1, string s2, int idx1, int idx2, int len) {
        if (idx1 + len > s1.length())   return false;
        if (idx2 + len > s2.length())   return false;
        
        for (int i = 0; i < len; ++i) {
            if (s1[i + idx1] != s2[i + idx2]) return false;
        }
        
        return true;
    }   
};
```

# 3. Longest Substring Without Repeating Characters

* *Difficulty: Medium*

* *Topics: Hash Table, Two Pointers, String, Sliding Window*

* *Similar Questions:*

  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)

  * [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters.md)

  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)

## Problem:

<p>Given a string, find the length of the <b>longest substring</b> without repeating characters.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;abcabcbb&quot;</span>
<strong>Output: </strong><span id="example-output-1">3 
<strong>Explanation:</strong></span> The answer is <code>&quot;abc&quot;</code>, with the length of 3. 
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;bbbbb&quot;</span>
<strong>Output: </strong><span id="example-output-2">1
</span><span id="example-output-1"><strong>Explanation: </strong>T</span>he answer is <code>&quot;b&quot;</code>, with the length of 1.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;pwwkew&quot;</span>
<strong>Output: </strong><span id="example-output-3">3
</span><span id="example-output-1"><strong>Explanation: </strong></span>The answer is <code>&quot;wke&quot;</code>, with the length of 3. 
             Note that the answer must be a <b>substring</b>, <code>&quot;pwke&quot;</code> is a <i>subsequence</i> and not a substring.
</pre>
</div>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int charPos[256] {0}; // initialization only for 0, not for other values
        for (int i = 0; i < 256; ++i) charPos[i] = -1;
        int ret = 0;
        int left = 0;
        for (int i = 0; i < s.length(); ++i) {
            char c = s[i];
            if (charPos[c] == -1 || charPos[c] < left) {
                charPos[c] = i;
                ret = max(ret, i - left + 1);
            } else {
                left = max(charPos[c] + 1, left); // first to update left;
                charPos[c] = i;
            }
        }
        
        return ret;
    }
};
```

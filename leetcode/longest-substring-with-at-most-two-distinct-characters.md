# 159. Longest Substring with At Most Two Distinct Characters

* *Difficulty: Hard*

* *Topics: Hash Table, Two Pointers, String, Sliding Window*

* *Similar Questions:*

  * [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md)

  * [Sliding Window Maximum](sliding-window-maximum.md)

  * [Longest Substring with At Most K Distinct Characters](longest-substring-with-at-most-k-distinct-characters.md)

  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)

## Problem:

<p>Given a string <strong><em>s</em></strong> , find the length of the longest substring&nbsp;<strong><em>t&nbsp;&nbsp;</em></strong>that contains <strong>at most </strong>2 distinct characters.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> &quot;eceba&quot;
<strong>Output: </strong>3
<strong>Explanation: <em>t</em></strong><em> </em>is &quot;ece&quot; which its length is 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> &quot;ccaabbb&quot;
<strong>Output: </strong>5
<strong>Explanation: <em>t</em></strong><em> </em>is &quot;aabbb&quot; which its length is 5.
</pre>
## Solutions:

```c++
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        unordered_map<char, int> charCount;
        int left = 0;
        int maxLen = 0;
        
        for (int right = 0; right < s.length(); ++right) {
            ++charCount[s[right]];
            if (charCount.size() <= 2) {
                maxLen = max(maxLen, right - left + 1);
            } else {
                while (left <= right && charCount.size() > 2) {
                    if(--charCount[s[left]] == 0)  charCount.erase(s[left]);
                    ++left;
                }
            }
        }
        
        return maxLen;
    }
};
```

# 340. Longest Substring with At Most K Distinct Characters

* *Difficulty: Hard*

* *Topics: Hash Table, String, Sliding Window*

* *Similar Questions:*

  * [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md)

  * [Longest Substring with At Most Two Distinct Characters](longest-substring-with-at-most-two-distinct-characters.md)

  * [Longest Repeating Character Replacement](longest-repeating-character-replacement.md)

  * [Subarrays with K Different Integers](subarrays-with-k-different-integers.md)

  * [Max Consecutive Ones III](max-consecutive-ones-iii.md)

## Problem:

<p>Given a string, find the length of the longest substring T that contains at most <i>k</i> distinct characters.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong>s = <span id="example-input-1-1">&quot;eceba&quot;</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>T is &quot;ece&quot; which its length is 3.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>s = <span id="example-input-2-1">&quot;aa&quot;</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong>2
<strong>Explanation: </strong>T is &quot;aa&quot; which its length is 2.
</pre>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        unordered_map<char, int> charCount;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); ++right) {
            ++charCount[s[right]];
            if (charCount.size() <= k) {
                maxLen = max(maxLen, right - left + 1);
            } else {
                while (left <= right && charCount.size() > k) {
                    if(--charCount[s[left]] == 0)  charCount.erase(s[left]);
                    ++left;
                }
            }
        }

        return maxLen;
    }
};
```

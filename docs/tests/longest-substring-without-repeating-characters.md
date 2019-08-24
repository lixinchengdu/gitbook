# 3. Longest Substring Without Repeating Characters

* *Difficulty: Medium*

* *Topics: Hash Table, Two Pointers, String, Sliding Window*

* *Similar Questions:*

  * [Longest Substring with At Most Two Distinct Characters](./tests/longest-substring-without-repeating-characters.md)

  * [Longest Substring with At Most K Distinct Characters](./tests/longest-substring-without-repeating-characters.md)

  * [Subarrays with K Different Integers](./tests/longest-substring-without-repeating-characters.md)

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
func lengthOfLongestSubstring(s string) int {
    ret := 0
    start := 0
    
    location := [256]int{}
    for i := range location {
        location[i] = -1
    }
    
    for end := 0; end < len(s); end++ {
        if location[s[end]] >= start {
            start = location[s[end]] + 1
        } else if end - start + 1 > ret {
            ret = end - start + 1
        }
        location[s[end]] = end
    }
    
    return ret
}
```

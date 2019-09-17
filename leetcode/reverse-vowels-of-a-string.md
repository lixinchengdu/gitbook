# 345. Reverse Vowels of a String

* *Difficulty: Easy*

* *Topics: Two Pointers, String*

* *Similar Questions:*

  * [Reverse String](reverse-string.md)

  * [Remove Vowels from a String](remove-vowels-from-a-string.md)

## Problem:

<p>Write a function that takes a string as input and reverse only the vowels of a string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;hello&quot;</span>
<strong>Output: </strong><span id="example-output-1">&quot;holle&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;leetcode&quot;</span>
<strong>Output: </strong><span id="example-output-2">&quot;leotcede&quot;</span></pre>
</div>

<p><b>Note:</b><br />
The vowels does not include the letter &quot;y&quot;.</p>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {'a','e','i','o','u','A','E','I','O','U'};
        
        int left = 0;
        int right = s.length() - 1;
        
        while (left < right) {
            while (left < right && vowels.count(s[left]) == 0)  ++left;
            while (left < right && vowels.count(s[right]) == 0) --right;
            swap(s[left], s[right]);
            ++left;
            --right;
        }
        
        return s;
    }
};
```

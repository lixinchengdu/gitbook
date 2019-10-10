# 246. Strobogrammatic Number

* *Difficulty: Easy*

* *Topics: Hash Table, Math*

* *Similar Questions:*

  * [Strobogrammatic Number II](strobogrammatic-number-ii.md)

  * [Strobogrammatic Number III](strobogrammatic-number-iii.md)

  * [Confusing Number](confusing-number.md)

## Problem:

<p>A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).</p>

<p>Write a function to determine if a number is strobogrammatic. The number is represented as a string.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>  &quot;69&quot;
<b>Output:</b> true
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>  &quot;88&quot;
<b>Output:</b> true</pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b>  &quot;962&quot;
<b>Output:</b> false</pre>

## Solutions:

```c++
class Solution {
public:
    bool isStrobogrammatic(string num) {
        unordered_map<char, char> mirror {
            {'0', '0'},
            {'1', '1'},
            {'6', '9'},
            {'8', '8'},
            {'9', '6'}
        };
        
        int left = 0;
        int right = num.length() - 1;
        while (left <= right) {
            if (mirror.count(num[left]) == 0 || mirror[num[left]] != num[right])    return false;
            ++left;
            --right;
        }
        
        return true;
    }
};
```

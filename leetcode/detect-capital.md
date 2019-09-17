# 520. Detect Capital

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Given a word, you need to judge whether the usage of capitals in it is right or not.</p>

<p>We define the usage of capitals in a word to be right when one of the following cases holds:</p>

<ol>
	<li>All letters in this word are capitals, like &quot;USA&quot;.</li>
	<li>All letters in this word are not capitals, like &quot;leetcode&quot;.</li>
	<li>Only the first letter in this word is capital, like &quot;Google&quot;.</li>
</ol>
Otherwise, we define that this word doesn&#39;t use capitals in a right way.

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> &quot;USA&quot;
<b>Output:</b> True
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> &quot;FlaG&quot;
<b>Output:</b> False
</pre>

<p>&nbsp;</p>

<p><b>Note:</b> The input will be a non-empty word consisting of uppercase and lowercase latin letters.</p>

## Solutions:

```c++
class Solution {
public:
    bool detectCapitalUse(string word) {
        if (word.length() == 1) return true;
        if (islower(word[0]) && isupper(word[1]))   return false;
        for (int i = 2; i < word.length(); ++i) {
            if (!(isupper(word[i]) && isupper(word[i-1]) || islower(word[i]) && islower(word[i-1])))   return false;
        }
        return true;
    }
};
```

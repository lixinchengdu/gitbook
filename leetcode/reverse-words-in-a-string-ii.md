# 186. Reverse Words in a String II

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

  * [Reverse Words in a String](reverse-words-in-a-string.md)

  * [Rotate Array](rotate-array.md)

## Problem:

<p>Given an input string<strong><em>&nbsp;</em></strong>, reverse the string word by word.&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:  </strong>[&quot;t&quot;,&quot;h&quot;,&quot;e&quot;,&quot; &quot;,&quot;s&quot;,&quot;k&quot;,&quot;y&quot;,&quot; &quot;,&quot;i&quot;,&quot;s&quot;,&quot; &quot;,&quot;b&quot;,&quot;l&quot;,&quot;u&quot;,&quot;e&quot;]
<strong>Output: </strong>[&quot;b&quot;,&quot;l&quot;,&quot;u&quot;,&quot;e&quot;,&quot; &quot;,&quot;i&quot;,&quot;s&quot;,&quot; &quot;,&quot;s&quot;,&quot;k&quot;,&quot;y&quot;,&quot; &quot;,&quot;t&quot;,&quot;h&quot;,&quot;e&quot;]</pre>

<p><strong>Note:&nbsp;</strong></p>

<ul>
	<li>A word is defined as a sequence of non-space characters.</li>
	<li>The input string does not contain leading or trailing spaces.</li>
	<li>The words are always separated by a single space.</li>
</ul>

<p><strong>Follow up:&nbsp;</strong>Could you do it <i>in-place</i> without allocating extra space?</p>

## Solutions:

```c++
class Solution {
public:
    void reverseWords(vector<char>& s) {
        int start = 0;
        int end = 0;
        
        while (start < s.size()) {
            end = start + 1;
            while (end < s.size() && s[end] != ' ') ++end;
            reverse(s, start, end - 1);
            start = end + 1;
        }
        
        
        reverse(s, 0, s.size() - 1);
    }
    
    void reverse(vector<char>& s, int start, int end) {
        while (start < end) {
            swap(s[start], s[end]);
            ++start;
            --end;
        }
    }
};
```

# 443. String Compression

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Count and Say](count-and-say.md)

  * [Encode and Decode Strings](encode-and-decode-strings.md)

  * [Design Compressed String Iterator](design-compressed-string-iterator.md)

## Problem:

<p>Given an array of characters, compress it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><b>in-place</b></a>.</p>

<p>The length after compression must always be smaller than or equal to the original array.</p>

<p>Every element of the array should be a <b>character</b> (not int) of length 1.</p>

<p>After you are done <b>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></b>, return the new length of the array.</p>
&nbsp;

<p><b>Follow up:</b><br />
Could you solve it using only O(1) extra space?</p>
&nbsp;

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]

<b>Output:</b>
Return 6, and the first 6 characters of the input array should be: [&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]

<b>Explanation:</b>
&quot;aa&quot; is replaced by &quot;a2&quot;. &quot;bb&quot; is replaced by &quot;b2&quot;. &quot;ccc&quot; is replaced by &quot;c3&quot;.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;]

<b>Output:</b>
Return 1, and the first 1 characters of the input array should be: [&quot;a&quot;]

<b>Explanation:</b>
Nothing is replaced.
</pre>

<p>&nbsp;</p>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b>
[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]

<b>Output:</b>
Return 4, and the first 4 characters of the input array should be: [&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;].

<b>Explanation:</b>
Since the character &quot;a&quot; does not repeat, it is not compressed. &quot;bbbbbbbbbbbb&quot; is replaced by &quot;b12&quot;.
Notice each digit has it&#39;s own entry in the array.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>All characters have an ASCII value in <code>[35, 126]</code>.</li>
	<li><code>1 &lt;= len(chars) &lt;= 1000</code>.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    int compress(vector<char>& chars) {
        if (chars.size() == 0)    return 0;
        
        int pos = 0;
        int index = 0;
        char c;
        int count;
        while (index < chars.size()) {
            c = chars[index++];
            count = 1;
            while (index < chars.size() && chars[index] == c) {
                ++index;
                ++count;
            }
            if (count == 1) {
                chars[pos++] = c;
            } else {
                chars[pos++] = c;
                string countStr = to_string(count);
                for (auto& v : countStr) {
                    chars[pos++] = v;
                }
            }
        }
        
        return pos;
    }
};
```

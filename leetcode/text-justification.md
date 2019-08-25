# 68. Text Justification

* *Difficulty: Hard*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Given an array of words and a width&nbsp;<em>maxWidth</em>, format the text such that each line has exactly <em>maxWidth</em> characters and is fully (left and right) justified.</p>

<p>You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces <code>&#39; &#39;</code> when necessary so that each line has exactly <em>maxWidth</em> characters.</p>

<p>Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.</p>

<p>For the last line of text, it should be left justified and no <strong>extra</strong> space is inserted between words.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>A word is defined as a character sequence consisting&nbsp;of non-space characters only.</li>
	<li>Each word&#39;s length is&nbsp;guaranteed to be greater than 0 and not exceed <em>maxWidth</em>.</li>
	<li>The input array <code>words</code>&nbsp;contains at least one word.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
words = [&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;, &quot;of&quot;, &quot;text&quot;, &quot;justification.&quot;]
maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &nbsp;&quot;This &nbsp; &nbsp;is &nbsp; &nbsp;an&quot;,
&nbsp; &nbsp;&quot;example &nbsp;of text&quot;,
&nbsp; &nbsp;&quot;justification. &nbsp;&quot;
]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
words = [&quot;What&quot;,&quot;must&quot;,&quot;be&quot;,&quot;acknowledgment&quot;,&quot;shall&quot;,&quot;be&quot;]
maxWidth = 16
<strong>Output:</strong>
[
&nbsp; &quot;What &nbsp; must &nbsp; be&quot;,
&nbsp; &quot;acknowledgment &nbsp;&quot;,
&nbsp; &quot;shall be &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]
<strong>Explanation:</strong> Note that the last line is &quot;shall be    &quot; instead of &quot;shall     be&quot;,
&nbsp;            because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>
words = [&quot;Science&quot;,&quot;is&quot;,&quot;what&quot;,&quot;we&quot;,&quot;understand&quot;,&quot;well&quot;,&quot;enough&quot;,&quot;to&quot;,&quot;explain&quot;,
&nbsp;        &quot;to&quot;,&quot;a&quot;,&quot;computer.&quot;,&quot;Art&quot;,&quot;is&quot;,&quot;everything&quot;,&quot;else&quot;,&quot;we&quot;,&quot;do&quot;]
maxWidth = 20
<strong>Output:</strong>
[
&nbsp; &quot;Science &nbsp;is &nbsp;what we&quot;,
  &quot;understand &nbsp; &nbsp; &nbsp;well&quot;,
&nbsp; &quot;enough to explain to&quot;,
&nbsp; &quot;a &nbsp;computer. &nbsp;Art is&quot;,
&nbsp; &quot;everything &nbsp;else &nbsp;we&quot;,
&nbsp; &quot;do &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&quot;
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> ret;
        int count = 0;
        int n = words.size();
        vector<string> buffer;
        for (int i = 0; i < n;) {
            if (count == 0) {
                buffer.push_back(words[i]);
                count = words[i].length();
                ++i;
            } else {
                if (count + 1 + words[i].length() > maxWidth) {
                    ret.push_back(lineProcess(buffer, maxWidth));
                    count = 0;
                    buffer.clear();
                } else {
                    buffer.push_back(words[i]);
                    count += 1 + words[i].length();
                    ++i;
                }
            }
        }
        
        if (buffer.size() != 0) {
            ret.push_back(lastLineProcess(buffer, maxWidth));
        }
        
        return ret;
    }
    
    string lineProcess(vector<string>& buffer, int maxWidth) {
        if (buffer.size() == 1) return lastLineProcess(buffer, maxWidth);
        
        int count = 0;
        for (auto& word : buffer) {
            count += word.length();
        }
        
        int quotient = (maxWidth - count) / (buffer.size() - 1);
        int modulo = (maxWidth - count) % (buffer.size() - 1);
        
        string ret;
        ret.append(buffer[0]);
        for (int i = 1; i < buffer.size(); ++i) {
            int distance = quotient + (modulo-- > 0 ? 1 : 0);
            ret.append(distance, ' ');
            ret.append(buffer[i]);
        }
        return ret;
    }
    
    string lastLineProcess(vector<string>& buffer, int maxWidth) {
        string ret = buffer[0];
        for (int i = 1; i < buffer.size(); ++i) {
            ret.push_back(' ');
            ret.append(buffer[i]);
        }
        
        if (ret.length() < maxWidth) {
            ret.append(maxWidth - ret.length(), ' ');
        }
        
        return ret;
    }
};
```

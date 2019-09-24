# 318. Maximum Product of Word Lengths

* *Difficulty: Medium*

* *Topics: Bit Manipulation*

* *Similar Questions:*

## Problem:

<p>Given a string array <code>words</code>, find the maximum value of <code>length(word[i]) * length(word[j])</code> where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]</code>
<b>Output: </b><code>16 
<strong>Explanation: </strong></code>The two words can be <code>&quot;abcw&quot;, &quot;xtfn&quot;</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code>[&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]</code>
<b>Output: </b><code>4 
<strong>Explanation: </strong></code>The two words can be <code>&quot;ab&quot;, &quot;cd&quot;</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> <code>[&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]</code>
<b>Output: </b><code>0 
<strong>Explanation: </strong></code>No such pair of words.
</pre>

## Solutions:

```c++
class Solution {
public:
    int maxProduct(vector<string>& words) {
        unordered_map<int, int> indexToBit;
        
        for (int i = 0; i < words.size(); ++i) {
            int bitmap = getBitMap(words[i]);
            indexToBit[i] = bitmap;
        }
        
        int ret = 0;
        for (int i = 0; i < words.size(); ++i) {
            for (int j = i + 1; j < words.size(); ++j) {
                if ((indexToBit[i] & indexToBit[j]) == 0) {
                    ret = max(ret, (int) (words[i].length() * words[j].length()));
                }
            }
        }
        
        return ret;
    }
    
private:
    int getBitMap(const string& word) {
        int bitmap = 0;
        for (auto& c : word) {
            bitmap |= 1 << (c - 'a');
        }
        
        return bitmap;
    }
    
};
```

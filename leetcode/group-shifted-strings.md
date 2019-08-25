# 249. Group Shifted Strings

* *Difficulty: Medium*

* *Topics: Hash Table, String*

* *Similar Questions:*

  * [Group Anagrams](group-anagrams.md)

## Problem:

<p>Given a string, we can &quot;shift&quot; each of its letter to its successive letter, for example: <code>&quot;abc&quot; -&gt; &quot;bcd&quot;</code>. We can keep &quot;shifting&quot; which forms the sequence:</p>

<pre>
&quot;abc&quot; -&gt; &quot;bcd&quot; -&gt; ... -&gt; &quot;xyz&quot;</pre>

<p>Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>[&quot;abc&quot;, &quot;bcd&quot;, &quot;acef&quot;, &quot;xyz&quot;, &quot;az&quot;, &quot;ba&quot;, &quot;a&quot;, &quot;z&quot;],</code>
<b>Output:</b> 
[
  [&quot;abc&quot;,&quot;bcd&quot;,&quot;xyz&quot;],
  [&quot;az&quot;,&quot;ba&quot;],
  [&quot;acef&quot;],
  [&quot;a&quot;,&quot;z&quot;]
]
</pre>

## Solutions:

```c++
class Solution {
public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        unordered_map<string, vector<string>> groups;
        for (auto& s : strings) {
            string shift = s;
            int diff = s[0] - 'a';
            for (int i = 0; i < shift.length(); ++i) {
                shift[i] -= diff;
                if (shift[i] < 'a') {
                    shift[i] += 26;
                }
            }
            groups[shift].push_back(s);
        }
        vector<vector<string>> ret;
        for (auto& entry : groups) {
            ret.push_back(entry.second);
        }
        return ret;
    }
};
```

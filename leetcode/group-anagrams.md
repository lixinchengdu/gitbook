# 49. Group Anagrams

* *Difficulty: Medium*

* *Topics: Hash Table, String*

* *Similar Questions:*

  * [Valid Anagram](valid-anagram.md)

  * [Group Shifted Strings](group-shifted-strings.md)

## Problem:

<p>Given an array of strings, group anagrams together.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> <code>[&quot;eat&quot;, &quot;tea&quot;, &quot;tan&quot;, &quot;ate&quot;, &quot;nat&quot;, &quot;bat&quot;]</code>,
<strong>Output:</strong>
[
  [&quot;ate&quot;,&quot;eat&quot;,&quot;tea&quot;],
  [&quot;nat&quot;,&quot;tan&quot;],
  [&quot;bat&quot;]
]</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All inputs will be in lowercase.</li>
	<li>The order of your output does not&nbsp;matter.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagrams;
        
        for (auto& str : strs) {
            string anagram = str;
            sort(anagram.begin(), anagram.end());
            anagrams[anagram].push_back(str);
        }
        
        vector<vector<string>> ret;
        for (auto it = anagrams.begin(); it != anagrams.end(); ++it) {
            ret.push_back(it->second);
        }
        
        return ret;
    }
};
```

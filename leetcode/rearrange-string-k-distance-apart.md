# 358. Rearrange String k Distance Apart

* *Difficulty: Hard*

* *Topics: Hash Table, Heap, Greedy*

* *Similar Questions:*

  * [Task Scheduler](task-scheduler.md)

  * [Reorganize String](reorganize-string.md)

## Problem:

<p>Given a non-empty string <b>s</b> and an integer <b>k</b>, rearrange the string such that the same characters are at least distance <b>k</b> from each other.</p>

<p>All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string <code>&quot;&quot;</code>.</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong>s = <span id="example-input-1-1">&quot;aabbcc&quot;</span>, k = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">&quot;abcabc&quot; 
<strong>Explanation: </strong></span>The same letters are at least distance 3 from each other.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>s = <span id="example-input-2-1">&quot;aaabc&quot;</span>, k = <span id="example-input-2-2">3</span>
<strong>Output: </strong><span id="example-output-2">&quot;&quot; 
<strong>Explanation:</strong> </span>It is not possible to rearrange the string.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>s = <span id="example-input-3-1">&quot;aaadbbcc&quot;</span>, k = <span id="example-input-3-2">2</span>
<strong>Output: </strong><span id="example-output-3">&quot;abacabcd&quot;
</span><span id="example-output-2"><strong>Explanation:</strong> </span>The same letters are at least distance 2 from each other.
</pre>
</div>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    string rearrangeString(string s, int k) {
        if (k <= 0) return s; // This special case if important
        if (s.length() == 0)    return s;
        
        int len = s.length();
        
        unordered_map<char, int> charCount;
        for (auto c : s) {
            ++charCount[c];
        }
        
        vector<char> chars;
        for (auto& entry : charCount) {
            chars.push_back(entry.first);
        }
        
        sort(chars.begin(), chars.end(), [charCount](char c1, char c2) {
           return charCount.at(c1) > charCount.at(c2); 
        });
        
        int maxVal = charCount[chars[0]];
        int maxCount = 0;
        for (int i = 0; i < chars.size() && charCount[chars[i]] == maxVal; ++i) ++maxCount;
        
        
        if (len < (k * (maxVal - 1) + maxCount)) return "";
        
        vector<string> matrix(maxVal - 1);
        int pos = 0;
        for (int i = maxCount; i < chars.size(); ++i) {
            for (int j = 0; j < charCount[chars[i]]; ++j) {
                matrix[pos%(maxVal - 1)].push_back(chars[i]);
                ++pos;
            }
        }
        
        string ret;
        string maxStr;
        for (int i = 0; i < maxCount; ++i) {
            maxStr.push_back(chars[i]);
        }
        
        for (int i = 0; i < maxVal - 1; ++i) {
            ret.append(maxStr);
            ret.append(matrix[i]);
        }
        ret.append(maxStr);
        return ret;
    }
};
```

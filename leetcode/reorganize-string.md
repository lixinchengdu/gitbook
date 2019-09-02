# 778. Reorganize String

* *Difficulty: Medium*

* *Topics: String, Heap, Greedy, Sort*

* *Similar Questions:*

  * [Rearrange String k Distance Apart](rearrange-string-k-distance-apart.md)

  * [Task Scheduler](task-scheduler.md)

## Problem:

<p>Given a string <code>S</code>, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.</p>

<p>If possible, output any possible result.&nbsp; If not possible, return the empty string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aab&quot;
<strong>Output:</strong> &quot;aba&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;aaab&quot;
<strong>Output:</strong> &quot;&quot;
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>S</code> will consist of lowercase letters and have length in range <code>[1, 500]</code>.</li>
</ul>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    string reorganizeString(string S) {
        return rearrangeString(S, 2);
    }
    
private:
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

# 768. Partition Labels

* *Difficulty: Medium*

* *Topics: Two Pointers, Greedy*

* *Similar Questions:*

  * [Merge Intervals](merge-intervals.md)

## Problem:

<p>
A string <code>S</code> of lowercase letters is given.  We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "ababcbacadefegdehijhklij"
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
<li><code>S</code> will consist of lowercase letters (<code>'a'</code> to <code>'z'</code>) only.</li>
</ol></p>
## Solutions:

```c++
class Solution {
public:
    vector<int> partitionLabels(string S) {
        int charLastIndex[26];
        for (int i = 0; i < 26; ++i) {
            charLastIndex[i] = -1;
        }
        
        for (int i = 0; i < S.length(); ++i) {
            charLastIndex[S[i] - 'a'] = i;
        }
        
        vector<int> ret;
        int left = 0;
        int right = 0;
        
        for (int i = 0; i < S.length(); ++i) {
            right = max(right, charLastIndex[S[i] - 'a']);
            if (i != right) {
              continue;  
            }
            
            ret.push_back(right - left + 1);
            left = right + 1;
            right = left;
        }
        
        return ret;
    }
};
```

# 387. First Unique Character in a String

* *Difficulty: Easy*

* *Topics: Hash Table, String*

* *Similar Questions:*

  * [Sort Characters By Frequency](sort-characters-by-frequency.md)

## Problem:

<p>
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
</p>
<p><b>Examples:</b>
<pre>
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
</pre>
</p>

<p>
<b>Note:</b> You may assume the string contain only lowercase letters.
</p>
## Solutions:

```c++
class Solution {
public:
    int firstUniqChar(string s) {
        int count[26] = {0};
        for (int i = 0; i < s.length(); ++i) {
            ++count[s[i] - 'a'];
        }
        
        for (int i = 0; i < s.length(); ++i) {
            if (count[s[i] - 'a'] == 1) return i;
        }
        
        return -1;
    }
};
```

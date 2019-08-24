# 387. First Unique Character in a String

* *Difficulty: Easy*

* *Topics: Hash Table, String*

* *Similar Questions:*

  * [Sort Characters By Frequency](./tests/first-unique-character-in-a-string.md)

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
        unordered_map<char, int> charCount;
        for (auto c:s) {
            ++charCount[c]; 
        }
        for (int i = 0; i < s.length(); ++i) {
            if (charCount[s[i]] == 1)    return i;
        }
        return -1;
    }
};
```

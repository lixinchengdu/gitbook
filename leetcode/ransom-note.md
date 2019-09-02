# 383. Ransom Note

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Stickers to Spell Word](stickers-to-spell-word.md)

## Problem:

<p>
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 
</p>
<p>
Each letter in the magazine string can only be used once in your ransom note.
</p>

<p><b>Note:</b><br />
You may assume that both strings contain only lowercase letters.
</p>

<pre>
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
</pre>

## Solutions:

```c++
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> m;
        for (char c : magazine) ++m[c];
        for (char c : ransomNote) {
            if (--m[c] < 0) return false;
        }
        return true;
    }
};
```

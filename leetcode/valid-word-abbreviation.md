# 408. Valid Word Abbreviation

* *Difficulty: Easy*

* *Topics: String*

* *Similar Questions:*

  * [Minimum Unique Word Abbreviation](minimum-unique-word-abbreviation.md)

  * [Word Abbreviation](word-abbreviation.md)

## Problem:

<p>
Given a <b>non-empty</b> string <code>s</code> and an abbreviation <code>abbr</code>, return whether the string matches with the given abbreviation.
</p>

<p>A string such as <code>"word"</code> contains only the following valid abbreviations:</p>

<pre>["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
</pre>

<p>Notice that only the above abbreviations are valid abbreviations of the string <code>"word"</code>. Any other string is not a valid abbreviation of <code>"word"</code>.</p>

<p><b>Note:</b><br />
Assume <code>s</code> contains only lowercase letters and <code>abbr</code> contains only lowercase letters and digits.
</p>

<p><b>Example 1:</b><br />
<pre>
Given <b>s</b> = "internationalization", <b>abbr</b> = "i12iz4n":

Return true.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
Given <b>s</b> = "apple", <b>abbr</b> = "a2e":

Return false.
</pre>
</p>
## Solutions:

```c++
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int pos = 0;
        int count = 0;
        for (int i = 0; i < abbr.length(); ++i) {
            if (!isdigit(abbr[i])) {
                pos += count;
                count = 0;
                if (pos > word.length() || word[pos] != abbr[i])    return false;
                ++pos;
            } else {
                if (count == 0 && abbr[i] == '0')   return false;
                count = 10 * count + (abbr[i] - '0');
            }
        }
        
        pos += count;
        return pos == word.length();
    }
};
```

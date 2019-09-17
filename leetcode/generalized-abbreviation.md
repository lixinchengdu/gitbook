# 320. Generalized Abbreviation

* *Difficulty: Medium*

* *Topics: Backtracking, Bit Manipulation*

* *Similar Questions:*

  * [Subsets](subsets.md)

  * [Unique Word Abbreviation](unique-word-abbreviation.md)

  * [Minimum Unique Word Abbreviation](minimum-unique-word-abbreviation.md)

## Problem:

<p>Write a function to generate the generalized abbreviations of a word.&nbsp;</p>

<p><strong>Note:&nbsp;</strong>The order of the output does not matter.</p>

<p><b>Example:</b></p>

<pre>
<strong>Input:</strong> <code>&quot;word&quot;</code>
<strong>Output:</strong>
[&quot;word&quot;, &quot;1ord&quot;, &quot;w1rd&quot;, &quot;wo1d&quot;, &quot;wor1&quot;, &quot;2rd&quot;, &quot;w2d&quot;, &quot;wo2&quot;, &quot;1o1d&quot;, &quot;1or1&quot;, &quot;w1r1&quot;, &quot;1o2&quot;, &quot;2r1&quot;, &quot;3d&quot;, &quot;w3&quot;, &quot;4&quot;]
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> ret;
        for (int i = 0; i < (1 << word.size()); ++i) {
            string abbr;
            int count = 0;
            for (int j = 0; j < word.size(); ++j) {
                if ((1 << j) & i) ++count;
                else {
                    if (count != 0) {
                        abbr.append(to_string(count));
                        count = 0;
                    }
                    
                    abbr.push_back(word[j]);
                }
            }
            
            if (count != 0) {
                abbr.append(to_string(count));
            }
            
            ret.push_back(abbr);
        }
        
        return ret;
    }
};
```

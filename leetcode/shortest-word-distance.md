# 243. Shortest Word Distance

* *Difficulty: Easy*

* *Topics: Array*

* *Similar Questions:*

  * [Shortest Word Distance II](shortest-word-distance-ii.md)

  * [Shortest Word Distance III](shortest-word-distance-iii.md)

## Problem:

<p>Given a list of words and two words <em>word1</em> and <em>word2</em>, return the shortest distance between these two words in the list.</p>

<p><strong>Example:</strong><br />
Assume that words = <code>[&quot;practice&quot;, &quot;makes&quot;, &quot;perfect&quot;, &quot;coding&quot;, &quot;makes&quot;]</code>.</p>

<pre>
<b>Input:</b> <em>word1</em> = <code>&ldquo;coding&rdquo;</code>, <em>word2</em> = <code>&ldquo;practice&rdquo;</code>
<b>Output:</b> 3
</pre>

<pre>
<b>Input:</b> <em>word1</em> = <code>&quot;makes&quot;</code>, <em>word2</em> = <code>&quot;coding&quot;</code>
<b>Output:</b> 1
</pre>

<p><strong>Note:</strong><br />
You may assume that <em>word1</em> <strong>does not equal to</strong> <em>word2</em>, and <em>word1</em> and <em>word2</em> are both in the list.</p>

## Solutions:

```c++
class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int index1 = -1;
        int index2 = -1;
        
        int distance = INT_MAX;
        
        for (int i = 0; i < words.size(); ++i) {
            if (words[i] == word1) {
                index1 = i;
                if (index2 != -1)
                    distance = min(distance, i - index2);
            } else if (words[i] == word2) {
                index2 = i;
                if (index1 != -1) {
                    distance = min(distance, i - index1);
                }
            }
        }
        
        return distance;
    }
};
```

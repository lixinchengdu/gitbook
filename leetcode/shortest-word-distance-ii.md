# 244. Shortest Word Distance II

* *Difficulty: Medium*

* *Topics: Hash Table, Design*

* *Similar Questions:*

  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)

  * [Shortest Word Distance](shortest-word-distance.md)

  * [Shortest Word Distance III](shortest-word-distance-iii.md)

## Problem:

<p>Design a class which receives a list of words in the constructor, and implements a method that takes two words <em>word1</em> and <em>word2</em> and return the shortest distance between these two words in the list. Your method will be called <em>repeatedly</em> many times with different parameters.&nbsp;</p>

<p><strong>Example:</strong><br />
Assume that words = <code>[&quot;practice&quot;, &quot;makes&quot;, &quot;perfect&quot;, &quot;coding&quot;, &quot;makes&quot;]</code>.</p>

<pre>
<b>Input:</b> <em>word1</em> = <code>&ldquo;coding&rdquo;</code>, <em>word2</em> = <code>&ldquo;practice&rdquo;</code>
<b>Output:</b> 3
</pre>

<pre>
<b>Input:</b> <em>word1</em> = <code>&quot;makes&quot;</code>, <em>word2</em> = <code>&quot;coding&quot;</code>
<b>Output:</b> 1</pre>

<p><strong>Note:</strong><br />
You may assume that <em>word1</em> <strong>does not equal to</strong> <em>word2</em>, and <em>word1</em> and <em>word2</em> are both in the list.</p>

## Solutions:

```c++
class WordDistance {
public:
    WordDistance(vector<string>& words) {
        for (int i = 0; i < words.size(); ++i) {
            wordToIndex[words[i]].push_back(i);
        }
    }
    
    int shortest(string word1, string word2) {
        return shortest(wordToIndex[word1], wordToIndex[word2]);
    }
    
    int shortest(vector<int>& list1, vector<int>& list2) {
        int ret = INT_MAX;
        int pos1 = 0;
        int pos2 = 0;
        int last;
        int lastSource;
        
        if (list1[pos1] < list2[pos2]) {
            last = list1[pos1++];
            lastSource = 1;
        } else {
            last = list2[pos2++];
            lastSource = 2;
        }
        
        while (pos1 < list1.size() && pos2 < list2.size()) {
            if (list1[pos1] < list2[pos2]) {
                if (lastSource == 2) {
                    ret = min(ret, list1[pos1] - last);
                }
                last = list1[pos1++];
                lastSource = 1;
            } else {
                if (lastSource == 1) {
                    ret = min(ret, list2[pos2] - last);
                }
                last = list2[pos2++];
                lastSource = 2;
            }
        }
        
        if (pos1 == list1.size()) {
            ret = min(ret, list2[pos2] - last);
        } else {
            ret = min(ret, list1[pos1] - last);
        }
        
        return ret;
    }
    
private:
    unordered_map<string, vector<int>> wordToIndex;
};

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance* obj = new WordDistance(words);
 * int param_1 = obj->shortest(word1,word2);
 */
```

# 127. Word Ladder

* *Difficulty: Medium*

* *Topics: Breadth-first Search*

* *Similar Questions:*

  * [Word Ladder II](word-ladder-ii.md)

  * [Minimum Genetic Mutation](minimum-genetic-mutation.md)

## Problem:

<p>Given two words (<em>beginWord</em> and <em>endWord</em>), and a dictionary&#39;s word list, find the length of shortest transformation sequence from <em>beginWord</em> to <em>endWord</em>, such that:</p>

<ol>
	<li>Only one letter can be changed at a time.</li>
	<li>Each transformed word must exist in the word list. Note that <em>beginWord</em> is <em>not</em> a transformed word.</li>
</ol>

<p><strong>Note:</strong></p>

<ul>
	<li>Return 0 if there is no such transformation sequence.</li>
	<li>All words have the same length.</li>
	<li>All words contain only lowercase alphabetic characters.</li>
	<li>You may assume no duplicates in the word list.</li>
	<li>You may assume <em>beginWord</em> and <em>endWord</em> are non-empty and are not the same.</li>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>Output: </strong>5

<strong>Explanation:</strong> As one shortest transformation is &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,
return its length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>Output:</strong>&nbsp;0

<strong>Explanation:</strong>&nbsp;The endWord &quot;cog&quot; is not in wordList, therefore no possible<strong>&nbsp;</strong>transformation.
</pre>

<ul>
</ul>

## Solutions:

```c++
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (wordSet.count(endWord) == 0)    return 0;
        unordered_set<string> q1;
        unordered_set<string> q2;
        q1.insert(beginWord);
        q2.insert(endWord);
        int n = beginWord.length();
        
        int level = 0;
        
        while (!(q1.empty() || q2.empty())) {
            ++level;
            int size1 = q1.size();
            int size2 = q2.size();
            
            if (size1 > size2) {
                swap(q1, q2);
            }
            
            unordered_set<string> q;
            
            for (string word : q1) {
                if (q2.count(word) > 0)    return level;
                
                for (int pos = 0; pos < n; ++pos) {
                    char origin = word[pos];
                    for (char letter = 'a'; letter <= 'z'; ++letter) {
                        word[pos] = letter;
                        if  (q1.count(word) == 0 && wordSet.count(word) > 0) {
                            q.insert(word);
                        }
                    }
                    word[pos] = origin;
                }
            }
            swap(q1, q);
        }
        
        return 0;
    }
};
```

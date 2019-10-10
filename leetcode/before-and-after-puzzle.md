# 1132. Before and After Puzzle

* *Difficulty: Medium*

* *Topics: String*

* *Similar Questions:*

## Problem:

<p>Given a list of <code>phrases</code>, generate a list of&nbsp;Before and After puzzles.</p>

<p>A <em>phrase</em> is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are&nbsp;no consecutive spaces&nbsp;in a phrase.</p>

<p><em>Before and After&nbsp;puzzles</em> are phrases that are formed by merging&nbsp;two phrases where the <strong>last&nbsp;word of the first&nbsp;phrase</strong> is the same as the <strong>first word of the second phrase</strong>.</p>

<p>Return the&nbsp;Before and After&nbsp;puzzles that can be formed by every two phrases&nbsp;<code>phrases[i]</code>&nbsp;and&nbsp;<code>phrases[j]</code>&nbsp;where&nbsp;<code>i != j</code>. Note that the order of matching two phrases matters, we want to consider both orders.</p>

<p>You should return a list of&nbsp;<strong>distinct</strong>&nbsp;strings <strong>sorted&nbsp;lexicographically</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> phrases = [&quot;writing code&quot;,&quot;code rocks&quot;]
<strong>Output:</strong> [&quot;writing code rocks&quot;]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> phrases = [&quot;mission statement&quot;,
                  &quot;a quick bite to eat&quot;,
&nbsp;                 &quot;a chip off the old block&quot;,
&nbsp;                 &quot;chocolate bar&quot;,
&nbsp;                 &quot;mission impossible&quot;,
&nbsp;                 &quot;a man on a mission&quot;,
&nbsp;                 &quot;block party&quot;,
&nbsp;                 &quot;eat my words&quot;,
&nbsp;                 &quot;bar of soap&quot;]
<strong>Output:</strong> [&quot;a chip off the old block party&quot;,
&nbsp;        &quot;a man on a mission impossible&quot;,
&nbsp;        &quot;a man on a mission statement&quot;,
&nbsp;        &quot;a quick bite to eat my words&quot;,
         &quot;chocolate bar of soap&quot;]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> phrases = [&quot;a&quot;,&quot;b&quot;,&quot;a&quot;]
<strong>Output:</strong> [&quot;a&quot;]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= phrases.length &lt;= 100</code></li>
	<li><code>1 &lt;= phrases[i].length &lt;= 100</code></li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<string> beforeAndAfterPuzzles(vector<string>& phrases) {
        unordered_map<string, vector<int>> firstWordToPhase;
        
        for (int i = 0; i < phrases.size(); ++i) {
            string firstWord = getFirstWord(phrases[i]);
            firstWordToPhase[firstWord].push_back(i);
        }
        
        set<string> ret;
        for (int i = 0; i < phrases.size(); ++i) {
            int lastWordIndex = getLastWordIndex(phrases[i]);
            string lastWord = phrases[i].substr(lastWordIndex);
            if (firstWordToPhase.count(lastWord) > 0) {
                string prefix = phrases[i].substr(0, lastWordIndex);
                for (auto& j : firstWordToPhase[lastWord]) {
                    if (j == i) continue;
                    ret.insert(prefix + phrases[j]);
                }
            }
        }
        
        return {ret.begin(), ret.end()};
    }
    
private:
    string getFirstWord(const string& str) {
        int pos = 0;
        while (pos < str.length() && str[pos] != ' ') {
            ++pos;
        }
        
        return str.substr(0, pos);
    }
    
    int getLastWordIndex(const string& str) {
        int pos = str.length() - 1;
        while (pos >= 0 && str[pos] != ' ') {
            --pos;
        }
        
        return pos + 1;
    }
    
};
```

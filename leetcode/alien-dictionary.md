# 269. Alien Dictionary

* *Difficulty: Hard*

* *Topics: Graph, Topological Sort*

* *Similar Questions:*

  * [Course Schedule II](course-schedule-ii.md)

## Problem:

<p>There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of <b>non-empty</b> words from the dictionary, where <b>words are sorted lexicographically by the rules of this new language</b>. Derive the order of letters in this language.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong>
[
  &quot;wrt&quot;,
  &quot;wrf&quot;,
  &quot;er&quot;,
  &quot;ett&quot;,
  &quot;rftt&quot;
]

<strong>Output: </strong><code>&quot;wertf&quot;</code>
</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong>
[
  &quot;z&quot;,
  &quot;x&quot;
]

<strong>Output: </strong><code>&quot;zx&quot;</code>
</pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input:</strong>
[
  &quot;z&quot;,
  &quot;x&quot;,
  &quot;z&quot;
] 

<strong>Output:</strong> <code>&quot;&quot;</code>&nbsp;

<strong>Explanation:</strong> The order is invalid, so return <code>&quot;&quot;</code>.
</pre>

<p><b>Note:</b></p>

<ol>
	<li>You may assume all letters are in lowercase.</li>
	<li>You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.</li>
	<li>If the order is invalid, return an empty string.</li>
	<li>There may be multiple valid order of letters, return any one of them is fine.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char, vector<char>> graph;
        unordered_map<char, int> inDegree;
        for (int i = 0; i < words.size(); ++i) {
            for (auto c: words[i]) {
                graph[c];
            }
        }
        
        for (int i = 0; i < words.size() - 1; ++i) {
            vector<char> partialOrder = getPartialOrder(words[i], words[i+1]);
            if (partialOrder.size() == 0)   continue;
            graph[partialOrder[0]].push_back(partialOrder[1]);
            ++inDegree[partialOrder[1]];
        }
        
        string ret;
        queue<char> q;
        for (auto& node : graph) {
            if (inDegree.count(node.first) == 0) { // it is wrong to iterate inDegree directly, becaues for those free chars, it is not in inDegree. 
                q.push(node.first);
            }
        }
        
        
        
        while (!q.empty()) {
            char c = q.front(); q.pop();
            ret.push_back(c);
            for (auto& neighbor : graph[c]) {
                if(--inDegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        for (auto& node : inDegree) {
            if (node.second != 0)   return "";
        }
        
        
        return ret;
    }
    
    vector<char> getPartialOrder(string& smaller, string& larger) {
        for (int i = 0; i < min(smaller.length(), larger.length()); ++i) {
            if (smaller[i] != larger[i]) {
                return {smaller[i], larger[i]};
            }
        }
        
        return {}; 
    }
};
```

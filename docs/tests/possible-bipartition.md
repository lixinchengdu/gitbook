# 922. Possible Bipartition

* *Difficulty: Medium*

* *Topics: Depth-first Search*

* *Similar Questions:*

## Problem:

<p>Given a set of <code>N</code>&nbsp;people (numbered <code>1, 2, ..., N</code>), we would like to split everyone into two groups of <strong>any</strong> size.</p>

<p>Each person may dislike some other people, and they should not go into the same group.&nbsp;</p>

<p>Formally, if <code>dislikes[i] = [a, b]</code>, it means it is not allowed to put the people numbered <code>a</code> and <code>b</code> into the same group.</p>

<p>Return <code>true</code>&nbsp;if and only if it is possible to split everyone into two groups in this way.</p>

<p>&nbsp;</p>

<div>
<div>
<ol>
</ol>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">4</span>, dislikes = <span id="example-input-1-2">[[1,2],[1,3],[2,4]]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation</strong>: group1 [1,4], group2 [2,3]
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">3</span>, dislikes = <span id="example-input-2-2">[[1,2],[1,3],[2,3]]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-3-1">5</span>, dislikes = <span id="example-input-3-2">[[1,2],[2,3],[3,4],[4,5],[1,5]]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 2000</code></li>
	<li><code>0 &lt;= dislikes.length &lt;= 10000</code></li>
	<li><code>1 &lt;= dislikes[i][j] &lt;= N</code></li>
	<li><code>dislikes[i][0] &lt; dislikes[i][1]</code></li>
	<li>There does not exist <code>i != j</code> for which <code>dislikes[i] == dislikes[j]</code>.</li>
</ol>
</div>
</div>
</div>

## Solutions:

```c++
class Solution {
public:
    
    bool dfs(int user, map<int, vector<int>>& userToDislikes, map<int, int>& visited, int color) {
       // cout << user << " " <<  color << endl;
        if (visited.count(user) > 0) {
            if (color == 2) return true;
            return visited[user] == color;
        }
        
        if (color == 2)
            visited[user] = 0;
        else 
            visited[user] = color;
        
        for (auto& rival : userToDislikes[user]) {
            if (!dfs(rival, userToDislikes, visited, 1^color))  return false;
        }
        return true;
    }
    
    
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        map<int,int> visited;
        map<int, vector<int>> userToDislikes;
        
        for (auto& dislike : dislikes) {
            int user1 = dislike[0];
            int user2 = dislike[1];
            userToDislikes[user1].push_back(user2);
            userToDislikes[user2].push_back(user1);
        }
        
        for (int i = 1; i <= N; ++i) {
            if (!dfs(i, userToDislikes, visited, 2))    return false;    
        }
        
        return true;
    }
};
```

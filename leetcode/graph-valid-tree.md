# 261. Graph Valid Tree

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search, Union Find, Graph*

* *Similar Questions:*

  * [Course Schedule](course-schedule.md)

  * [Number of Connected Components in an Undirected Graph](number-of-connected-components-in-an-undirected-graph.md)

## Problem:

<p>Given <code>n</code> nodes labeled from <code>0</code> to <code>n-1</code> and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>n = 5</code>, and <code>edges = [[0,1], [0,2], [0,3], [1,4]]</code>
<strong>Output:</strong> true</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>n = 5, </code>and <code>edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]</code>
<strong>Output:</strong> false</pre>

<p><b>Note</b>: you can assume that no duplicate edges will appear in <code>edges</code>. Since all edges are undirected, <code>[0,1]</code> is the same as <code>[1,0]</code> and thus will not appear together in <code>edges</code>.</p>

## Solutions:

```c++
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph (n);
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        int edgeNum = edges.size();
        
        if (edgeNum != n - 1)   return false;
        vector<bool> visited(n, false);
        int nodeCount = getConnectedNode(0, graph, visited);
        return nodeCount == n;
    }
    
    int getConnectedNode(int start, vector<vector<int>>& graph, vector<bool>& visited) {
        if (visited[start]) return 0;
        int count = 1;
        visited[start] = true;
        for (auto& neighbor : graph[start]) {
            count += getConnectedNode(neighbor, graph, visited);
        }
        
        return count;
    }
};
```

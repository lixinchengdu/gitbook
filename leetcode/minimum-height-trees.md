# 310. Minimum Height Trees

* *Difficulty: Medium*

* *Topics: Breadth-first Search, Graph*

* *Similar Questions:*

  * [Course Schedule](course-schedule.md)

  * [Course Schedule II](course-schedule-ii.md)

## Problem:

<p>For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.</p>

<p><b>Format</b><br />
The graph contains <code>n</code> nodes which are labeled from <code>0</code> to <code>n - 1</code>. You will be given the number <code>n</code> and a list of undirected <code>edges</code> (each edge is a pair of labels).</p>

<p>You can assume that no duplicate edges will appear in <code>edges</code>. Since all edges are undirected, <code>[0, 1]</code> is the same as <code>[1, 0]</code> and thus will not appear together in <code>edges</code>.</p>

<p><b>Example 1 :</b></p>

<pre>
<strong>Input:</strong> <code>n = 4</code>, <code>edges = [[1, 0], [1, 2], [1, 3]]</code>

        0
        |
        1
       / \
      2   3 

<strong>Output:</strong> <code>[1]</code>
</pre>

<p><b>Example 2 :</b></p>

<pre>
<strong>Input:</strong> <code>n = 6</code>, <code>edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]</code>

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

<strong>Output:</strong> <code>[3, 4]</code></pre>

<p><b>Note</b>:</p>

<ul>
	<li>According to the <a href="https://en.wikipedia.org/wiki/Tree_(graph_theory)" target="_blank">definition of tree on Wikipedia</a>: &ldquo;a tree is an undirected graph in which any two vertices are connected by <i>exactly</i> one path. In other words, any connected graph without simple cycles is a tree.&rdquo;</li>
	<li>The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (n == 1) return {0}; // this check is important
        unordered_map<int, vector<int>> neighbors;
        unordered_map<int, int> degree;
        
        for (auto& edge : edges) {
            int node1 = edge[0];
            int node2 = edge[1];
            
            neighbors[node1].push_back(node2);
            neighbors[node2].push_back(node1);
            ++degree[node1];
            ++degree[node2];
        }
        
        vector<int> ret;
        queue<int> q;
        
        
        for (auto it = degree.begin(); it != degree.end(); ++it) {
            if (it->second == 1) {
                q.push(it->first);
            }
        }
        
        
        while(!q.empty()) {
            int size = q.size();
            ret.clear();
            for (int i = 0; i < size; ++i) {
                int node = q.front(); q.pop();
                //cout << node << endl;
                ret.push_back(node);
                for (auto& neighbor : neighbors[node]) {
                    if (--degree[neighbor] == 1) {
                        q.push(neighbor);
                    }
                }
            }
        }
        
        return ret;
    }
};
```

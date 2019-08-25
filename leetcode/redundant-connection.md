# 684. Redundant Connection

* *Difficulty: Medium*

* *Topics: Tree, Union Find, Graph*

* *Similar Questions:*

  * [Redundant Connection II](redundant-connection-ii.md)

  * [Accounts Merge](accounts-merge.md)

## Problem:

<p>
In this problem, a tree is an <b>undirected</b> graph that is connected and has no cycles.
</p><p>
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
</p><p>
The resulting graph is given as a 2D-array of <code>edges</code>.  Each element of <code>edges</code> is a pair <code>[u, v]</code> with <code>u < v</code>, that represents an <b>undirected</b> edge connecting nodes <code>u</code> and <code>v</code>.
</p><p>
Return an edge that can be removed so that the resulting graph is a tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.  The answer edge <code>[u, v]</code> should be in the same format, with <code>u < v</code>.
</p><p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given undirected graph will be like this:
  1
 / \
2 - 3
</pre>
</p>
<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<b>Output:</b> [1,4]
<b>Explanation:</b> The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
</pre>
</p>
<p><b>Note:</b><br />
<li>The size of the input 2D-array will be between 3 and 1000.</li>
<li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>
</p>

<br />

<p>
<b><font color="red">Update (2017-09-26):</font></b><br>
We have overhauled the problem description + test cases and specified clearly the graph is an <b><i>undirected</i></b> graph. For the <b><i>directed</i></b> graph follow up please see <b><a href="https://leetcode.com/problems/redundant-connection-ii/description/">Redundant Connection II</a></b>). We apologize for any inconvenience caused.
</p>
## Solutions:

```c++
class Solution {
public:
    class UF {
        public:
            bool isConnected(int a, int b) {
                return findParents(a) == findParents(b);
            }
        
            void connect(int a, int b) {
                int rootA = findParents(a);
                int rootB = findParents(b);
                parents[rootA] = rootB;
            }
        
            int findParents(int a) {
                if (parents.count(a) == 0 || parents[a] == a) { // check whether parents[a] == a; otherwise infinite resursion. 
                    parents[a] = a;
                } else {
                    parents[a] = findParents(parents[a]);
                }
                return parents[a];
            }
        
        private:
            unordered_map<int, int> parents;
    };
    
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        UF uf;
        for (auto& edge : edges) {
            if (uf.isConnected(edge[0], edge[1]))   return edge;
            else {
                uf.connect(edge[0], edge[1]);
            }
        }
        
        return {};
    }
};
```

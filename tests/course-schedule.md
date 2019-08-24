# 207. Course Schedule

* *Difficulty: Medium*

* *Topics: Depth-first Search, Breadth-first Search, Graph, Topological Sort*

* *Similar Questions:*

  * [Course Schedule II](./tests/course-schedule.md)

  * [Graph Valid Tree](./tests/course-schedule.md)

  * [Minimum Height Trees](./tests/course-schedule.md)

  * [Course Schedule III](./tests/course-schedule.md)

## Problem:

<p>There are a total of <i>n</i> courses you have to take, labeled from <code>0</code> to <code>n-1</code>.</p>

<p>Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: <code>[0,1]</code></p>

<p>Given the total number of courses and a list of prerequisite <b>pairs</b>, is it possible for you to finish all courses?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2, [[1,0]] 
<strong>Output: </strong>true
<strong>Explanation:</strong>&nbsp;There are a total of 2 courses to take. 
&nbsp;            To take course 1 you should have finished course 0. So it is possible.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 2, [[1,0],[0,1]]
<strong>Output: </strong>false
<strong>Explanation:</strong>&nbsp;There are a total of 2 courses to take. 
&nbsp;            To take course 1 you should have finished course 0, and to take course 0 you should
&nbsp;            also have finished course 1. So it is impossible.
</pre>

<p><b>Note:</b></p>

<ol>
	<li>The input prerequisites is a graph represented by <b>a list of edges</b>, not adjacency matrices. Read more about <a href="https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs" target="_blank">how a graph is represented</a>.</li>
	<li>You may assume that there are no duplicate edges in the input prerequisites.</li>
</ol>

## Solutions:

```c++
class Solution {
public:
    bool canFinish(int numCourses, vector<pair<int, int>>& prerequisites) {
        visited.insert(visited.begin(), numCourses, false);
        for (int i = 0; i < numCourses; i++)
        {
            vector <int> tempVector;
            graph.push_back(tempVector);
        }
        for (auto edge: prerequisites)
        {
            graph[edge.second].push_back(edge.first);
        }
        
        for (int i = 0; i < numCourses; i++)
        {
            if (!isValid(i))    return false;
        }
        return true;
    }
    
private:
    vector<bool> visited;
    vector <vector <int> > graph;
    bool isValid(int courseId)
    {
        if (visited[courseId])  return false;
        visited[courseId] = true;
        for (auto neighbor: graph[courseId])
        {
            if (!isValid(neighbor)) return false;
        }
        visited[courseId] = false;
        return true;
    }
    
    
};
```

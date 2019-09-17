# 833. Bus Routes

* *Difficulty: Hard*

* *Topics: Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>We have a list of bus routes. Each <code>routes[i]</code> is a bus route that the i-th bus&nbsp;repeats forever. For example if <code>routes[0] = [1, 5, 7]</code>, this means that the first&nbsp;bus (0-th indexed) travels in the sequence 1-&gt;5-&gt;7-&gt;1-&gt;5-&gt;7-&gt;1-&gt;... forever.</p>

<p>We start at bus stop <code>S</code> (initially not on a bus), and we want to go to bus stop <code>T</code>. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 500</code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10 ^ 6</code>.</li>
</ul>

## Solutions:

```c++
class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int S, int T) {
        if (S == T) return 0;
        map<int, vector<int>> stopToRoutes;
        for (int i = 0; i < routes.size(); ++i) {
            for (int j = 0; j < routes[i].size(); ++j) {
                stopToRoutes[routes[i][j]].push_back(i);
            }
        }
        
        unordered_set<int> visitedStops;
        unordered_set<int> visitedRoutes;
        queue<int> q;
        q.push(S);
        int ret = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                int stop = q.front(); q.pop();
                if (stop == T)  return ret;
                for (auto& route : stopToRoutes[stop]) {
                    if (visitedRoutes.count(route)) continue;
                    visitedRoutes.insert(route);
                    for (auto& neighbor : routes[route]) {
                        if (visitedStops.count(neighbor))   continue;
                        visitedStops.insert(neighbor);
                        q.push(neighbor);
                    }
                }
            }
            ++ret;
        }
        
        return -1;
        
    }
};
```

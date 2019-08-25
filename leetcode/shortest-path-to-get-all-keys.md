# 895. Shortest Path to Get All Keys

* *Difficulty: Hard*

* *Topics: Heap, Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>We are given a 2-dimensional&nbsp;<code>grid</code>.&nbsp;<code>&quot;.&quot;</code> is an empty cell, <code>&quot;#&quot;</code> is&nbsp;a wall, <code>&quot;@&quot;</code> is the starting point, (<code>&quot;a&quot;</code>, <code>&quot;b&quot;</code>, ...) are keys, and (<code>&quot;A&quot;</code>,&nbsp;<code>&quot;B&quot;</code>, ...) are locks.</p>

<p>We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.&nbsp; We cannot walk outside the grid, or walk into a wall.&nbsp; If we walk over a key, we pick it up.&nbsp; We can&#39;t walk over a lock unless we have the corresponding key.</p>

<p>For some <font face="monospace">1 &lt;= K &lt;= 6</font>, there is exactly one lowercase and one uppercase letter of the first <code>K</code> letters of the English alphabet in the grid.&nbsp; This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were&nbsp;chosen in the same order as the English alphabet.</p>

<p>Return the lowest number of moves to acquire all keys.&nbsp; If&nbsp;it&#39;s impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[&quot;@.a.#&quot;,&quot;###.#&quot;,&quot;b.A.B&quot;]</span>
<strong>Output: </strong><span id="example-output-1">8</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[&quot;@..aA&quot;,&quot;..B#.&quot;,&quot;....b&quot;]</span>
<strong>Output: </strong><span id="example-output-2">6</span>
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length&nbsp;&lt;= 30</code></li>
	<li><code>1 &lt;= grid[0].length&nbsp;&lt;= 30</code></li>
	<li><code>grid[i][j]</code> contains only<code> &#39;.&#39;</code>, <code>&#39;#&#39;</code>, <code>&#39;@&#39;</code>,&nbsp;<code>&#39;a&#39;-</code><code>&#39;f</code><code>&#39;</code> and <code>&#39;A&#39;-&#39;F&#39;</code></li>
	<li>The number of keys is in <code>[1, 6]</code>.&nbsp; Each key has a different letter and opens exactly one lock.</li>
</ol>
</div>

## Solutions:

```c++
using namespace std;

class Solution {
public:
 
    struct Status {
        int x;
        int y;
        int keys;
        
        Status(int x, int y, int keys) {
            this->x = x;
            this->y = y;
            this->keys = keys;
        }
        
        bool operator<(const Status& other) const {
            if (x != other.x) {
                return x < other.x;
            }
            
            if (y != other.y) {
                return y < other.y;
            }
            
            return keys < other.keys;
        }
    };

    
    inline bool isKey(char c) {
        return c >= 'a' && c <= 'z';
    }
    
    inline bool isLock(char c) {
        return c >= 'A' && c <= 'Z';
    }
    
    
    int shortestPathAllKeys(vector<string>& grid) {
        int keyCount = 0;
        pair<int, int> startPoint;
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].length();
        if (n == 0) return 0;
        
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (grid[x][y] == '@') {
                    startPoint = {x, y};
                } else if (isKey(grid[x][y])) {
                    ++keyCount;
                }
            }
        }
        
        if (keyCount == 0)  return 0;
        queue<Status> q;
        set<Status> visited;
        q.push({startPoint.first, startPoint.second, 0});
        int steps = 0;
        int allKeys = (1 << keyCount) - 1;
        
        while (!q.empty()) {
            int size = q.size(); // The reason for my mistake is that I first define "int n = q.size()" !!! n outside this code block is shadowed! 
            for (int i = 0; i < size; ++i) {
                Status s = q.front(); q.pop();
                if (s.x < 0 || s.x >= m || s.y < 0 || s.y >= n || grid[s.x][s.y] == '#') continue;
                if (visited.count(s) > 0)   continue;
                visited.insert(s);
                
                if (isKey(grid[s.x][s.y])) {
                    s.keys = ((s.keys) | (1 << (grid[s.x][s.y] - 'a')));
                } else if (isLock(grid[s.x][s.y])) {
                    if (((s.keys >> (grid[s.x][s.y] - 'A')) & 1) != 1) {
                        continue;
                    }
                }
                visited.insert(s);
                
                if (s.keys == allKeys)  return steps;
                
                q.push({s.x + 1, s.y, s.keys});
                q.push({s.x - 1, s.y, s.keys});
                q.push({s.x, s.y + 1, s.keys});
                q.push({s.x, s.y - 1, s.keys});
            }
            ++steps;
        }
        
        return -1;
    }
};
```

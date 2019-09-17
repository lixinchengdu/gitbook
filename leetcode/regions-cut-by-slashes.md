# 999. Regions Cut By Slashes

* *Difficulty: Medium*

* *Topics: Depth-first Search, Union Find, Graph*

* *Similar Questions:*

## Problem:

<p>In a N x N&nbsp;<code>grid</code> composed of 1 x 1 squares, each 1 x 1 square consists of a <code>/</code>, <code>\</code>, or blank space.&nbsp; These characters divide the square into contiguous regions.</p>

<p>(Note that backslash characters are escaped, so a <code>\</code>&nbsp;is represented as <code>&quot;\\&quot;</code>.)</p>

<p>Return the number of regions.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-2-1">[
&nbsp; &quot; /&quot;,
&nbsp; &quot;  &quot;
]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-3-1">[
&nbsp; &quot;\\/&quot;,
&nbsp; &quot;/\\&quot;
]</span>
<strong>Output: </strong><span id="example-output-3">4</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;\\/&quot; refers to \/, and &quot;/\\&quot; refers to /\.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/3.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-4-1">[
&nbsp; &quot;/\\&quot;,
&nbsp; &quot;\\/&quot;
]</span>
<strong>Output: </strong><span id="example-output-4">5</span>
<strong>Explanation: </strong>(Recall that because \ characters are escaped, &quot;/\\&quot; refers to /\, and &quot;\\/&quot; refers to \/.)
The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="width: 82px; height: 82px;" />
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-5-1">[
&nbsp; &quot;//&quot;,
&nbsp; &quot;/ &quot;
]</span>
<strong>Output: </strong><span id="example-output-5">3</span>
<strong>Explanation: </strong>The 2x2 grid is as follows:
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/15/5.png" style="width: 82px; height: 82px;" />
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= grid.length == grid[0].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> is either <code>&#39;/&#39;</code>, <code>&#39;\&#39;</code>, or <code>&#39; &#39;</code>.</li>
</ol>
</div>
</div>
</div>
</div>
</div>
## Solutions:

```c++
class Solution {
public:
    class UF {
    public:
        bool exist(int a) {
            return parents.count(a) > 0;
        }
        
        int getSize() {
            return size;
        }
        
        void add(int a) {
            parents[a] = a;
            ++size;
        }
        
        void connect(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            
            if (rootA != rootB) {
                parents[rootA] = rootB;
                --size;
            }
        }
            
        int find(int x) {
            if (parents.count(x) == 0) {
                parents[x] = x;
                ++size;
            }
            
            if (parents[x] != x) {
                parents[x] = find(parents[x]);
            }
            return parents[x];
        }
    private:
        map<int, int> parents;
        int size = 0;
    };
    
    int regionsBySlashes(vector<string>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        UF uf;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                char c = grid[i][j];
                int gridId = i * n + j;
                if (c == '/') {
                    uf.connect(gridId * 4 + 0, gridId * 4 + 1); // left and up
                    uf.connect(gridId * 4 + 2, gridId * 4 + 3); // right and down
                } else if (c == '\\') {
                    uf.connect(gridId * 4 + 0, gridId * 4 + 3); // left and down
                    uf.connect(gridId * 4 + 1, gridId * 4 + 2); // up and right
                } else {
                    uf.connect(gridId * 4 + 0, gridId * 4 + 1);
                    uf.connect(gridId * 4 + 0, gridId * 4 + 2);
                    uf.connect(gridId * 4 + 0, gridId * 4 + 3); 
                }
                
                if (i > 0) {
                    uf.connect(gridId * 4 + 1, ((i - 1) * n + j) * 4 + 3);
                }
                if (i < m - 1) {
                    uf.connect(gridId * 4 + 3, ((i + 1) * n + j) * 4 + 1);
                }
                if (j > 0) {
                    uf.connect(gridId * 4 + 0, (i * n + j - 1) * 4 + 2);
                }
                if (j < n - 1) {
                    uf.connect(gridId * 4 + 2, (i * n + j + 1) * 4 + 0);
                }
            }
        }
        
        return uf.getSize();
    }
};
```

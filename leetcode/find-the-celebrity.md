# 277. Find the Celebrity

* *Difficulty: Medium*

* *Topics: Array*

* *Similar Questions:*

  * [Find the Town Judge](find-the-town-judge.md)

## Problem:

<p>Suppose you are at a party with <code>n</code> people (labeled from <code>0</code> to <code>n - 1</code>) and among them, there may exist one celebrity. The definition of a celebrity is that all the other <code>n - 1</code> people know him/her but he/she does not know any of them.</p>

<p>Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: &quot;Hi, A. Do you know B?&quot; to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).</p>

<p>You are given a helper function <code>bool knows(a, b)</code> which tells you whether A knows B. Implement a function <code>int findCelebrity(n)</code>.&nbsp;There will be exactly one celebrity if he/she is in the party. Return the celebrity&#39;s label if there is a celebrity in the party. If there is no celebrity, return <code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/02/277_example_1_bold.PNG" style="width: 186px; height: 181px;" />
<pre>
<strong>Input: </strong>graph = <span id="example-input-1-1">[
&nbsp; [1,1,0],
&nbsp; [0,1,0],
&nbsp; [1,1,1]
]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/02/277_example_2.PNG" style="width: 193px; height: 192px;" />
<pre>
<strong>Input: </strong>graph = <span id="example-input-2-1">[
&nbsp; [1,0,1],
&nbsp; [1,1,0],
&nbsp; [0,1,1]
]</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>There is no celebrity.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>The directed graph is represented as an adjacency matrix, which is an&nbsp;<code>n x n</code> matrix where <code>a[i][j] = 1</code> means person&nbsp;<code>i</code> knows person&nbsp;<code>j</code> while&nbsp;<code>a[i][j] = 0</code> means the contrary.</li>
	<li>Remember that you won&#39;t have direct access to the adjacency matrix.</li>
</ol>

## Solutions:

```c++
// Forward declaration of the knows API.
bool knows(int a, int b);

class Solution {
public:
    int findCelebrity(int n) {
        return findCandidate(n);
    }
private:
    int findCandidate(int n) {
        unordered_set<int> candidates;
        for (int i = 0; i < n; ++i) {
            candidates.insert(i);
        }
        
        while (!candidates.empty()) {
            auto it = candidates.begin();
            if (checkCelebrity(n, *it)) return *it;
            candidates.erase(it);
        }
        
        return -1;
    }
    
    bool checkCelebrity(int n, int c) {
        for (int i = 0; i < n; ++i) {
            if (i == c) continue;
            if (knows(c, i) || !knows(i, c))    return false;
        }
        
        return true;
    }
    
};
```

# 666. Path Sum IV

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

  * [Path Sum](path-sum.md)

  * [Path Sum II](path-sum-ii.md)

  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)

  * [Path Sum III](path-sum-iii.md)

## Problem:

<p>If the depth of a tree is smaller than <code>5</code>, then this tree can be represented by a list of three-digits integers.</p>

<p>For each integer in this list:</p>

<ol>
	<li>The hundreds digit represents the depth <code>D</code> of this node, <code>1 &lt;= D &lt;= 4.</code></li>
	<li>The tens digit represents the position <code>P</code> of this node in the level it belongs to, <code>1 &lt;= P &lt;= 8</code>. The position is the same as that in a full binary tree.</li>
	<li>The units digit represents the value <code>V</code> of this node, <code>0 &lt;= V &lt;= 9.</code></li>
</ol>

<p>&nbsp;</p>

<p>Given a list of <code>ascending</code> three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> [113, 215, 221]
<b>Output:</b> 12
<b>Explanation:</b> 
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> [113, 221]
<b>Output:</b> 4
<b>Explanation:</b> 
The tree that the list represents is: 
    3
     \
      1

The path sum is (3 + 1) = 4.
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class Solution {
public:
    int pathSum(vector<int>& nums) {
        if (nums.size() == 0)   return 0;
        sort(nums.begin(), nums.end());
        
        int curLevel = 0;
        vector<int> curLevelVals = {0};
        vector<int> lastLevelVals;
        
        vector<vector<int>> tree;
        
        for (auto num : nums) {
            int level = num/100;
            int pos = (num - level * 100)/10;
            int val = num % 10;
            if (level != curLevel) {
                tree.push_back(lastLevelVals);
                lastLevelVals = curLevelVals;
                curLevelVals.clear();
                curLevelVals.resize(1 << (level - 1), -1);
                curLevel = level;           
            } 
            
            {
                curLevelVals[pos-1] = val + lastLevelVals[(pos-1)/2];
            }
        }
        
        tree.push_back(lastLevelVals); // don't forget to include lastLevelVals
        tree.push_back(curLevelVals);
        
        int sum = 0;
        for (int level = 0; level < tree.size(); ++level) {
            for (int i = 0; i < tree[level].size(); ++i) {
                if (tree[level][i] != -1 && (level == tree.size() - 1 || tree[level+1][2*i] == -1 && tree[level + 1][2*i + 1] == -1)) { // should also include leaf not at last level
                    sum += tree[level][i];
                }
            }
        }
        
        return sum;
    }
};
```

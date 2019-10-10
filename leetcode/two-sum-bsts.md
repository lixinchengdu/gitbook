# 1150. Two Sum BSTs

* *Difficulty: Medium*

* *Topics: Binary Search Tree*

* *Similar Questions:*

  * [Two Sum IV - Input is a BST](two-sum-iv-input-is-a-bst.md)

## Problem:

<p>Given two binary search trees, return <code>True</code>&nbsp;if and only if there is a node in the first tree and a node in the second tree whose values&nbsp;sum up to a given integer&nbsp;<code>target</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/05/31/1368_1_a2.png" style="width: 150px; height: 140px;" /><img alt="" src="https://assets.leetcode.com/uploads/2019/05/31/1368_1_b.png" style="width: 150px; height: 136px;" /></strong></p>

<pre>
<strong>Input:</strong> root1 = [2,1,4], root2 = [1,0,3], target = 5
<strong>Output:</strong> true
<strong>Explanation: </strong>2 and 3 sum up to 5.
</pre>

<p><strong>Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/05/31/1368_2_a.png" style="width: 150px; height: 137px;" /><img alt="" src="https://assets.leetcode.com/uploads/2019/05/31/1368_2_b.png" style="width: 150px; height: 168px;" /></strong></p>

<pre>
<strong>Input:</strong> root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>Each tree has at most <code>5000</code> nodes.</li>
	<li><code>-10^9 &lt;= target, node.val &lt;= 10^9</code></li>
</ul>

## Solutions:

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool twoSumBSTs(TreeNode* root1, TreeNode* root2, int target) {
        unordered_set<int> visited;
        dfs(root1, target, visited, true);
        return dfs(root2, target, visited, false);
    }
    
private:
    bool dfs(TreeNode* root, int target, unordered_set<int>& visited, bool populate) {
        if (root == nullptr)    return false;
        if (populate) {
            visited.insert(root->val);
        } else {
            if (visited.count(target - root->val))  return true;
        }
        
        return dfs(root->left, target, visited, populate) || dfs(root->right, target, visited, populate);
    }
    
};
```

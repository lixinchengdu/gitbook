# 107. Binary Tree Level Order Traversal II

* *Difficulty: Easy*

* *Topics: Tree, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)

  * [Average of Levels in Binary Tree](average-of-levels-in-binary-tree.md)

## Problem:

<p>Given a binary tree, return the <i>bottom-up level order</i> traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).</p>

<p>
For example:<br />
Given binary tree <code>[3,9,20,null,null,15,7]</code>,<br />
<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>
</p>
<p>
return its bottom-up level order traversal as:<br />
<pre>
[
  [15,7],
  [9,20],
  [3]
]
</pre>
</p>
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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ret;
        queue<TreeNode*> q;
        if (root != NULL)   q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ret.push_back(level);
        }
        
        reverse(ret.begin(), ret.end());
        return ret;
    }
};
```

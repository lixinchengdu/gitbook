# 111. Minimum Depth of Binary Tree

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)

  * [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md)

## Problem:

<p>Given a binary tree, find its minimum depth.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given binary tree <code>[3,9,20,null,null,15,7]</code>,</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<p>return its minimum&nbsp;depth = 2.</p>

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
    int minDepth(TreeNode* root) {
        if (root == nullptr)    return 0;
        int ret = INT_MAX;
        if (root->left) {
            ret = min(ret, 1 + minDepth(root->left));
        } 
        
        if (root->right) {
            ret = min(ret, 1 + minDepth(root->right));
        }
        
        return ret == INT_MAX ? 1 : ret;
    }
};
```

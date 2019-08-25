# 98. Validate Binary Search Tree

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)

  * [Find Mode in Binary Search Tree](find-mode-in-binary-search-tree.md)

## Problem:

<p>Given a binary tree, determine if it is a valid binary search tree (BST).</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
    2
   / \
  1   3

<strong>Input:</strong>&nbsp;[2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6

<strong>Input:</strong> [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node&#39;s value is 5 but its right child&#39;s value is 4.
</pre>

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
    bool isValidBST(TreeNode* root) {
        return isValidBSTHelper(root, NULL, NULL);
    }
    
    bool isValidBSTHelper(TreeNode* root, TreeNode*left, TreeNode* right) {
        if (root == NULL)   return true;
        if (left && root->val <= left->val || right && root->val >= right->val) return false;
        return isValidBSTHelper(root->left, left, root) && isValidBSTHelper(root->right, root, right);
    }
};
```

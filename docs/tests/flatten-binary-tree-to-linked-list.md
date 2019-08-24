# 114. Flatten Binary Tree to Linked List

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Flatten a Multilevel Doubly Linked List](./tests/flatten-binary-tree-to-linked-list.md)

## Problem:

<p>Given a binary tree, flatten it to a linked list in-place.</p>

<p>For example, given the following tree:</p>

<pre>
    1
   / \
  2   5
 / \   \
3   4   6
</pre>

<p>The flattened tree should look like:</p>

<pre>
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
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
    void flatten(TreeNode* root) {
        helper (root);
    }
    
    TreeNode* helper(TreeNode* root)
    {
        if (!root)  return NULL;
        if (!root->left && !root->right)    return root;
        if (!root->left)    return  helper(root->right);
        if (!root->right)   {root -> right = root -> left; root-> left = NULL; return helper(root->right);}
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        root-> left = NULL;
        root -> right = left;
        helper(left) -> right = right;
        return helper(root->right);
    }
};
```

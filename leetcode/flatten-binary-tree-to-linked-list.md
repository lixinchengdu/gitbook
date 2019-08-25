# 114. Flatten Binary Tree to Linked List

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Flatten a Multilevel Doubly Linked List](flatten-a-multilevel-doubly-linked-list.md)

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
        TreeNode* dummyHead = new TreeNode(0);
        preorder(root, dummyHead);
    }
    
    void preorder(TreeNode* root, TreeNode*& tail) {
        if (root == NULL)   return;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        
        tail->right = root;
        tail = tail->right;
        root->left = NULL;
        
        
        preorder(left, tail);
        preorder(right, tail);
    }
};
```

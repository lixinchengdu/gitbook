# 94. Binary Tree Inorder Traversal

* *Difficulty: Medium*

* *Topics: Hash Table, Stack, Tree*

* *Similar Questions:*

  * [Validate Binary Search Tree](./tests/binary-tree-inorder-traversal.md)

  * [Binary Tree Preorder Traversal](./tests/binary-tree-inorder-traversal.md)

  * [Binary Tree Postorder Traversal](./tests/binary-tree-inorder-traversal.md)

  * [Binary Search Tree Iterator](./tests/binary-tree-inorder-traversal.md)

  * [Kth Smallest Element in a BST](./tests/binary-tree-inorder-traversal.md)

  * [Closest Binary Search Tree Value II](./tests/binary-tree-inorder-traversal.md)

  * [Inorder Successor in BST](./tests/binary-tree-inorder-traversal.md)

  * [Convert Binary Search Tree to Sorted Doubly Linked List](./tests/binary-tree-inorder-traversal.md)

  * [Minimum Distance Between BST Nodes](./tests/binary-tree-inorder-traversal.md)

## Problem:

<p>Given a binary tree, return the <em>inorder</em> traversal of its nodes&#39; values.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,null,2,3]
   1
    \
     2
    /
   3

<strong>Output:</strong> [1,3,2]</pre>

<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>

## Solutions:

```c++
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> result;
        if(root==NULL) return result;
        vector<int> leftTree;
        leftTree=inorderTraversal(root->left);
        for(vector<int>::iterator it=leftTree.begin(); it!=leftTree.end(); it++)
        {
            result.push_back(*it);
        }
        result.push_back(root->val);
        vector<int> rightTree;
        rightTree=inorderTraversal(root->right);
        for(vector<int>::iterator it=rightTree.begin(); it!=rightTree.end();it++)
        {
            result.push_back(*it);
        }
        return result;
    }
};
```

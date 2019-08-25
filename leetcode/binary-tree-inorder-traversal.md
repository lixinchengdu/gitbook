# 94. Binary Tree Inorder Traversal

* *Difficulty: Medium*

* *Topics: Hash Table, Stack, Tree*

* *Similar Questions:*

  * [Validate Binary Search Tree](validate-binary-search-tree.md)

  * [Binary Tree Preorder Traversal](binary-tree-preorder-traversal.md)

  * [Binary Tree Postorder Traversal](binary-tree-postorder-traversal.md)

  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)

  * [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst.md)

  * [Closest Binary Search Tree Value II](closest-binary-search-tree-value-ii.md)

  * [Inorder Successor in BST](inorder-successor-in-bst.md)

  * [Convert Binary Search Tree to Sorted Doubly Linked List](convert-binary-search-tree-to-sorted-doubly-linked-list.md)

  * [Minimum Distance Between BST Nodes](minimum-distance-between-bst-nodes.md)

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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ret;
        
        TreeNode* cur = root;
        while (cur) {
            TreeNode* pre = cur->left;
            if (pre == nullptr) {
                ret.push_back(cur->val); // visit
                cur = cur->right;
                continue;
            }
            
            while (pre->right != nullptr && pre->right != cur) {
                pre = pre->right;
            }
            
            if (pre->right == nullptr) {
                pre->right = cur;
                cur = cur->left;
            } else {
                pre->right = nullptr;
                ret.push_back(cur->val); // visit
                cur = cur->right;
            }
        }
        
        return ret;
        
    }
};
```

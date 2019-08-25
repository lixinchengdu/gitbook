# 144. Binary Tree Preorder Traversal

* *Difficulty: Medium*

* *Topics: Stack, Tree*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)

  * [Verify Preorder Sequence in Binary Search Tree](verify-preorder-sequence-in-binary-search-tree.md)

  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)

## Problem:

<p>Given a binary tree, return the <em>preorder</em> traversal of its nodes&#39; values.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;<code>[1,null,2,3]</code>
   1
    \
     2
    /
   3

<strong>Output:</strong>&nbsp;<code>[1,2,3]</code>
</pre>

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
    vector<int> preorderTraversal(TreeNode* root) {
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
                ret.push_back(cur->val); // visit
                cur = cur->left;
            } else {
                pre->right = nullptr;
                cur = cur->right;
            }
        }
        
        return ret;
    }
};
```

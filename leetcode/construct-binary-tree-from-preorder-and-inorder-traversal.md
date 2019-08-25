# 105. Construct Binary Tree from Preorder and Inorder Traversal

* *Difficulty: Medium*

* *Topics: Array, Tree, Depth-first Search*

* *Similar Questions:*

  * [Construct Binary Tree from Inorder and Postorder Traversal](construct-binary-tree-from-inorder-and-postorder-traversal.md)

## Problem:

<p>Given preorder and inorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
preorder =&nbsp;[3,9,20,15,7]
inorder = [9,3,15,20,7]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    
    TreeNode* helper(vector<int>& preorder, int preorderLeft, int preorderRight, vector<int>& inorder, int inorderLeft, int inorderRight) {
        if (preorderRight < preorderLeft)   return NULL;
        TreeNode* root = new TreeNode(preorder[preorderLeft]);
        int pos = find(inorder.begin() + inorderLeft, inorder.begin() + inorderRight + 1, preorder[preorderLeft]) - inorder.begin();
        int leftLen = pos - inorderLeft;
        int rightLen = inorderRight - pos;
        root->left = helper(preorder, preorderLeft + 1, preorderLeft + 1 + leftLen - 1, inorder, inorderLeft, pos - 1);
        root->right = helper(preorder, preorderLeft + 1 + leftLen, preorderRight, inorder, pos + 1, inorderRight);
        
        return root;
    }
};
```

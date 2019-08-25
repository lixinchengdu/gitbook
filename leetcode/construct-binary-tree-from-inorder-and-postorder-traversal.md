# 106. Construct Binary Tree from Inorder and Postorder Traversal

* *Difficulty: Medium*

* *Topics: Array, Tree, Depth-first Search*

* *Similar Questions:*

  * [Construct Binary Tree from Preorder and Inorder Traversal](construct-binary-tree-from-preorder-and-inorder-traversal.md)

## Problem:

<p>Given inorder and postorder traversal of a tree, construct the binary tree.</p>

<p><strong>Note:</strong><br />
You may assume that duplicates do not exist in the tree.</p>

<p>For example, given</p>

<pre>
inorder =&nbsp;[9,3,15,20,7]
postorder = [9,15,7,20,3]</pre>

<p>Return the following binary tree:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return helper(inorder, 0, inorder.size() - 1, postorder, 0, postorder.size() - 1);
    }
    
    TreeNode* helper(vector<int>& inorder, int inorderLeft, int inorderRight, vector<int>& postorder, int postorderLeft, int postorderRight) {
        if (inorderRight < inorderLeft) return nullptr;
        if (inorderLeft == inorderRight)    return new TreeNode(inorder[inorderLeft]);
        
        TreeNode* root = new TreeNode(postorder[postorderRight]);
        int pos = find(inorder.begin() + inorderLeft, inorder.begin() + inorderRight + 1, postorder[postorderRight]) - inorder.begin();
        int leftLen = pos - inorderLeft;
        root->left = helper(inorder, inorderLeft, pos - 1, postorder, postorderLeft, postorderLeft + leftLen - 1);
        root->right = helper(inorder, pos + 1, inorderRight, postorder, postorderLeft + leftLen, postorderRight - 1);
        
        return root;
    }
};
```

# 105. Construct Binary Tree from Preorder and Inorder Traversal

* *Difficulty: Medium*

* *Topics: Array, Tree, Depth-first Search*

* *Similar Questions:*

  * [Construct Binary Tree from Inorder and Postorder Traversal](./tests/construct-binary-tree-from-preorder-and-inorder-traversal.md)

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
        return buildTreeHelper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
    
    TreeNode* buildTreeHelper (vector<int>& preorder, int preLeft, int preRight, vector<int>& inorder, int inLeft, int inRight) {
        if (preRight < preLeft) return NULL;
        if (preRight == preLeft)    return new TreeNode(preorder[preRight]);
        
        TreeNode* root = new TreeNode(preorder[preLeft]);
        
        auto it = find(inorder.begin() + inLeft, inorder.begin() + inRight + 1, preorder[preLeft]);
        int rootPosition = it - inorder.begin(); 
        
        root->left = buildTreeHelper (preorder, preLeft + 1, preLeft + rootPosition - inLeft, inorder, inLeft, rootPosition - 1);
        root->right = buildTreeHelper (preorder, preLeft + rootPosition - inLeft + 1, preRight, inorder, rootPosition + 1, inRight);
        
        return root;
    }
};
```

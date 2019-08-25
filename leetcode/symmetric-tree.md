# 101. Symmetric Tree

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search, Breadth-first Search*

* *Similar Questions:*

## Problem:

<p>Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).</p>

<p>For example, this binary tree <code>[1,2,2,3,4,4,3]</code> is symmetric:</p>

<pre>
    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>

<p>&nbsp;</p>

<p>But the following <code>[1,2,2,null,3,null,3]</code> is not:</p>

<pre>
    1
   / \
  2   2
   \   \
   3    3
</pre>

<p>&nbsp;</p>

<p><b>Note:</b><br />
Bonus points if you could solve it both recursively and iteratively.</p>

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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)   return true;
        return isSymmetricHelper(root->left, root->right);
    }
    
    bool isSymmetricHelper(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL)  return true;
        if (left == NULL || right == NULL)  return false;
        
        if (left->val != right->val)    return false;
        return isSymmetricHelper(left->left, right->right) && isSymmetricHelper(left->right, right->left);
    }
};
```

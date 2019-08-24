# 112. Path Sum

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum II](./tests/path-sum.md)

  * [Binary Tree Maximum Path Sum](./tests/path-sum.md)

  * [Sum Root to Leaf Numbers](./tests/path-sum.md)

  * [Path Sum III](./tests/path-sum.md)

  * [Path Sum IV](./tests/path-sum.md)

## Problem:

<p>Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given the below binary tree and <code>sum = 22</code>,</p>

<pre>
      <strong>5</strong>
     <strong>/</strong> \
    <strong>4</strong>   8
   <strong>/</strong>   / \
  <strong>11</strong>  13  4
 /  <strong>\</strong>      \
7    <strong>2</strong>      1
</pre>

<p>return true, as there exist a root-to-leaf path <code>5-&gt;4-&gt;11-&gt;2</code> which sum is 22.</p>

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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL)   return false;
        if (root->left == NULL && root->right != NULL)
            return hasPathSum (root->right, sum-root->val);
        if (root->left != NULL && root->right == NULL)
            return hasPathSum (root->left, sum-root->val);
        if (root->left ==NULL && root->right == NULL)
            return (sum == root->val);
        return (hasPathSum (root->left, sum-root->val) || hasPathSum (root-> right, sum-root->val));
        
    }
};
```

# 112. Path Sum

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum II](path-sum-ii.md)

  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)

  * [Sum Root to Leaf Numbers](sum-root-to-leaf-numbers.md)

  * [Path Sum III](path-sum-iii.md)

  * [Path Sum IV](path-sum-iv.md)

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
        if (root == nullptr)    return false;
        if (root->left == nullptr && root->right == nullptr) {
            return root->val == sum;
        }
        
        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
    }
};
```

# 110. Balanced Binary Tree

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Maximum Depth of Binary Tree](./tests/balanced-binary-tree.md)

## Problem:

<p>Given a binary tree, determine if it is height-balanced.</p>

<p>For this problem, a height-balanced binary tree is defined as:</p>

<blockquote>
<p>a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>
</blockquote>

<p><strong>Example 1:</strong></p>

<p>Given the following tree <code>[3,9,20,null,null,15,7]</code>:</p>

<pre>
    3
   / \
  9  20
    /  \
   15   7</pre>

<p>Return true.<br />
<br />
<strong>Example 2:</strong></p>

<p>Given the following tree <code>[1,2,2,3,3,null,null,4,4]</code>:</p>

<pre>
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
</pre>

<p>Return false.</p>

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
    bool isBalanced(TreeNode* root) {
        if (!root)  return true;
        if (!isBalanced(root->left) || !isBalanced(root->right))    return false;
        return (abs(getHeight(root->left) - getHeight(root->right) ) <= 1 );
    }
    
    int getHeight(TreeNode* root)
    {
        if (!root)  return 0;
        return max(getHeight(root->left), getHeight(root->right)) + 1;
    }
};
```

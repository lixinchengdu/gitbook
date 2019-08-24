# 100. Same Tree

* *Difficulty: Easy*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

## Problem:

<p>Given two binary trees, write a function to check if they are the same or not.</p>

<p>Two binary trees are considered the same if they are structurally identical and the nodes have the same value.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong>     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

<strong>Output:</strong> false
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == NULL && q == NULL) return true;
        if (p == NULL)  return false;
        if (q == NULL)  return false;
        
        return (p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right));
    }
};
```

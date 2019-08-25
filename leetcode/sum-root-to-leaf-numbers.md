# 129. Sum Root to Leaf Numbers

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum](path-sum.md)

  * [Binary Tree Maximum Path Sum](binary-tree-maximum-path-sum.md)

  * [Smallest String Starting From Leaf](smallest-string-starting-from-leaf.md)

## Problem:

<p>Given a binary tree containing digits from <code>0-9</code> only, each root-to-leaf path could represent a number.</p>

<p>An example is the root-to-leaf path <code>1-&gt;2-&gt;3</code> which represents the number <code>123</code>.</p>

<p>Find the total sum of all root-to-leaf numbers.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]
    1
   / \
  2   3
<strong>Output:</strong> 25
<strong>Explanation:</strong>
The root-to-leaf path <code>1-&gt;2</code> represents the number <code>12</code>.
The root-to-leaf path <code>1-&gt;3</code> represents the number <code>13</code>.
Therefore, sum = 12 + 13 = <code>25</code>.</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [4,9,0,5,1]
    4
   / \
  9   0
&nbsp;/ \
5   1
<strong>Output:</strong> 1026
<strong>Explanation:</strong>
The root-to-leaf path <code>4-&gt;9-&gt;5</code> represents the number 495.
The root-to-leaf path <code>4-&gt;9-&gt;1</code> represents the number 491.
The root-to-leaf path <code>4-&gt;0</code> represents the number 40.
Therefore, sum = 495 + 491 + 40 = <code>1026</code>.</pre>

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
    int sumNumbers(TreeNode* root) {
        int ret = 0;
        helper(root, 0, ret);
        return ret;
    }
    
    void helper(TreeNode* root, int path, int& ret) {
        if (root == nullptr) {
            return;
        }
        
        int val = 10 * path + root->val;
        
        if (root->left == nullptr && root->right == nullptr) {
            ret += val;
            return;
        }
        
        if (root->left) {
            helper(root->left, val, ret);
        }
        
        if (root->right) {
            helper(root->right, val, ret);
        }
        
    }
};
```

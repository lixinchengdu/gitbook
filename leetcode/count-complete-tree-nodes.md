# 222. Count Complete Tree Nodes

* *Difficulty: Medium*

* *Topics: Binary Search, Tree*

* *Similar Questions:*

  * [Closest Binary Search Tree Value](closest-binary-search-tree-value.md)

## Problem:

<p>Given a <b>complete</b> binary tree, count the number of nodes.</p>

<p><b>Note: </b></p>

<p><b><u>Definition of a complete binary tree from <a href="http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees" target="_blank">Wikipedia</a>:</u></b><br />
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2<sup>h</sup> nodes inclusive at the last level h.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 
    1
   / \
  2   3
 / \  /
4  5 6

<strong>Output:</strong> 6</pre>

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
    int countNodes(TreeNode* root) {
        if (root == nullptr)    return 0;
        int leftLevel = getLeftLevel(root);
        int rightLevel = getRightLevel(root);
        if (leftLevel == rightLevel) {
            return (1 << leftLevel) - 1;
        } else {
            return 1 + countNodes(root->left) + countNodes(root->right);
        }
    }
    
private:
    int getLeftLevel(TreeNode* root) {
        if (root == nullptr)    return 0;
        return 1 + getLeftLevel(root->left);
    }
    
    int getRightLevel(TreeNode* root) {
        if (root == nullptr)    return 0;
        return 1 + getRightLevel(root->right);
    }
    
};
```

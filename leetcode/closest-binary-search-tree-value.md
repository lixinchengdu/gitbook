# 270. Closest Binary Search Tree Value

* *Difficulty: Easy*

* *Topics: Binary Search, Tree*

* *Similar Questions:*

  * [Count Complete Tree Nodes](count-complete-tree-nodes.md)

  * [Closest Binary Search Tree Value II](closest-binary-search-tree-value-ii.md)

  * [Search in a Binary Search Tree](search-in-a-binary-search-tree.md)

## Problem:

<p>Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.</p>

<p><b>Note:</b></p>

<ul>
	<li>Given target value is a floating point.</li>
	<li>You are guaranteed to have only one unique value in the BST that is closest to the target.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

<strong>Output:</strong> 4
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
    int closestValue(TreeNode* root, double target) {
        int ret = root->val;
        if (root->left) {
            int leftClose = closestValue(root->left, target);
            if (abs(ret - target) > abs(leftClose - target)) {
                ret = leftClose;
            }
        }
        
        if (root->right) {
            int rightClose = closestValue(root->right, target);
            if (abs(ret - target) > abs(rightClose - target)) {
                ret = rightClose;
            }
        }
        
        return ret;
    }
};
```

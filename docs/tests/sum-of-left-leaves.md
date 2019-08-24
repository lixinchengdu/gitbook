# 404. Sum of Left Leaves

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>Find the sum of all left leaves in a given binary tree.</p>

<p><b>Example:</b>
<pre>
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values <b>9</b> and <b>15</b> respectively. Return <b>24</b>.
</pre>
</p>
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
    int sumOfLeftLeaves(TreeNode* root) {
        if (!root)  return 0;
        //if (isLeaf(root)) return 0;
        if (isLeaf(root->left)) return root->left->val + sumOfLeftLeaves(root->right);
        else
            return sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
    }
    
    bool isLeaf(TreeNode* root)
    {
        if (!root)  return false;
        return !root->left && !root->right;
    }
};
```

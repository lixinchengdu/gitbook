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
        int sum = 0;
        if (root->left)
            helper(root->left, sum, true);
        if (root->right) 
            helper(root->right, sum, false);
        return sum;
    }
    
private:
    void helper(TreeNode* root, int& sum, bool left) {
        if (!root->left && !root->right && left) {
            sum += root->val;
        }
        
        if (root->left) {
            helper(root->left, sum, true);
        }
        
        if (root->right) {
            helper(root->right, sum, false);
        }
        
    }
    
};
```

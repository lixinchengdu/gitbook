# 538. Convert BST to Greater Tree

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.</p>

<p>
<b>Example:</b>
<pre>
<b>Input:</b> The root of a Binary Search Tree like this:
              5
            /   \
           2     13

<b>Output:</b> The root of a Greater Tree like this:
             18
            /   \
          20     13
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
    TreeNode* convertBST(TreeNode* root) {
        int sum = 0;
        helper(root, sum);
        return root;
    }
    
private:
    void helper(TreeNode* root, int& sum) {
        if (root == nullptr)    return;
        helper(root->right, sum);
        root->val += sum;
        sum = root->val;
        helper(root->left, sum);
    }
};
```

# 250. Count Univalue Subtrees

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

  * [Subtree of Another Tree](subtree-of-another-tree.md)

  * [Longest Univalue Path](longest-univalue-path.md)

## Problem:

<p>Given a binary tree, count the number of uni-value subtrees.</p>

<p>A Uni-value subtree means all nodes of the subtree have the same value.</p>

<p><b>Example :</b></p>

<pre>
<b>Input:</b>  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

<b>Output:</b> 4
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
    struct UniInfo {
        bool inclusive;
        int num;
        UniInfo (bool inclusive, int num) {
            this->inclusive = inclusive;
            this->num = num;
        }
    };
    
    int countUnivalSubtrees(TreeNode* root) {
        if (root == nullptr)    return 0;
        auto ret = helper(root);
        return ret.num;
    }
    
    UniInfo helper(TreeNode* root) {
        if (root->left == nullptr && root->right == nullptr)    return {true, 1};
        if (root->left == nullptr) {
            auto rightInfo = helper(root->right);
            if (rightInfo.inclusive && root->val == root->right->val) return {true, rightInfo.num + 1};
            return {false, rightInfo.num};
        } else if (root->right == nullptr) {
            auto leftInfo = helper(root->left);
            if (leftInfo.inclusive && root->val == root->left->val) return {true, leftInfo.num + 1};
            return {false, leftInfo.num};
        } else {
            auto leftInfo = helper(root->left);
            auto rightInfo = helper(root->right);
            if (leftInfo.inclusive && rightInfo.inclusive && root->val == root->left->val && root->val == root->right->val) {
                return {true, leftInfo.num + rightInfo.num + 1};
            } else {
                return {false, leftInfo.num + rightInfo.num};
            }
        }
    }
};
```

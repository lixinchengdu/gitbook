# 199. Binary Tree Right Side View

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search, Breadth-first Search*

* *Similar Questions:*

  * [Populating Next Right Pointers in Each Node](populating-next-right-pointers-in-each-node.md)

  * [Boundary of Binary Tree](boundary-of-binary-tree.md)

## Problem:

<p>Given a binary tree, imagine yourself standing on the <em>right</em> side of it, return the values of the nodes you can see ordered from top to bottom.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[1,2,3,null,5,null,4]
<strong>Output:</strong>&nbsp;[1, 3, 4]
<strong>Explanation:
</strong>
   1            &lt;---
 /   \
2     3         &lt;---
 \     \
  5     4       &lt;---
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret;
        helper(root, 0, ret);
        return ret;
    }
    
    void helper(TreeNode* root, int level, vector<int>& ret) {
        if (root == nullptr)    return;
        if (ret.size() == level)    ret.push_back(root->val);
        helper(root->right, level + 1, ret);
        helper(root->left, level + 1, ret);
    }
};
```

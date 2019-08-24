# 145. Binary Tree Postorder Traversal

* *Difficulty: Hard*

* *Topics: Stack, Tree*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](./tests/binary-tree-postorder-traversal.md)

  * [N-ary Tree Postorder Traversal](./tests/binary-tree-postorder-traversal.md)

## Problem:

<p>Given a binary tree, return the <em>postorder</em> traversal of its nodes&#39; values.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;<code>[1,null,2,3]</code>
   1
    \
     2
    /
   3

<strong>Output:</strong>&nbsp;<code>[3,2,1]</code>
</pre>

<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>

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
    vector<int> postorderTraversal(TreeNode* root) {
        vector <int> result;
        if (!root)  return result;
        stk.push(make_pair(root, false));
        while (!stk.empty())
        {
            TreeStackNode n = stk.top();
            stk.pop();
            if (!n.first)   continue;
            if (n.second)   result.push_back(n.first->val);
            else
            {
                stk.push(make_pair(n.first, true));
                if (n.first->right) stk.push(make_pair(n.first->right, false));
                if (n.first->left) stk.push(make_pair(n.first->left, false));
            }
        }
        return result;
    }
    
private:
    typedef pair <TreeNode*, bool>  TreeStackNode;
    stack<TreeStackNode> stk;
    
};
```

# 145. Binary Tree Postorder Traversal

* *Difficulty: Hard*

* *Topics: Stack, Tree*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)

  * [N-ary Tree Postorder Traversal](n-ary-tree-postorder-traversal.md)

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
    TreeNode* reverse(TreeNode* head) {
        TreeNode* dummy = new TreeNode(0);
        TreeNode* next;
        while (head) {
            next = head->right;
            head->right = dummy->right;
            dummy->right = head;
            head = next;
        }
        return dummy->right;
    }

    void visit(TreeNode* from, TreeNode* to, vector<int>& ret) {
        TreeNode* newHead = reverse(from);
        TreeNode* cur = newHead;
        while (cur != nullptr) {
            ret.push_back(cur->val);
            cur = cur->right;
        }
        reverse(newHead);
    } 

    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ret;
        TreeNode* dummy = new TreeNode(0);
        dummy->left = root;

        TreeNode* cur = dummy;
        while (cur) {
            if (cur->left == nullptr) {
                cur = cur->right;
            } else {
                TreeNode* pre = cur->left;

                while (pre->right != nullptr && pre->right != cur) {
                    pre = pre->right;
                }

                if (pre->right == nullptr) {
                    pre->right = cur;
                    cur = cur->left;
                } else {
                    pre->right = nullptr;
                    visit(cur->left, pre, ret);
                    cur = cur->right;
                }
            }
        }
        
        return ret;
    }
};
```

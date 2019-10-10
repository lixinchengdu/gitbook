# 776. N-ary Tree Postorder Traversal

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [Binary Tree Postorder Traversal](binary-tree-postorder-traversal.md)

  * [N-ary Tree Level Order Traversal](n-ary-tree-level-order-traversal.md)

  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)

## Problem:

<p>Given an n-ary tree, return the <i>postorder</i> traversal of its nodes&#39; values.</p>

<p>For example, given a <code>3-ary</code> tree:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>Return its postorder traversal as: <code>[5,6,3,2,4,1]</code>.</p>
&nbsp;

<p><b>Note:</b></p>

<p>Recursive solution is trivial, could you do it iteratively?</p>

## Solutions:

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> ret;
        helper(root, ret);
        return ret;
    }
    
private:
    void helper(Node* root, vector<int>& ret) {
        if (root == nullptr)    return;
        for (auto& child : root->children) {
            helper(child, ret);
        }
        ret.push_back(root->val);
    }
    
};
```

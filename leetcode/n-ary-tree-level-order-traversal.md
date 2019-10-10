# 764. N-ary Tree Level Order Traversal

* *Difficulty: Easy*

* *Topics: Tree, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)

  * [N-ary Tree Preorder Traversal](n-ary-tree-preorder-traversal.md)

  * [N-ary Tree Postorder Traversal](n-ary-tree-postorder-traversal.md)

## Problem:

<p>Given an n-ary tree, return the level order traversal of its nodes&#39; values. (ie, from left to right, level by level).</p>

<p>For example, given a <code>3-ary</code> tree:</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" /></p>

<p>&nbsp;</p>

<p>We should return its level order traversal:</p>

<pre>
[
     [1],
     [3,2,4],
     [5,6]
]
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The depth of the tree is at most <code>1000</code>.</li>
	<li>The total number of nodes is at most <code>5000</code>.</li>
</ol>

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
    vector<vector<int>> levelOrder(Node* root) {
        if (root == nullptr)    return {};
        queue<Node*> q;
        q.push(root);
        
        vector<vector<int>> ret;
        
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            for (int i = 0; i < size; ++i) {
                Node* node = q.front(); q.pop();
                level.push_back(node->val);
                for (auto& child : node->children) {
                    q.push(child);
                }
            }
            ret.push_back(level);
        }
        
        return ret;
    }
};
```

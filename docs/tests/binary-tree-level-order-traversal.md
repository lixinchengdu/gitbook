# 102. Binary Tree Level Order Traversal

* *Difficulty: Medium*

* *Topics: Tree, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Zigzag Level Order Traversal](./tests/binary-tree-level-order-traversal.md)

  * [Binary Tree Level Order Traversal II](./tests/binary-tree-level-order-traversal.md)

  * [Minimum Depth of Binary Tree](./tests/binary-tree-level-order-traversal.md)

  * [Binary Tree Vertical Order Traversal](./tests/binary-tree-level-order-traversal.md)

  * [Average of Levels in Binary Tree](./tests/binary-tree-level-order-traversal.md)

  * [N-ary Tree Level Order Traversal](./tests/binary-tree-level-order-traversal.md)

  * [Cousins in Binary Tree](./tests/binary-tree-level-order-traversal.md)

## Problem:

<p>Given a binary tree, return the <i>level order</i> traversal of its nodes' values. (ie, from left to right, level by level).</p>

<p>
For example:<br />
Given binary tree <code>[3,9,20,null,null,15,7]</code>,<br />
<pre>
    3
   / \
  9  20
    /  \
   15   7
</pre>
</p>
<p>
return its level order traversal as:<br />
<pre>
[
  [3],
  [9,20],
  [15,7]
]
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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*>  q1, q2;
        queue<TreeNode*> *main = &q1, *backup = &q2;
        vector <vector <int> > result;
        if (!root)  return result;
        main -> push(root);
        vector <int> level;
        while(!main->empty() || !backup->empty())
        {
            if (main->empty())
            {
                queue<TreeNode*> *temp;
                temp = main;
                main = backup;
                backup = temp;
                result.push_back(level);
                level.clear();
            }
            TreeNode* top = main->front();
            main->pop();
            if (!top)   continue;
            level.push_back(top->val);
            backup->push(top->left);
            backup->push(top->right);
        }
        return result;
    }
};
```

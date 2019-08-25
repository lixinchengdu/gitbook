# 102. Binary Tree Level Order Traversal

* *Difficulty: Medium*

* *Topics: Tree, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Zigzag Level Order Traversal](binary-tree-zigzag-level-order-traversal.md)

  * [Binary Tree Level Order Traversal II](binary-tree-level-order-traversal-ii.md)

  * [Minimum Depth of Binary Tree](minimum-depth-of-binary-tree.md)

  * [Binary Tree Vertical Order Traversal](binary-tree-vertical-order-traversal.md)

  * [Average of Levels in Binary Tree](average-of-levels-in-binary-tree.md)

  * [N-ary Tree Level Order Traversal](n-ary-tree-level-order-traversal.md)

  * [Cousins in Binary Tree](cousins-in-binary-tree.md)

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
        vector<vector<int>> ret;
        if (root == NULL)   return ret;
        
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            int count = 0;
            vector<int> level;
            for (int i = q.size() - 1; i >= 0; --i) {  // starting from 0 is wrong because q.size() keeps on changing. 
                auto node = q.front(); q.pop();
                level.push_back(node->val);
                if (node->left) {
                    q.push(node->left);
                }
                
                if (node->right) {
                    q.push(node->right);
                }
            }
            
            ret.push_back(level);
        }
        
        return ret;
        
    }
};
```

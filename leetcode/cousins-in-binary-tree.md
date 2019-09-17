# 1035. Cousins in Binary Tree

* *Difficulty: Easy*

* *Topics: Tree, Breadth-first Search*

* *Similar Questions:*

  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)

## Problem:

<p>In a binary tree, the root node is at depth <code>0</code>, and children of each depth <code>k</code> node are at depth <code>k+1</code>.</p>

<p>Two nodes of a binary tree are <em>cousins</em> if they have the same depth, but have <strong>different parents</strong>.</p>

<p>We are given the <code>root</code> of a binary tree with unique values, and the values <code>x</code>&nbsp;and <code>y</code>&nbsp;of two different nodes in the tree.</p>

<p>Return&nbsp;<code>true</code>&nbsp;if and only if the nodes corresponding to the values <code>x</code> and <code>y</code> are cousins.</p>

<p>&nbsp;</p>

<p><strong>Example 1:<br />
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-01.png" style="width: 180px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[1,2,3,4]</span>, x = <span id="example-input-1-2">4</span>, y = <span id="example-input-1-3">3</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:<br />
<img alt="" src="https://assets.leetcode.com/uploads/2019/02/12/q1248-02.png" style="width: 201px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-2-1">[1,2,3,null,4,null,5]</span>, x = <span id="example-input-2-2">5</span>, y = <span id="example-input-2-3">4</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/02/13/q1248-03.png" style="width: 156px; height: 160px;" /></strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-3-1">[1,2,3,null,4]</span>, x = 2, y = 3
<strong>Output: </strong><span id="example-output-3">false</span></pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li>The number of nodes in the tree will be between <code>2</code> and <code>100</code>.</li>
	<li>Each node has a unique integer value from <code>1</code> to <code>100</code>.</li>
</ol>

<div>
<div>
<div>&nbsp;</div>
</div>
</div>
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
    bool isCousins(TreeNode* root, int x, int y) {
        int levels[2] = {-1, -2};
        queue<TreeNode*> q;
        
        int level = 0;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {
                TreeNode* node = q.front(); q.pop();
                if (node == nullptr)   continue;
                if (node->val == x) levels[0] = level;
                if (node->val == y) levels[1] = level;
                if (levels[0] == levels[1]) return true;
                if (node->left && node->right && (node->left->val == x && node->right->val == y || node->left->val == y && node->right->val == x))  return false;
                q.push(node->left);
                q.push(node->right);
            }
            ++level;
        }
        
        return false;
    }
};
```

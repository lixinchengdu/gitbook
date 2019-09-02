# 314. Binary Tree Vertical Order Traversal

* *Difficulty: Medium*

* *Topics: Hash Table*

* *Similar Questions:*

  * [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md)

## Problem:

<p>Given a binary tree, return the <i>vertical order</i> traversal of its nodes&#39; values. (ie, from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <b>left to right</b>.</p>

<p><b>Examples 1:</b></p>

<pre>
<strong>Input:</strong> <code>[3,9,20,null,null,15,7]
</code>
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

<strong>Output:</strong>

[
  [9],
  [3,15],
  [20],
  [7]
]
</pre>

<p><b>Examples 2:</b></p>

<pre>
<strong>Input: </strong><code>[3,9,8,4,0,1,7]

</code>     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7 

<strong>Output:</strong>

[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
</pre>

<p><b>Examples 3:</b></p>

<pre>
<strong>Input:</strong> <code>[3,9,8,4,0,1,7,null,null,null,2,5]</code> (0&#39;s right child is 2 and 1&#39;s left child is 5)

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

<strong>Output:</strong>

[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        queue<pair<TreeNode*, int>> q;
        map<int, vector<int>> verticals;
        
        q.push({root,0});
        
        while(!q.empty()) {
            auto node = q.front(); q.pop();
            if (node.first == nullptr) continue;
            verticals[node.second].push_back(node.first->val);
            q.push({node.first->left, node.second - 1});
            q.push({node.first->right, node.second + 1});
        }
        vector<vector<int>> ret;
        for (auto it = verticals.begin(); it != verticals.end(); ++it) {
            ret.push_back(it->second);
        }
        
        return ret;
        
    }
};
```

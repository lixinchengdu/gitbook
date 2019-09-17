# 366. Find Leaves of Binary Tree

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

## Problem:

<p>Given a binary tree, collect a tree&#39;s nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.</p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4,5]
&nbsp; 
&nbsp;         </span>1
         / \
        2   3
       / \     
      4   5    

<strong>Output: </strong><span id="example-output-1">[[4,5,3],[2],[1]]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Explanation:</strong></p>

<p>1. Removing the leaves <code>[4,5,3]</code> would result in this tree:</p>

<pre>
          1
         / 
        2          
</pre>

<p>&nbsp;</p>

<p>2. Now removing the leaf <code>[2]</code> would result in this tree:</p>

<pre>
          1          
</pre>

<p>&nbsp;</p>

<p>3. Now removing the leaf <code>[1]</code> would result in the empty tree:</p>

<pre>
          []         
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
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> ret;
        visit(root, ret);
        return ret;
    }
    
private:
    int visit(TreeNode* root, vector<vector<int>>& ret) {
        if (root == nullptr)    return -1;
        int leftDepth = visit(root->left, ret);
        int rightDepth = visit(root->right, ret);
        
        int rootDepth = 1 + max(leftDepth, rightDepth);
        if (ret.size() == rootDepth) {
            ret.push_back({});
        }
        ret[rootDepth].push_back(root->val);
        return rootDepth;
    }
    
};
```

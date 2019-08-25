# 113. Path Sum II

* *Difficulty: Medium*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum](path-sum.md)

  * [Binary Tree Paths](binary-tree-paths.md)

  * [Path Sum III](path-sum-iii.md)

  * [Path Sum IV](path-sum-iv.md)

## Problem:

<p>Given a binary tree and a sum, find all root-to-leaf paths where each path&#39;s sum equals the given sum.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p><strong>Example:</strong></p>

<p>Given the below binary tree and <code>sum = 22</code>,</p>

<pre>
      <strong>5</strong>
     <strong>/ \</strong>
    <strong>4   8</strong>
   <strong>/</strong>   / <strong>\</strong>
  <strong>11</strong>  13  <strong>4</strong>
 /  <strong>\</strong>    <strong>/</strong> \
7    <strong>2</strong>  <strong>5</strong>   1
</pre>

<p>Return:</p>

<pre>
[
   [5,4,11,2],
   [5,8,4,5]
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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        vector<vector<int>> ret;
        
        helper(root, sum, path, ret);
        
        return ret;
    }
    
    void helper(TreeNode* root, int sum, vector<int>& path, vector<vector<int>>& ret) {
        if (root == nullptr)    return;
        if (root->left == nullptr && root->right == nullptr) {
            if (sum == root->val) {
                path.push_back(root->val);
                ret.push_back(path);
                path.pop_back();
            }
            return;
        }
        
        int val = root->val;
        path.push_back(val);
        helper(root->left, sum - val, path, ret);
        helper(root->right, sum - val, path, ret);
        path.pop_back();
        
        return;
    }
};
```

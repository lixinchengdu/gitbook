# 124. Binary Tree Maximum Path Sum

* *Difficulty: Hard*

* *Topics: Tree, Depth-first Search*

* *Similar Questions:*

  * [Path Sum](path-sum.md)

  * [Sum Root to Leaf Numbers](sum-root-to-leaf-numbers.md)

  * [Path Sum IV](path-sum-iv.md)

  * [Longest Univalue Path](longest-univalue-path.md)

## Problem:

<p>Given a <strong>non-empty</strong> binary tree, find the maximum path sum.</p>

<p>For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain <strong>at least one node</strong> and does not need to go through the root.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> [1,2,3]

       <strong>1</strong>
      <strong>/ \</strong>
     <strong>2</strong>   <strong>3</strong>

<strong>Output:</strong> 6
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> [-10,9,20,null,null,15,7]

&nbsp;  -10
&nbsp; &nbsp;/ \
&nbsp; 9 &nbsp;<strong>20</strong>
&nbsp; &nbsp; <strong>/ &nbsp;\</strong>
&nbsp; &nbsp;<strong>15 &nbsp; 7</strong>

<strong>Output:</strong> 42
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
    int maxPathSum(TreeNode* root) {
        int maxPathToRoot;
        return helper(root, maxPathToRoot);
    }
    
    int helper(TreeNode* root, int& maxPathToRoot) {
        if (root == nullptr) {
            maxPathToRoot = 0;
            return 0;
        }
        
        int ret = INT_MIN;
        int leftMaxPathToRoot = 0;
        int rightMaxPathToRoot = 0;
        
        if (root->left) {
            ret = max(ret, helper(root->left, leftMaxPathToRoot));
        }
        
        if (root->right) {
            ret = max(ret, helper(root->right, rightMaxPathToRoot));
        }
        
        maxPathToRoot = root->val + max(0, max(leftMaxPathToRoot, rightMaxPathToRoot));
        return max(ret, root->val + max(0, leftMaxPathToRoot) + max(0, rightMaxPathToRoot));
    }
};
```

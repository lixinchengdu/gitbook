# 543. Diameter of Binary Tree

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the <b>longest</b> path between any two nodes in a tree. This path may or may not pass through the root.
</p>

<p>
<b>Example:</b><br />
Given a binary tree <br />
<pre>
          1
         / \
        2   3
       / \     
      4   5    
</pre>
</p>
<p>
Return <b>3</b>, which is the length of the path [4,2,1,3] or [5,2,1,3].
</p>

<p><b>Note:</b>
The length of path between two nodes is represented by the number of edges between them.
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
    int diameterOfBinaryTree(TreeNode* root) {
        int maxLength;
        return helper (root, &maxLength);
    }
    
    int helper(TreeNode* root, int* maxLength)
    {
        if (!root) 
        {
            *maxLength = 0;
            return 0;
        }
        int leftLength;
        int rightLength;
        int leftDiameter = helper(root->left, &leftLength);
        int rightDiameter = helper (root->right, &rightLength);
        *maxLength = max(leftLength, rightLength) + 1;
        return max(max(leftDiameter, rightDiameter), leftLength+rightLength);
    }
};
```

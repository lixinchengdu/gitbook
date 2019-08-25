# 437. Path Sum III

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [Path Sum](path-sum.md)

  * [Path Sum II](path-sum-ii.md)

  * [Path Sum IV](path-sum-iv.md)

  * [Longest Univalue Path](longest-univalue-path.md)

## Problem:

<p>You are given a binary tree in which each node contains an integer value.</p>

<p>Find the number of paths that sum to a given value.</p>

<p>The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).</p>

<p>The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

<p><b>Example:</b>
<pre>
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    <b>5</b>   <b>-3</b>
   <b>/</b> <b>\</b>    <b>\</b>
  <b>3</b>   <b>2</b>   <b>11</b>
 / \   <b>\</b>
3  -2   <b>1</b>

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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
    int pathSum(TreeNode* root, int sum) {
        if (root == nullptr)    return 0;
        return helper(root, sum, 0) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
    
    int helper(TreeNode* root, int sum, int path) {
        if (root == nullptr)    return 0;
        int count = 0;
        count += ((sum == path + root->val) ? 1 : 0);       
        count += helper(root->left, sum, path + root->val);
        count += helper(root->right, sum, path + root->val);
        
        return count;
    }
};
```

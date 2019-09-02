# 653. Two Sum IV - Input is a BST

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [Two Sum](two-sum.md)

  * [Two Sum II - Input array is sorted](two-sum-ii-input-array-is-sorted.md)

  * [Two Sum III - Data structure design](two-sum-iii-data-structure-design.md)

## Problem:

<p>Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

<b>Output:</b> True
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

<b>Output:</b> False
</pre>

<p>&nbsp;</p>

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
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> seen;
        return helper(root, k, seen);
    }
    
private:
    bool helper(TreeNode* root, int k, unordered_set<int>& seen) {
        if (root == nullptr)    return false;
        if (seen.count(k - root->val) > 0)  return true;
        seen.insert(root->val);
        return helper(root->left, k, seen) || helper(root->right, k, seen);
    }
};
```

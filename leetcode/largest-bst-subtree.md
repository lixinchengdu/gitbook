# 333. Largest BST Subtree

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.</p>

<p><b>Note:</b><br />
A subtree must include all of its descendants.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input: </strong>[10,5,15,1,8,null,7]

   10 
   / \ 
<font color="red">  5</font>  15 
<font color="red"> / \</font>   \ 
<font color="red">1   8</font>   7

<strong>Output:</strong> 3
<strong>Explanation: </strong>The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree&#39;s size, which is 3.
</pre>

<p><b>Follow up:</b><br />
Can you figure out ways to solve it with O(n) time complexity?</p>

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
    int largestBSTSubtree(TreeNode* root) {
        int left;
        int right;
        int num = 0;
        helper(root, left, right, num);
        return num;
    }
    
private:
    TreeNode* helper(TreeNode* root, int& left, int& right, int& num) {
        if (root == nullptr)    return nullptr;
        
        int left1 = INT_MAX;
        int right1 = INT_MIN;
        int num1 = 0;
        TreeNode* leftRet = helper(root->left, left1, right1, num1);
        
        int left2 = INT_MAX ;
        int right2 = INT_MIN;
        int num2 = 0;
        TreeNode* rightRet = helper(root->right, left2, right2, num2);
        
        if (leftRet == root->left && rightRet == root->right && root->val > right1 && root->val < left2) {
            num = 1 + num1 + num2;
            left = (num1 == 0 ? root->val : left1);
            right = (num2 == 0 ? root->val : right2);
            return root;
        }
        
        if (num1 >= num2) {
            num = num1;
            return leftRet;
        } else {
            num = num2;
            return rightRet;
        }
        
    }
    
};
```

# 109. Convert Sorted List to Binary Search Tree

* *Difficulty: Medium*

* *Topics: Linked List, Depth-first Search*

* *Similar Questions:*

  * [Convert Sorted Array to Binary Search Tree](convert-sorted-array-to-binary-search-tree.md)

## Problem:

<p>Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.</p>

<p>For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of <em>every</em> node never differ by more than 1.</p>

<p><strong>Example:</strong></p>

<pre>
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
</pre>

## Solutions:

```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == nullptr)    return nullptr;
        int count = 0;
        ListNode* cur = head;
        while (cur) {
            ++count;
            cur = cur->next;
        }
        
        return helper(head, count);        
    }
    
    TreeNode* helper(ListNode*& head, int count) {
        if (count == 0) return nullptr;
        if (count == 1) {
            int val = head->val;
            head = head->next;
            return new TreeNode(val);
        }
        
        int mid = (count+1)/2;
        int leftCount = mid - 1;
        int rightCount = count - 1 - leftCount;
        
        TreeNode* left = helper(head, leftCount);
        
        int val = head->val;
        head = head->next;
        TreeNode* root = new TreeNode(val);
        
        TreeNode* right = helper(head, rightCount);
        
        root->left = left;
        root->right = right;
        return root;
    }
};
```

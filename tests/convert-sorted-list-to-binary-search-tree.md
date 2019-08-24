# 109. Convert Sorted List to Binary Search Tree

* *Difficulty: Medium*

* *Topics: Linked List, Depth-first Search*

* *Similar Questions:*

  * [Convert Sorted Array to Binary Search Tree](./tests/convert-sorted-list-to-binary-search-tree.md)

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
        int cnt = 0;
        ListNode* cur = head;
        while (cur) {
            ++cnt;
            cur = cur-> next;
        }
        
        return sortedListToBSTHelper(head, cnt);
    }
    
    TreeNode* sortedListToBSTHelper(ListNode*& head, int cnt) {
        //cout << head->val << " " << cnt << endl;
        if (cnt == 0)   return NULL;
        if (cnt == 1) {
            TreeNode* root = new TreeNode(head->val);
            head = head->next;
            return root;
        }
        TreeNode* root = NULL;
        TreeNode* left = sortedListToBSTHelper(head, cnt/2);
        
        root = new TreeNode(head->val);
        //cout << "root:" << root->val << endl;
        root->left = left;
        head = head-> next;
        root->right = sortedListToBSTHelper(head, (cnt-1)/2);
        return root;
    }
    
};
```

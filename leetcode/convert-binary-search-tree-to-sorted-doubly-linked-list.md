# 758. Convert Binary Search Tree to Sorted Doubly Linked List

* *Difficulty: Medium*

* *Topics: Linked List, Divide and Conquer, Tree*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)

## Problem:

<p>Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.</p>

<p>Let&#39;s take the following BST as an example, it may help you understand the problem better:</p>
&nbsp;

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/bstdlloriginalbst.png" style="width: 100%; max-width: 300px;" /></p>
&nbsp;

<p>We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.</p>

<p>The figure below shows the circular doubly linked list for the BST above. The &quot;head&quot; symbol means the node it points to is the smallest element of the linked list.</p>
&nbsp;

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/bstdllreturndll.png" style="width: 100%; max-width: 450px;" /></p>
&nbsp;

<p>Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.</p>

<p>The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.</p>
&nbsp;

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/bstdllreturnbst.png" style="width: 100%; max-width: 450px;" /></p>

## Solutions:

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
public:
    Node* treeToDoublyList(Node* root) {
        if (root == NULL)   return NULL;
        Node* dummy = new Node(0, NULL, NULL);
        Node* tail = dummy;
        helper(root, tail);
        tail->right = dummy->right;
        dummy->right->left = tail;
        return dummy->right;
    }
    
    void helper(Node* root, Node*& tail) {
        if (root == NULL)   return;
        Node* left = root->left;
        Node* right = root->right;
        helper(left, tail);
        tail->right = root;
        root->left = tail;
        tail = root;
        helper(right, tail);
    }
};
```

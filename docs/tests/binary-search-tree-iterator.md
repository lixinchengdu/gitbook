# 173. Binary Search Tree Iterator

* *Difficulty: Medium*

* *Topics: Stack, Tree, Design*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](./tests/binary-search-tree-iterator.md)

  * [Flatten 2D Vector](./tests/binary-search-tree-iterator.md)

  * [Zigzag Iterator](./tests/binary-search-tree-iterator.md)

  * [Peeking Iterator](./tests/binary-search-tree-iterator.md)

  * [Inorder Successor in BST](./tests/binary-search-tree-iterator.md)

## Problem:

<p>Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.</p>

<p>Calling <code>next()</code> will return the next smallest number in the BST.</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>Example:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" style="width: 189px; height: 178px;" /></strong></p>

<pre>
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>next()</code> and <code>hasNext()</code> should run in average O(1) time and uses O(<i>h</i>) memory, where <i>h</i> is the height of the tree.</li>
	<li>You may assume that&nbsp;<code>next()</code>&nbsp;call&nbsp;will always be valid, that is, there will be at least a next smallest number in the BST when <code>next()</code> is called.</li>
</ul>

## Solutions:

```c++
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        if (!root)  current = NULL;
        else
            current = root;
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return (current || !rootStack.empty());
    }

    /** @return the next smallest number */
    int next() {
        while (current)    {rootStack.push(current); current = current -> left;}
        if (!rootStack.empty())
        {
            current = rootStack.top();
            rootStack.pop();
            int value =current -> val;
            //rootStack.push(current -> right);
            current = current -> right;
            return value;
        }
    }
    
    stack<TreeNode*> rootStack;
    TreeNode* current;
    
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
```

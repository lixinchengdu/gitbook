# 925. Construct Binary Tree from Preorder and Postorder Traversal

* *Difficulty: Medium*

* *Topics: Tree*

* *Similar Questions:*

## Problem:

<p>Return any binary tree that matches the given preorder and postorder traversals.</p>

<p>Values in the traversals&nbsp;<code>pre</code> and <code>post</code>&nbsp;are distinct&nbsp;positive integers.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>pre = <span id="example-input-1-1">[1,2,4,5,3,6,7]</span>, post = <span id="example-input-1-2">[4,5,2,6,7,3,1]</span>
<strong>Output: </strong><span id="example-output-1">[1,2,3,4,5,6,7]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ul>
	<li><code>1 &lt;= pre.length == post.length &lt;= 30</code></li>
	<li><code>pre[]</code> and <code>post[]</code>&nbsp;are both permutations of <code>1, 2, ..., pre.length</code>.</li>
	<li>It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.</li>
</ul>
</div>

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
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        return constructFromPrePostHelper(pre, 0, pre.size() - 1, post, 0, post.size() - 1);
    }
    
    TreeNode* constructFromPrePostHelper(vector<int>& pre, int preLeft, int preRight, vector<int>& post, int postLeft, int postRight) {
        //cout << preLeft << " " << preRight << " " << postLeft << " " << postRight << endl;
        if (preLeft > preRight)    return NULL;
        TreeNode* root = new TreeNode(pre[preLeft]);
        if (preLeft == preRight)    return root;
        
        int leftChildVal = pre[preLeft + 1];
        int pos = postLeft;
        while (post[pos] != leftChildVal) ++pos;
        TreeNode* leftChild = constructFromPrePostHelper(pre, preLeft + 1, preLeft + 1 + pos - postLeft, post, postLeft, pos);
        TreeNode* rightChild = constructFromPrePostHelper(pre, preLeft + 1 + pos - postLeft + 1, preRight, post, pos + 1, postRight - 1);
        root->left = leftChild;
        root->right = rightChild;
        return root;
    }
};
```

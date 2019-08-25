# 272. Closest Binary Search Tree Value II

* *Difficulty: Hard*

* *Topics: Stack, Tree*

* *Similar Questions:*

  * [Binary Tree Inorder Traversal](binary-tree-inorder-traversal.md)

  * [Closest Binary Search Tree Value](closest-binary-search-tree-value.md)

## Problem:

<p>Given a non-empty binary search tree and a target value, find <i>k</i> values in the BST that are closest to the target.</p>

<p><b>Note:</b></p>

<ul>
	<li>Given target value is a floating point.</li>
	<li>You may assume <i>k</i> is always valid, that is: <i>k</i> &le; total nodes.</li>
	<li>You are guaranteed to have only one unique set of <i>k</i> values in the BST that are closest to the target.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> root = [4,2,5,1,3], target = 3.714286, and <em>k</em> = 2

    4
   / \
  2   5
 / \
1   3

<strong>Output:</strong> [4,3]</pre>

<p><b>Follow up:</b><br />
Assume that the BST is balanced, could you solve it in less than <i>O</i>(<i>n</i>) runtime (where <i>n</i> = total nodes)?</p>

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

class Iterator{
    public:
    Iterator(stack<TreeNode*> stk, bool forward): stk_(stk), forward_(forward) {
        
    }
    
    int next() {
        TreeNode* node = stk_.top(); stk_.pop();
        int ret = node->val;
        node = forward_ ? node->right : node->left;
        while (node) {
            stk_.push(node);
            node = forward_ ? node->left : node->right;
        }
        return ret;
    }
    
    // remember to has peek()
    int peek() {
        return stk_.top()->val;
    }
    
    bool hasNext() {
        return !stk_.empty();
    }
    
    private:
        bool forward_;
        stack<TreeNode*> stk_;
};

class Solution {
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        if (k == 0) return {};
        if (root == NULL)   return {};
        stack<TreeNode*> fstk;
        stack<TreeNode*> bstk;
        findHelper(root, target, fstk, bstk);
        
        Iterator forwardIter = Iterator(fstk, true);
        Iterator backIter = Iterator(bstk, false);
        
        if (forwardIter.peek() <= target) {
            forwardIter.next();
        } else {
            backIter.next();
        }
        
        
        vector<int> ret;
        for (int i = 0; i < k; ++i) {
            if (!forwardIter.hasNext()) {
                ret.push_back(backIter.next());
                continue;
            }
            
            if (!backIter.hasNext()) {
                ret.push_back(forwardIter.next());
                continue;
            }
            
            int forwardVal = forwardIter.peek();
            int backVal = backIter.peek();
            
            if (abs(forwardVal - target) <= abs(backVal - target)) {
                ret.push_back(forwardVal);
                if (forwardIter.hasNext()) {
                    forwardIter.next();
                }
            } else {
                ret.push_back(backVal);
                if (backIter.hasNext()) {
                    backIter.next();
                }
            }
        }
        return ret;
    }
    
    // differciate fstk and bstk!
    void findHelper(TreeNode* root, double target, stack<TreeNode*>& fstk, stack<TreeNode*>& bstk) {   
        if (double(root->val) == target) {
            fstk.push(root);
            bstk.push(root);
            return;
        } 
        
        if (double(root->val) > target) {
            if (root->left) {
                fstk.push(root);
                findHelper(root->left, target, fstk, bstk);
                return;
            }
            
            fstk.push(root);
            bstk.push(root);
            return;
        } 
        if (double(root->val) < target) {
            if (root->right) {
                bstk.push(root);
                findHelper(root->right, target, fstk, bstk);
                return;
            }
            fstk.push(root);
            bstk.push(root);
            return;
        }
    }
};
```

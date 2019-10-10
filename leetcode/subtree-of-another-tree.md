# 572. Subtree of Another Tree

* *Difficulty: Easy*

* *Topics: Tree*

* *Similar Questions:*

  * [Count Univalue Subtrees](count-univalue-subtrees.md)

  * [Most Frequent Subtree Sum](most-frequent-subtree-sum.md)

## Problem:

<p>
Given two non-empty binary trees <b>s</b> and <b>t</b>, check whether tree <b>t</b> has exactly the same structure and node values with a subtree of <b>s</b>. A subtree of <b>s</b> is a tree consists of a node in <b>s</b> and all of this node's descendants. The tree <b>s</b> could also be considered as a subtree of itself.
</p>

<p><b>Example 1:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
</pre>
Given tree t:
<pre>
   4 
  / \
 1   2
</pre>
Return <b>true</b>, because t has the same structure and node values with a subtree of s.
</p>

<p><b>Example 2:</b><br>

Given tree s:
<pre>
     3
    / \
   4   5
  / \
 1   2
    /
   0
</pre>
Given tree t:
<pre>
   4
  / \
 1   2
</pre>
Return <b>false</b>.
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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        int tHash = hash(t);
        int sHash = 0;
        return helper(s, t, tHash, sHash);
        
    }
    
    
private:
    int MOD = 1e6 + 7;
    
    int hash(TreeNode* root) {
        if (root == nullptr) return 0;
        string str = to_string(hash(root->left)) + to_string(root->val) + to_string(hash(root->right));
        return intHash(str);
    }
    
    int intHash(const string& str) {
        int hash = 0x31;
        for (int i = 0; i < str.length(); ++i) {
            hash = (hash * 37 + str[i]) % MOD;
        }
        
        return hash;
    }
    
    bool equal(TreeNode* s, TreeNode* t) {
        if (s == nullptr && t == nullptr)   return true;
        if (s == nullptr)   return false;
        if (t == nullptr)   return false;
        if (s->val != t->val)   return false;
        return equal(s->left, t->left) && equal(s->right, t->right);
    }
    
    bool helper(TreeNode* s, TreeNode* t, int tHash, int& sHash) {
        if (s == nullptr) {
            sHash = 0;
            return s == t;
        }
        
        int leftHash = 0;
        int rightHash = 0;
        bool leftResult = helper(s->left, t, tHash, leftHash);
        bool rightResult = helper(s->right, t, tHash, rightHash);
        
        if (leftResult || rightResult)  return true;
        string str = to_string(leftHash) + to_string(s->val) + to_string(rightHash);
        sHash = intHash(str);
        
        return (sHash == tHash && equal(s, t));
    }
    
};
```

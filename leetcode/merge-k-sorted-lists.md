# 23. Merge k Sorted Lists

* *Difficulty: Hard*

* *Topics: Linked List, Divide and Conquer, Heap*

* *Similar Questions:*

  * [Merge Two Sorted Lists](merge-two-sorted-lists.md)

  * [Ugly Number II](ugly-number-ii.md)

## Problem:

<p>Merge <em>k</em> sorted linked lists and return it as one sorted list. Analyze and describe its complexity.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>
[
&nbsp; 1-&gt;4-&gt;5,
&nbsp; 1-&gt;3-&gt;4,
&nbsp; 2-&gt;6
]
<strong>Output:</strong> 1-&gt;1-&gt;2-&gt;3-&gt;4-&gt;4-&gt;5-&gt;6
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
class Solution {
public:
    struct NodeInfo {
        ListNode* node;
        int srcList;
        
        NodeInfo(ListNode* node, int srcList) {
            this->node = node;
            this->srcList = srcList;
        }
        
        bool operator<(const NodeInfo& another) const {
            return this->node->val < another.node->val;
        }
        
         bool operator>(const NodeInfo& another) const {
            return this->node->val > another.node->val;
        }
    };
    
    
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
        priority_queue<NodeInfo, vector<NodeInfo>, greater<NodeInfo>> pq;
        ListNode* dummyHead = new ListNode(0);
        ListNode* tail = dummyHead;
        for (int i = 0; i < n; ++i) {
            if (lists[i] != NULL) {
                pq.push({lists[i], i});
                lists[i] = lists[i]->next;
            }
        }
        
        while (!pq.empty()) {
            NodeInfo nodeInfo = pq.top(); pq.pop();
            int srcList = nodeInfo.srcList;
            ListNode* node = nodeInfo.node;
            tail->next = node;
            tail = node;
            if (lists[srcList] != NULL) {
                pq.push({lists[srcList], srcList});
                lists[srcList] = lists[srcList]->next;
            }
        }
        
        return dummyHead->next;
    }
};
```

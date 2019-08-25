# 138. Copy List with Random Pointer

* *Difficulty: Medium*

* *Topics: Hash Table, Linked List*

* *Similar Questions:*

  * [Clone Graph](clone-graph.md)

## Problem:

<p>A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.</p>

<p>Return a <a href="https://en.wikipedia.org/wiki/Object_copying#Deep_copy" target="_blank"><strong>deep copy</strong></a> of the list.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://discuss.leetcode.com/uploads/files/1470150906153-2yxeznm.png" style="width: 375px; height: 129px;" /></strong></p>

<pre>
<strong>Input:
</strong><span id="example-input-1-1">{&quot;$id&quot;:&quot;1&quot;,&quot;next&quot;:{&quot;$id&quot;:&quot;2&quot;,&quot;next&quot;:null,&quot;random&quot;:{&quot;$ref&quot;:&quot;2&quot;},&quot;val&quot;:2},&quot;random&quot;:{&quot;$ref&quot;:&quot;2&quot;},&quot;val&quot;:1}
</span>
<b>Explanation:
</b>Node 1&#39;s value is 1, both of its next and random pointer points to Node 2.
Node 2&#39;s value is 2, its next pointer points to null and its random pointer points to itself.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li>You must return the <strong>copy of the given head</strong>&nbsp;as a reference to the cloned list.</li>
</ol>

## Solutions:

```c++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        copyNodes(head);
        copyRandomPointers(head);
        return partition(head);
    }
    
    void copyNodes(Node* head) {
        while (head) {
            Node* nodeCopy = new Node(head->val, head->next, nullptr);
            head->next = nodeCopy;
            head = nodeCopy->next;
        }
    }
    
    void copyRandomPointers(Node* head) {
        while (head) {
            head->next->random = head->random == nullptr ? nullptr : head->random->next; // pay attention to null random pointer
            head = head->next->next;
        }
    }
    
    Node* partition(Node* head) {
        Node* dummy = new Node(0, nullptr, nullptr);
        Node* tail = dummy;
        while (head) {
            tail->next = head->next;
            tail = tail->next;
            head->next = head->next->next;
            head = head->next;
        }
        
        return dummy->next;
    }
};
```

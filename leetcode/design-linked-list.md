# 838. Design Linked List

* *Difficulty: Easy*

* *Topics: Linked List, Design*

* *Similar Questions:*

## Problem:

<p>Design your&nbsp;implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly&nbsp;linked list should have two attributes: <code>val</code>&nbsp;and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code>&nbsp;is&nbsp;a&nbsp;pointer/reference to the next node. If you want to use the doubly linked list,&nbsp;you will need&nbsp;one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.</p>

<p>Implement these functions in your linked list class:</p>

<ul>
	<li>get(index) : Get the value of&nbsp;the <code>index</code>-th&nbsp;node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li>addAtHead(val) : Add a node of value <code>val</code>&nbsp;before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li>addAtTail(val) : Append a node of value <code>val</code>&nbsp;to the last element of the linked list.</li>
	<li>addAtIndex(index, val) : Add a node of value <code>val</code>&nbsp;before the <code>index</code>-th&nbsp;node in the linked list.&nbsp;If <code>index</code>&nbsp;equals&nbsp;to the length of&nbsp;linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. If index is negative, the node will be inserted at the head&nbsp;of the list.</li>
	<li>deleteAtIndex(index) : Delete&nbsp;the <code>index</code>-th&nbsp;node in the linked list, if the index is valid.</li>
</ul>

<p><strong>Example:</strong></p>

<pre>
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1-&gt;2-&gt;3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1-&gt;3
linkedList.get(1);&nbsp;&nbsp;&nbsp;         // returns 3
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of <code>[1, 1000]</code>.</li>
	<li>The number of operations will be in the range of&nbsp;<code>[1, 1000]</code>.</li>
	<li>Please do not use the built-in LinkedList library.</li>
</ul>

## Solutions:

```c++
class MyLinkedList {
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index < 0)  return -1;
        Node* cur = head;
        while (index >= 0) {
            cur = cur->next;
            if (cur == nullptr) return -1;
            --index;
        }
        
        return cur == head ? -1 : cur->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        Node* node = new Node(val);
        node->next = head->next;
        head->next = node;
        if(node->next == nullptr) {
            tail = node;
        }
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        tail->next = new Node(val);
        tail = tail->next;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index < 0) {
            addAtHead(val);
        }
        Node* cur = head;
        while (index > 0) {
            cur = cur->next;
            --index;
            if (cur == nullptr) return;
        }
        
        cur->next = new Node(val, cur->next);
        if (cur->next->next == nullptr) {
            tail = cur->next;
        }
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index < 0)  return;
        Node* prev = head;
        Node* cur = head->next;
        
        while (index > 0) {
            if (cur == nullptr) return;
            prev = cur;
            cur = cur->next;
            --index;
        }
        
        if (cur == nullptr) return;
        prev->next = cur->next;
        if (prev->next == nullptr) {
            tail = prev;
        }
    }
    
private:
    struct Node{
        int val;
        Node* next;
        Node(int val, Node* next = nullptr) {
            this->val = val;
            this->next = next;
        }
    };
    
    Node* head = new Node(0);
    Node* tail = head;
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
```

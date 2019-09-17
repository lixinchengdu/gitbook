# 382. Linked List Random Node

* *Difficulty: Medium*

* *Topics: Reservoir Sampling*

* *Similar Questions:*

  * [Random Pick Index](random-pick-index.md)

## Problem:

<p>Given a singly linked list, return a random node's value from the linked list. Each node must have the <b>same probability</b> of being chosen.</p>

<p><b>Follow up:</b><br />
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?
</p>

<p><b>Example:</b>
<pre>
// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
</pre>
</p>
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
    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    Solution(ListNode* head) {
        this->head = head;
    }
    
    /** Returns a random node's value. */
    int getRandom() {
        int count = 0;
        int val;
        
        ListNode* cur = head;
        while (cur != nullptr) {
            ++count;
            if (rand() % count == 0) {
                val = cur->val;
            }
            cur = cur->next;
        }
        return val;
    }
    
private:
    ListNode* head;
    
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */
```

# 232. Implement Queue using Stacks

* *Difficulty: Easy*

* *Topics: Stack, Design*

* *Similar Questions:*

  * [Implement Stack using Queues](implement-stack-using-queues.md)

## Problem:

<p>Implement the following operations of a queue using stacks.</p>

<ul>
	<li>push(x) -- Push element x to the back of queue.</li>
	<li>pop() -- Removes the element from in front of queue.</li>
	<li>peek() -- Get the front element.</li>
	<li>empty() -- Return whether the queue is empty.</li>
</ul>

<p><b>Example:</b></p>

<pre>
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false</pre>

<p><b>Notes:</b></p>

<ul>
	<li>You must use <i>only</i> standard operations of a stack -- which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.</li>
	<li>You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).</li>
</ul>

## Solutions:

```c++
class MyQueue {
public:
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        stk1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        flip();
        int val = stk2.top();
        stk2.pop();
        return val;
    }
    
    /** Get the front element. */
    int peek() {
        flip();
        return stk2.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        flip();
        return stk2.empty();
    }
    
private:
    void flip() {
        if (stk2.empty()) {
            while (!stk1.empty()) {
                int val = stk1.top(); stk1.pop();
                stk2.push(val);
            }
        }
    }
    
    
    stack<int> stk1;
    stack<int> stk2;
    
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```

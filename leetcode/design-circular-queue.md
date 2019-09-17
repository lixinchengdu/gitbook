# 860. Design Circular Queue

* *Difficulty: Medium*

* *Topics: Design, Queue*

* *Similar Questions:*

  * [Design Circular Deque](design-circular-deque.md)

## Problem:

<p>Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called &quot;Ring Buffer&quot;.</p>

<p>One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.</p>

<p>Your implementation should support following operations:</p>

<ul>
	<li><code>MyCircularQueue(k)</code>: Constructor, set the size of the queue to be k.</li>
	<li><code>Front</code>: Get the front item from the queue. If the queue is empty, return -1.</li>
	<li><code>Rear</code>: Get the last item from the queue. If the queue is empty, return -1.</li>
	<li><code>enQueue(value)</code>: Insert an element into the circular queue. Return true if the operation is successful.</li>
	<li><code>deQueue()</code>: Delete an element from the circular queue. Return true if the operation is successful.</li>
	<li><code>isEmpty()</code>: Checks whether the circular queue is empty or not.</li>
	<li><code>isFull()</code>: Checks whether the circular queue is full or not.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1); &nbsp;// return true
circularQueue.enQueue(2); &nbsp;// return true
circularQueue.enQueue(3); &nbsp;// return true
circularQueue.enQueue(4); &nbsp;// return false, the queue is full
circularQueue.Rear(); &nbsp;// return 3
circularQueue.isFull(); &nbsp;// return true
circularQueue.deQueue(); &nbsp;// return true
circularQueue.enQueue(4); &nbsp;// return true
circularQueue.Rear(); &nbsp;// return 4
</pre>
&nbsp;

<p><strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of [0, 1000].</li>
	<li>The number of operations will be in the range of&nbsp;[1, 1000].</li>
	<li>Please do not use the built-in Queue library.</li>
</ul>

## Solutions:

```c++
class MyCircularQueue {
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        buffer.resize(k+1);
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (isFull())   return false;
        buffer[r] = value;
        r = (r + 1) % buffer.size();
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (isEmpty())  return false;
        f = (f + 1) % buffer.size();
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if(isEmpty())   return -1;
        return buffer[f];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty())  return -1;
        if (r - 1 < 0)  return buffer.back();
        return buffer[r - 1];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return f == r;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return (r + 1) % buffer.size() == f;
    }
    
private:
    vector<int> buffer;
    int f = 0;
    int r = 0;
    int cap;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
```

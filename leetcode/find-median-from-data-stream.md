# 295. Find Median from Data Stream

* *Difficulty: Hard*

* *Topics: Heap, Design*

* *Similar Questions:*

  * [Sliding Window Median](sliding-window-median.md)

## Problem:

<p>Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.</p>
For example,

<p><code>[2,3,4]</code>, the median is <code>3</code></p>

<p><code>[2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code></p>

<p>Design a data structure that supports the following two operations:</p>

<ul>
	<li>void addNum(int num) - Add a integer number from the data stream to the data structure.</li>
	<li>double findMedian() - Return the median of all elements so far.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
addNum(1)
addNum(2)
findMedian() -&gt; 1.5
addNum(3) 
findMedian() -&gt; 2
</pre>

<p>&nbsp;</p>

<p><strong>Follow up:</strong></p>

<ol>
	<li>If all integer numbers from the stream are between 0&nbsp;and 100, how would you optimize it?</li>
	<li>If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?</li>
</ol>

## Solutions:

```c++
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        v2.insert(num);
        if (v2.size() - v1.size() > 1) {
            auto it = v2.begin();
            v1.insert(*it);
            v2.erase(it);
        }
        
        if (v1.size() > 0 && *v1.rbegin() > *v2.begin()) {
            int val1 = *v1.rbegin();
            int val2 = *v2.begin();
            
            v1.erase(--v1.end());
            v2.erase(v2.begin());
            
            v1.insert(val2);
            v2.insert(val1);
        }
    }
    
    double findMedian() {
        return v2.size() > v1.size() ? *v2.begin() : ((double) *v1.rbegin() + (double) *v2.begin()) / 2;
    }
    
private:
    multiset<int> v1;
    multiset<int> v2;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
```

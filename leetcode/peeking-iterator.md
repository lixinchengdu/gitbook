# 284. Peeking Iterator

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [Binary Search Tree Iterator](binary-search-tree-iterator.md)

  * [Flatten 2D Vector](flatten-2d-vector.md)

  * [Zigzag Iterator](zigzag-iterator.md)

## Problem:

<p>Given an Iterator class interface with methods: <code>next()</code> and <code>hasNext()</code>, design and implement a PeekingIterator that support the <code>peek()</code> operation -- it essentially peek() at the element that will be returned by the next call to next().</p>

<p><strong>Example:</strong></p>

<pre>
Assume that the iterator is initialized to the beginning of the list: <strong><code>[1,2,3]</code></strong>.

Call <strong><code>next()</code></strong> gets you <strong>1</strong>, the first element in the list.
Now you call <strong><code>peek()</code></strong> and it returns <strong>2</strong>, the next element. Calling <strong><code>next()</code></strong> after that <i><b>still</b></i> return <strong>2</strong>. 
You call <strong><code>next()</code></strong> the final time and it returns <strong>3</strong>, the last element. 
Calling <strong><code>hasNext()</code></strong> after that should return <strong>false</strong>.
</pre>

<p><b>Follow up</b>: How would you extend your design to be generic and work with all types, not just integer?</p>

## Solutions:

```c++
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.

class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};


class PeekingIterator : public Iterator {
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
        if (Iterator::hasNext()) {
            val = Iterator::next();
            end = false;
        } else {
            end = true;
        }
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        return val;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
        if (!Iterator::hasNext()) {
            end = true;
            return val;
        }
        int ret = val; 
	    val = Iterator::next();
        return ret;
	}

	bool hasNext() const {
	    return !end;
	}
    
private:
    int val;
    bool end;
};
```

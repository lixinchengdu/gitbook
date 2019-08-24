# 146. LRU Cache

* *Difficulty: Medium*

* *Topics: Design*

* *Similar Questions:*

  * [LFU Cache](./tests/lru-cache.md)

  * [Design In-Memory File System](./tests/lru-cache.md)

  * [Design Compressed String Iterator](./tests/lru-cache.md)

## Problem:

<p>Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a>. It should support the following operations: <code>get</code> and <code>put</code>.</p>

<p><code>get(key)</code> - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.<br />
<code>put(key, value)</code> - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.</p>

<p>The cache is initialized with a <strong>positive</strong> capacity.</p>

<p><b>Follow up:</b><br />
Could you do both operations in <b>O(1)</b> time complexity?</p>

<p><b>Example:</b></p>

<pre>
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
</pre>

<p>&nbsp;</p>

## Solutions:

```c++
class LRUCache {
private:
    typedef pair<int,int> Node;
   // {
    //     int key;
   //     int value;
   // } Node;
    unordered_map <int, list<Node>::iterator> cache;
    list <Node> nodeList;
    int _capacity;
public:
    //int cacheSize;
    LRUCache(int capacity) {
      //  cacheSize = 0;
        _capacity = capacity;
    }
    
    int get(int key) {
        if (cache.find(key) == cache.end()) return -1;
        else
        {
            list<Node>::iterator cacheNode = cache[key];
            int val = (*cacheNode).second;
            nodeList.erase(cacheNode);
           // cache.erase(key);
            //Node tempNode = {key, val};
            nodeList.push_front(make_pair(key,val));
            cache[key] = nodeList.begin();
            return val;
        }
    }
    
    void put(int key, int value) {
        //cout << nodeList.size() << endl;
        if (cache.find(key) != cache.end())
        {
            list<Node>::iterator cacheNode = cache[key];
            //int val = cacheNode -> value;
             nodeList.erase(cacheNode);
          //  Node tempNode = {key, value};
            nodeList.push_front(make_pair(key,value));
            cache[key] = nodeList.begin();
        }
        else 
        {
            //Node tempNode = {key, value};
            nodeList.push_front(make_pair(key,value));
            cache[key] = nodeList.begin();
           // cout << "aha!" << endl;
            //cout << cache.size() << endl;
            if (_capacity < nodeList.size())
            {
                Node eraseNode = nodeList.back();
                nodeList.pop_back();
                cache.erase(eraseNode.first);
            }
        }
        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
```

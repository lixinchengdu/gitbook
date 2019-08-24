# 347. Top K Frequent Elements

* *Difficulty: Medium*

* *Topics: Hash Table, Heap*

* *Similar Questions:*

  * [Word Frequency](./tests/top-k-frequent-elements.md)

  * [Kth Largest Element in an Array](./tests/top-k-frequent-elements.md)

  * [Sort Characters By Frequency](./tests/top-k-frequent-elements.md)

  * [Split Array into Consecutive Subsequences](./tests/top-k-frequent-elements.md)

  * [Top K Frequent Words](./tests/top-k-frequent-elements.md)

  * [K Closest Points to Origin](./tests/top-k-frequent-elements.md)

## Problem:

<p>Given a non-empty array of integers, return the <b><i>k</i></b> most frequent elements.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,1,1,2,2,3]</span>, k = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-2-1">[1]</span>, k = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[1]</span></pre>
</div>

<p><b>Note: </b></p>

<ul>
	<li>You may assume <i>k</i> is always valid, 1 &le; <i>k</i> &le; number of unique elements.</li>
	<li>Your algorithm&#39;s time complexity <b>must be</b> better than O(<i>n</i> log <i>n</i>), where <i>n</i> is the array&#39;s size.</li>
</ul>

## Solutions:

```c++
class Solution {
public:

    typedef struct
    {
        int num;
        int freq;
    }   numNode;
    
    class compNumNode
    {
        public:
        bool operator ()(numNode& n1, numNode& n2)
        {
            return n1.freq > n2.freq;
        }
    };

    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        priority_queue <numNode, vector<numNode>, compNumNode> pq;
        unordered_map <int, int> numsToFreq;
        for (int i = 0; i < nums.size(); i++)
        {
            numsToFreq[nums[i]] += 1;
        }
        
        for (auto it = numsToFreq.begin(); it != numsToFreq.end(); it++)
        {
            numNode temp;
            temp.num = it->first, temp.freq = it->second;
            if (pq.size() < k)  {pq.push(temp);}
            else
            {
                numNode cur = pq.top();
                if ( cur.freq > temp.freq) continue;
                else
                {
                    cout << cur.freq << " " << cur.num << endl;
                    cout << temp.freq << " " << temp.num << endl;
                    pq.pop();
                    pq.push(temp);
                }
            }
        }
        
        vector <int> result(pq.size());
        int i = pq.size()-1;
        while (!pq.empty())
        {
            result[i] = (pq.top().num);
            pq.pop();
            i--;
        }
        return result;
        
    }
};
```

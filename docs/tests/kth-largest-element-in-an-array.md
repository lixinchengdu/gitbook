# 215. Kth Largest Element in an Array

* *Difficulty: Medium*

* *Topics: Divide and Conquer, Heap*

* *Similar Questions:*

  * [Wiggle Sort II](./tests/kth-largest-element-in-an-array.md)

  * [Top K Frequent Elements](./tests/kth-largest-element-in-an-array.md)

  * [Third Maximum Number](./tests/kth-largest-element-in-an-array.md)

  * [Kth Largest Element in a Stream](./tests/kth-largest-element-in-an-array.md)

  * [K Closest Points to Origin](./tests/kth-largest-element-in-an-array.md)

## Problem:

<p>Find the <strong>k</strong>th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,1,5,6,4] </code>and k = 2
<strong>Output:</strong> 5
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> <code>[3,2,3,1,2,4,5,5,6] </code>and k = 4
<strong>Output:</strong> 4</pre>

<p><strong>Note: </strong><br />
You may assume k is always valid, 1 &le; k &le; array&#39;s length.</p>

## Solutions:

```c++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        //vector<int> ret;
        return nums[quickSelect(nums, 0, nums.size() - 1, k)];
    }
    
    
    int quickSelect(vector<int>& nums, int start, int end, int k) {
        /*
        for (auto num: nums) {
            cout << num << " ";
        }
        cout << endl;
        cout << "start:" << start << "\t" << "end:" << end << "\t" << "k:" << k << endl;
        */
        if (start == end) return k == 1 ? start: -1;
        if (start > end)    return -1;
        int pivotPos = quickPartition(nums, start, end, nums[start]);
        if (pivotPos - start + 1 > k)  return quickSelect(nums, start, pivotPos -1, k);
        else if (pivotPos - start + 1 < k)  return quickSelect(nums, pivotPos + 1, end, k - (pivotPos - start + 1));
        else return pivotPos;
    }
    
    int quickPartition(vector<int>& nums, int start, int end, int pivot) {
        //swap(nums[start], nums[end]);
        int init = start;
        while (start < end) {
            //cout << "start:" << start << " end: " << end << endl;
            while (start < end && nums[start] >= pivot) {
                start ++;
            }
            while (start < end && nums[end] < pivot) {
                end --;
            }
            if (start < end)    swap(nums[start++], nums[end--]);
        }
        int tureEnd = (nums[start] >= pivot? start : start - 1);
        swap(nums[tureEnd], nums[init]);
        return tureEnd;
    }

};
```

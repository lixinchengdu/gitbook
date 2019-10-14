# Pitfalls

## size() underflow
```c++
for(int i = 0; i < v.size() - 1; ++i) {
  ...
}
```

The return type of `v.size()` is `size_t`. Therefore, it is possible to encounter underflow if `v` is empty. 

## numerical_limits<float> min() v.s. lowest() 
```c++
numerical_limits<float>::min() == 1.17549e-38;
```

It is unexpected the result of `numerical_limits<float>::min()` is the smallest value greater than `0`. To get the minimum float number, the correct constant is `numerical_limits<float>::lowest()`.

REFERCE

[1] [std::numeric_limits](https://en.cppreference.com/w/cpp/types/numeric_limits)

## mask should be unsigned int
```c++
int x = 0x80000000; // the most significant bit is 1
int mask = 0xaaaaaaaa;
(x & mask) >> 1 != (x & 0xaaaaaaaa) >> 1;
```

For singed intergers, the right shift may preserve the most significant bit dependending on the compiler. The type of `x & mask` is still signed int, therefore the result of `(x & mask) >> 1` is `0xc0000000`. On the other hand, the type of `(x & 0xaaaaaaaa)` becomes unsigned int. For unsigned integers, the right shift populates the most signficant bit with 0. Subsequently, `(x & 0xaaaaaaaa) == 0x40000000`.

## array initialization
```c++
int charPos[256] {-1}; // initialization only for 0, not for other values
```
Range initialization only works for `0`.

## mix type of max()
```c++
max(int(tasks.size()), (n + 1) * (maxVal - 1) + maxCount); // for max, we can't mix types.
```

The return type of `vector::size()` is `size_t`.  

## usage of STL iterator
1. Both `prev(it)` and `next(it)` return BidirectionalIterator.  
However, the signature of `advance` is:

```c++
void advance (InputIterator& it, Distance n);
```
It means that advance return void.

2. Both `it++` and `it--` are valid but `it = it + 1` is not.

3. Be careful about the order of the two parameters of `std::distance`. The first parameter should be the first and the second parameter should be last. 

4. Be careful about the boundary! `prev(v.begin()) != v.begin()`. The same is true for `next()` and `advance()`. 

5. `prev(v.end())` return the iterator for the last element.

6. `unordered_map<int>::iterator` is not bidirectional. Therefore, `prev(m.end())` is not correct. Both `advance(m.begin(), 1)` and `next(m.begin())` work.

## abs(x) when x = INT_MIN
Overflow happens in this situation.

## negative number modulus operation
The rule to determine the sign of modulus is explained at one [https://stackoverflow.com/questions/7594508/modulo-operator-with-negative-values](article from StackOverFlow).  
Simple examples are shown below. 

<pre>
(-7/3) => -2
-2 * 3 => -6
so a%b => -1

(7/-3) => -2
-2 * -3 => 6
so a%b => 1
</pre>

## When size() meets minus

The return type of `size()` is `size_t` which is alias of `unsigned int`.  
If the `size()` minus an `int`, the return type is still `size_t`, which will never be smaller than `0`. 

For example,

```c++
 for (int i = 0; i < (int) A.size() - 2; ++i)
```

Without casting, the for loop validation check may not be what the programmer intended.  

## Binary search of pair
Sometimes, pairs are stored in one vector in ascending order by the first element. To binary search for lower/upper bound, one articulated entry is needed for searching. Be careful about the value of the second element. The second element should be of the max value. 

```c++
pair<int, vector<int>> searchEntry = {r, {INT_MAX, INT_MAX, INT_MAX, INT_MAX}}; // super important of the coordinates!

auto it = upper_bound(limits.begin(), limits.end(), searchEntry);
```


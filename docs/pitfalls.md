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

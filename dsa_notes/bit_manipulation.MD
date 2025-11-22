# Bit Manipulation

### Set a bit
x = (1 << 6) | x
# set a 1 at 6th position

### Clear a bit
x = x & ~(1 << 6)
# clear a 1 at 6th position

### Toggle a bit
x = x ^ (1 << 6)
# toggle a 1 at 6th position

### Convert trailing 0's to 1
x = (x - 1) | x

### Extracting the least significant 1 bit
- Two's complement
-x = (~x) + 1
- x & - x

### Masked copy
- Copy bits from B into A where M = 1
A = (B & M) | (A & ~M)

### Swapping two bits
P = (X >> A) ^ (X >> B) & 1
X ^= (P << A)
X ^= (P << B)

### Population count
X = X & (X - 1)


### Counting bit islands
(X & 1) + (count((X^(X >> 1))) / 2)

### Bit scan forwards (BSF)
```c
int BSF(unsigned int x){
    if (x == 0) return -1;
    x = x & - x;
    int count = 0;
    if ((x & 0xffff0000) != 0) count += 16;
    if ((x & 0xff00ff00) != 0) count += 8;
    if ((x & 0xf0f0f0f0) != 0) count += 4;
    if ((x & 0xcccccccc) != 0) count += 2;
    if ((x & 0xaaaaaaaa) != 0) count += 1;
    return count;
}
```


### Next lexicographic permutation
- given a bit string, generate the next permutation above with the same number of 1's.

t = x | (x - 1)
x = (t + 1) | ((~t& - (~t)) - 1) >> (BSF(x) + 1)


### # Function to calculate hamming distance 
```python
def hammingDistance(n1, n2) :

    x = n1 ^ n2 
    setBits = 0

    while (x > 0) :
        setBits += x & 1
        x >>= 1
    
    return setBits 
```
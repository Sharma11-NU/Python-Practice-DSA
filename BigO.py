"""
This is my practice file for the BigO.
What BigO is, what do we understand by O(n) , O(1)

"""

def Count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

print(Count_bits(12))

"""
O(1) means constant time — the work done does not depend on input size.
“Per bit” means for each single bit in the binary representation of a number.

"""
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

A = [3, 1, 2, 4, 7, 6]
even_odd(A)
print(A)

# Author : Kang Ho Dong
# Date : 2019 - 01 - 18
# Title : BOJ 6064
# Link : https://www.acmicpc.net/problem/6064
# Language : Python 3


def GCD(_big, _small):  # Greatest Common Divisor : Euclidean Algorithm
    while True:
        remainder = _big % _small

        if remainder != 0:
            _big = _small
            _small = remainder
        else:
            return _small

def LCD(_gcd, M, N): # Least Common Multiple
    return int(M * N / _gcd)

T = int(input())
# T: Input Data Numbers. Test Case.

while T != 0:
    T -= 1
    # Input Data : M,N,x,y
    M, N, x, y = map(int, input().split())

    if N>M: # Fixed a small nums. (x or y) <M,x> : Big <N,y> : Small
        M,N = N,M
        x,y = y,x

    k = y # k = Answer.
    lcd = LCD(GCD(M, N), M, N)

    while True:

        if M == x and N == y: # Counter Exmaple 1. If Dataset <M,x> and <N,y> are equal. <1:1> <2:2> ...
            print(lcd)
            break

        mod = k%M
        if mod == 0: # Counter Example 2. If k%M == 0. 0 = M
            mod = M

        if mod != x: # Calculate k. x or y is fixed.  like <3:5> <1:5> <9:5> ... until mod == x or k> lcd.
            k += N
        else:
            print(k)
            break

        if k>lcd: # Counter Example 3. k > lcd
            print("-1")
            break

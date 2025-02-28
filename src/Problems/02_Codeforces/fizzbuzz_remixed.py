# https://codeforces.com/problemset/problem/2070/A

# ❌ Wrong Solution ❌
def count_fizzbuzz(n):
    # Count full cycles
    count = (n // 15) * 9
    
    # Count remaining numbers in the last partial cycle
    remainder = n % 15
    for i in range(remainder + 1):
        if i % 3 == i % 5:
            count += 1
    
    return count

# Number of Test cases input
t = int(input())

while t > 0:
    n = int(input())
    print(count_fizzbuzz(n))

    t -= 1

"""
7
0
5
15
42
1337
17101997
998244353

Output:
1
3
4
9
270
3420402
199648872

"""

"""
    FizzBuzz is one of the most well-known problems from coding interviews. In this problem, 
    we will consider a remixed version of FizzBuzz:
    
    Given an integer `n`, process all integers from 0 to `n`. For every integer such that 
    its remainders modulo 3 and modulo 5are the same 
    (so, for every integer `i` such that `i` mod 3 = `i` mod 5), print FizzBuzz.

    However, you don't have to solve it. Instead, given the integer `n`, 
    you have to report how many times the correct solution to that problem will print FizzBuzz.
    
    Input The first line contains one integer t (1 ≤ t ≤ 104) — the number of test cases.
    Each test case contains one line consisting of one integer `n`(0 ≤ n ≤ 10**9)).
    
    Output
    For each test case, print one integer — the number of times the correct solution will print FizzBuzz 
    with the given value of `n`.

    ** Note **
    In the first test case, the solution will print FizzBuzz for the integer 0.
    
    In the second test case, the solution will print FizzBuzz for the integers 0,1,2.
    
    In the third test case, the solution will print FizzBuzz for the integers 0,1,2,15


"""
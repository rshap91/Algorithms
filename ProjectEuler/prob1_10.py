# Project Euler
import time
import numpy as np

def timer(func, *args, **kwargs):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        total_min = round((end - start), 3)
        print("Total Time:", total_min, 'Seconds')
        return ret
    return inner

# 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

@timer
def get_3_5(N):
    # O(N)
    total = 0
    for i in range(N):
        if (i % 3 == 0) or (i % 5 == 0):
            total+=i
    return total


# ex test case
get_3_5(10)
# ex question
get_3_5(1000)
# larger val
get_3_5(1000000)


# ----------------------------------------

# 2
"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

@timer
def even_fibs(N_max):
    # O(N)
    i_prev = 1
    i_curr = 2

    sum_evens = 2

    while i_curr < N_max:
        i_prev, i_curr = i_curr, i_prev+i_curr
        if i_curr %2 == 0:
            sum_evens +=i_curr
    return sum_evens

# test case
even_fibs(35) # 44
# question
even_fibs(4000000)
# big val
# hmmm...
even_fibs(40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

# ----------------------------------------

# 3
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

@timer
def largest_prime_factor(N):
    # O(sqrt(N))?????
    # find large factors
    for i in range(int(math.sqrt(N))+1, 1, -1):
        if N % i != 0:
            continue
        # test if prime
        for j in range(2,int(math.sqrt(i)+1)):
            prime = False
            if i % j ==0:
                break
            prime = True
        if prime:
            return i
    print('No Prime Factors')
    return N

largest_prime_factor(13195)

largest_prime_factor(600851475143)


# ----------------------------------------

# 4
"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


@timer
def largest_palindrome(n_digits):
    start, stop = 10**(n_digits)-1, 10**(n_digits-1)-1
    for i in range(start,stop , -1):
        for j in range(i, stop, -1):
            # test palindrome
            p = i*j
            if p == int(str(p)[::-1]):
                return p
    print("No Palindromes Found.")
    return False

largest_palindrome(2)
largest_palindrome(3)
largest_palindrome(10) # 11 seems to freeze...



# ----------------------------------------

# 5
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
@timer
def smallest_multiple(lower,upper):
    nums = range(lower,upper)
    p = np.prod(nums)

    multiple = p
    for i in range(upper, 0, -1):
        test = multiple/i
        if all([test % n ==0 for n in nums]):
            multiple = test

    return multiple


smallest_multiple(1,20)

# ----------------------------------------

# 6

"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

@timer
def sum_sqr_diffs(N):
    sum_sqr = sum([n**2 for n in range(1,N+1)])
    sqr_sum = sum(range(1,N+1))**2
    return sqr_sum - sum_sqr

sum_sqr_diffs(100)


# ----------------------------------------

# 7
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


@timer
def list_primes(n, nth=None):
    N = n+1 # 0 indexing
    # contains duplicates, but all multiples of every number up to sqrt of N
    not_primes = [j for i in range(2, int(np.sqrt(N))+1) for j in range(i*2,N, i)]

    if nth:
        return sorted(set(range(2,N)).difference(set(not_primes)))[nth-1]
    return sorted(set(range(2,N)).difference(set(not_primes)))

list_primes(1000000, 10001)


# ----------------------------------------

# 8

"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

"""
from functools import reduce

@timer
def largest_adj_product(n_digits):
    num ="""
    7316717653133062491922511967442657474235534919493496983520312774506326239578
    3180169848018694788518438586156078911294949545950173795833195285320880551112
    5406987471585238630507156932909632952274430435576689664895044524452316173185
    6403098711121722383113622298934233803081353362766142828064444866452387493035
    8907296290491560440772390713810515859307960866701724271218839987979087922749
    2190169972088809377665727333001053367881220235421809751254540594752243525849
    0771167055601360483958644670632441572215539753697817977846174064955149290862
    5693219784686224828397224137565705605749026140797296865241453510047482166370
    4844031998900088952434506585412275886668811642717147992444292823086346567481
    3919123162824586178664583591245665294765456828489128831426076900422421902267
    1055626321111109370544217506941658960408071984038509624554443629812309878799
    2724428490918884580156166097919133875499200524063689912560717606058861164671
    0940507754100225698315520005593572972571636269561882670428252483600823257530
    420752963450
    """.replace('\n','').replace(' ','').strip()

    print(len(num))

    largest_prod = 0
    for i in range(len(num)-n_digits):
        p =  np.prod([int(n) for n in num[i:i+n_digits]])
        if p > largest_prod:
            largest_prod=p
    return largest_prod

largest_adj_product(13)



# ----------------------------------------

# 9

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

@timer
def pythag_triplet(n):
    N=n+1
    for a in range(1,N):
        for b in range(a, N-a):
            c = n-a-b
            if a**2 + b**2 == c**2:
                print(a,b,c)
                return np.prod([a,b,c])

pythag_triplet(1000)



# ----------------------------------------

# 10

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


sum(list_primes(2000000))











#

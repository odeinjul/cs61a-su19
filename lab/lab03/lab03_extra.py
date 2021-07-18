""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check(n, k):
        if(k ** 2 > n):
            return True
        if(n % k == 0):
            return False
        return check(n, k + 1)
    return check(n, 2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if (a % b == 0):
        return b
    else:
        return gcd(b, a % b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    def count(n, k):
        sum = 0
        while(n > 0):
            if(n % 10 == k):
                sum += 1
            n //= 10
        return sum
    k = 1
    sum = 0
    while k < 5:
        sum += count(n, k) * count(n, 10-k)
        k += 1
    sum += count(n, 5)*(count(n, 5) - 1)//2
    return sum
    #how to avoid using assignment?
    """
    def count(n, k):
        if n == 0:
            return 0
        if n % 10 == k:
            return 1 + count(n // 10, k)
        return count(n // 10, k)
    if n < 10:
        return 0
    return ten_pairs(n // 10) + count(n // 10, 10 - n % 10)
    
    # Awesome!
    from exuanbo
    """

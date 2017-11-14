def is_prime(n):
    """Test if n has no divisors other than itself and 1."""
    if n == 1:
        return False
    for factor in range(2, n // 2 + 1):
        if n % factor == 0:
            return False
    return True

def is_happy(n):
    """Repeatedly apply the following procedure to n:
        - Square each of the digits of the number.
        - Add the squares together.
    If by doing this you eventually get to 1, then the number is 'happy'."""
    while n != 4:
        digits = list(str(n))
        sumOfSquares = 0
        for digit in digits:
            sumOfSquares += int(digit) ** 2
        if sumOfSquares == 1:
            return True
        n = sumOfSquares
    return False

def is_triangular(n):
    """Test if n is a triangular number."""
    k = 1
    while n > 0:
        n -= k
        if n == 0:
            return True
        k += 1
    return False

def is_square(n):
    """Test if n is a square number."""
    k = 1
    while n > 0:
        n -= k
        if n == 0:
            return True
        k += 2
    return False


def is_smug(n):
    """Test if n is the sum of two square numbers."""
    if n == 1:
        return False
    k = 1
    while 2 * k * k <= n:
        if is_square(n - k * k):
            return True
        k += 1
    return False
    

def is_honest(n):
    """A number n is dishonest if there is a number k such that n//k = k, 
       but k*k is not n. A number is honest if it is not dishonest."""
    for divisor in range(1, n):
        quotient = n // divisor
        if (n // divisor == divisor) and (quotient * quotient != n):
            return False
    return True

def tell(if_true, if_false, result, end):
    """Print the first parameter if result is True, else print the second parameter."""
    if result:
        print(if_true, end=end)
    else:
        print(if_false, end=end)

def main(limit):
    """Computes and prints a number of characteristics about a range of integers."""
    space = "  "
    for n in range(1, limit + 1):
        print(n, end=space)
        tell("prime", "composite", is_prime(n), ", ")
        tell("happy", "unhappy", is_happy(n), ", ")
        tell("triangular", "not triangular", is_triangular(n), ", ")
        tell("square", "not square", is_square(n), ", ")
        tell("smug", "not smug", is_smug(n), ", ")
        tell("honest", "dishnonest", is_honest(n), "\n")
    print("Done")

if __name__ == "__main__":
  main(100)
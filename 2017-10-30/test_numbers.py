from numbers import *


def tell_about(fun, n, should_be):
    if should_be:
        assert fun(n)
    else:
        assert not fun(n)
        
def test_is_prime():
    tell_about(is_prime, 1, False)
    tell_about(is_prime, 2, True)
    tell_about(is_prime, 3, True)
    tell_about(is_prime, 4, False)
    tell_about(is_prime, 5, True)
    tell_about(is_prime, 6, False)
    tell_about(is_prime, 99, False)
    tell_about(is_prime, 97, True)
    tell_about(is_prime, 169, False)

def test_is_happy():
    tell_about(is_happy, 1, True)
    tell_about(is_happy, 5, False)
    tell_about(is_happy, 7, True)
    tell_about(is_happy, 50, False)
    tell_about(is_happy, 79, True)
    tell_about(is_happy, 320, True)
    tell_about(is_happy, 1028, False)

def test_is_triangular():
    tell_about(is_triangular, 1, True)
    tell_about(is_triangular, 2, False)
    tell_about(is_triangular, 3, True)
    tell_about(is_triangular, 5, False)
    tell_about(is_triangular, 6, True)
    tell_about(is_triangular, 21, True)
    tell_about(is_triangular, 30, False)
    tell_about(is_triangular, 55, True)

def test_is_square():
    tell_about(is_square, 1, True)
    tell_about(is_square, 2, False)
    tell_about(is_square, 4, True)
    tell_about(is_square, 8, False)
    tell_about(is_square, 49, True)
    tell_about(is_square, 99, False)
    tell_about(is_square, 100, True)
    tell_about(is_square, 121, True)
    tell_about(is_square, 10000, True)
    tell_about(is_square, 10001, False)

def test_is_smug():
    tell_about(is_smug, 1, False)
    tell_about(is_smug, 2, True)
    tell_about(is_smug, 3, False)
    tell_about(is_smug, 4, False)
    tell_about(is_smug, 5, True)
    tell_about(is_smug, 8, True)
    tell_about(is_smug, 34, True)
    tell_about(is_smug, 46, False)
    tell_about(is_smug, 85, True)
    tell_about(is_smug, 99, False)

def test_is_honest():
    tell_about(is_honest, 1, True)
    tell_about(is_honest, 3, True)
    tell_about(is_honest, 5, False)
    tell_about(is_honest, 36, True)
    tell_about(is_honest, 90, True)
    tell_about(is_honest, 1024, True)
    tell_about(is_honest, 1028, False)
         
def test_large_numbers():
    tell_about(is_prime, 3637, True)
    tell_about(is_prime, 4959709, False)        
    tell_about(is_happy, 123456, True)
    tell_about(is_happy, 1234567, False)        
    tell_about(is_triangular, 5050, True)
    tell_about(is_triangular, 50500, False)        
    tell_about(is_square, 1234321, True)
    tell_about(is_square, 12341234, False)        
    tell_about(is_smug, 10322, True)
    tell_about(is_smug, 12345, False)        
    tell_about(is_honest, 982081, True)
    tell_about(is_honest, 326612, True)
    tell_about(is_honest, 12345, False)

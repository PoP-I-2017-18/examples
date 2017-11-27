def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

def fact(n):
    def fact_helper(n, acc):
        print("Acc = ",acc)
        if n == 0:
            return acc
        else:
            return fact_helper(n-1, acc * n)
    return fact_helper(n,1)
    
print(fact(10))

##def regular(n):
##    base_case
##    computation
##    return (result of computation) combined with (regular (move towards base case))
##
##def tail(n):
##    def helper(n, accumulator):
##        if n == base case:
##            return accumulator
##        computation
##        accumulator = computation combined with accumulator
##        return helper(n decreasing - heading towards base case, accumulator)
##    helper(n, base case)

def is_prime(x): 
	return True

# --------- Version One ------------------

def is_prime(x):
	for i in range(2, x):
		if x % i == 0: 
			return False
	return True

# --------- Version Two ------------------

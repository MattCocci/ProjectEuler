
# Define fast fib function

lookup_dict = {}

def fib_at_n(n):
    if n in lookup_dict:
	return lookup_dict[n]
    elif n==0 or n==1:
	lookup_dict[n] = 1
	return 1
    else:
	lookup_dict[n] = fib_at_n(n-1) + fib_at_n(n-2)
	return fib_at_n(n-1) + fib_at_n(n-2)

def fastfib(n):
    toRet = []
    for i in range(1,n+1):
	toRet.append(fib_at_n(i))
    return toRet


n = 1
summ = 0
while fib_at_n(n) < 4000000:
    proposed = fib_at_n(n)
    if proposed % 2 == 0:
	summ += proposed
    n += 1

print summ


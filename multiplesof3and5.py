# multiples of 3 and 5 below 1000

varList = x for x in range(1000) if x % 3 == 0 or x % 5 == 0

print sum(varList)

# 233168
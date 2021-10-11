def is_divisible_by_k(x, k):
   '''
   Checks whether x is divisible by k.
   '''
   if (x % k) == 0:

   '''
   Store all the integers that are multiples of 2 or 5 or 7 that are lower
   or equal to 1000 (excluding doubles)
   '''
   r = []
for i in range(1000):
    if (is_divisible_by_k(i, 2) and is_divisible_by_k(i, 3) and is_divisible_by_k(i, 7)):
       r.append(i)
   '''
   Sum all the integers that are multiples of 2 or 5 or 7 that are lower
   or equal to 1000 (excluding doubles)
   '''
   sum(r)
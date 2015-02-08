






MAX_K = 16


def is_prime(n):
   '''
   checks if a number is prime
   '''
   if n < 2:
      return False
   if n == 2:
      return True
   for x in range(2, int(n**0.5)+1, 2):
      if n % x == 0:
         return False
   return True

def get_n_primes_above_x(n, x):
   '''
   steps forward until n primes (other than 2) have been
   found that are smaller than x.
   '''
   primes = []
   i = x+1
   if i % 2 == 0:
      i += 1
   while len(primes) != n and i > 0:
      if is_prime(i):
         primes.append(i)
      i += 2
   return primes




def hash(word):
    assert len(word) <= MAX_K

    value = 0
    for n, ch in enumerate(word):
        value += ord(ch) * 128**n

    return value


ws = ['cognizant','peace']
for w in ws:
    print hash(w)
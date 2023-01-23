def getPrimes(userNum):
  primes = []
  count = userNum
  while count > 1:
    if userNum % count == 0:
      primes.append(count)
    count -=1
  return primes

userNum = float(input('enter a number:'))
outPrime = getPrimes(userNum)
print(outPrime)
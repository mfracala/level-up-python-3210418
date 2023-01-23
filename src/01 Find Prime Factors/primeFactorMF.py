def getPrimes(userNum):
  primes = []
  factor = 2
  while factor <= userNum:
    if userNum % factor == 0:
      primes.append(factor)
      userNum = userNum//factor
    else:
      factor +=1   
  return primes

userNum = float(input('enter a number:'))
outPrime = getPrimes(userNum)
print(outPrime)
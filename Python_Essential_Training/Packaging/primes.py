def isPrime(n,foundPrimes=None):
    foundPrimes = range(2,int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes(max):
    foundPrimes = []
    for i in range(2,max):
        if isPrime(i,foundPrimes):
            foundPrimes.append(i)
    return foundPrimes
if __name__ == "__main__":
    print(f"This is Module. Import & Use it")

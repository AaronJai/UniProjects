
from math import sqrt


def countprimesmall(xs):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range (2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    count = 0
    for num in range (2, xs+1):
        if is_prime(num):
            count += 1
            
    return count

x = int(input().strip())

print(countprimesmall(x))

def prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

n =7
if prime(n):
    print("prime number")
else:
    print("not prime number")

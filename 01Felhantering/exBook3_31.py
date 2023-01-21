
def is_prime(n):
    numbers = range(2,n) # create list on all numbers below n
    for number in numbers:
        if n%number == 0:
            print(f"{n} / {number}")
            return False
    return True

for n in range(1,1001):
    if is_prime(n):
        print(n)

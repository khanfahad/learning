num = input("Prime Checker: ")

def is_prime(num):
    prime = 0
    for i in range(2,int(num),1):
        if int(num) % i == 0:
            prime = 1
    return prime

x = is_prime(num)
if x == 1:
    print("Not a Prime")
elif x == 0:
    print("Prime")

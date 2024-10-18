# is paindrome:
def ispalindrome(str):
    startindex = 0
    endindex = len(str) -1

    for x in range(len(str)):
        if str[startindex] != str[endindex]:
            return False
    return True

print(ispalindrome('rececar'))


# fibnocci series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# find max numer

a = [0 ,1,2,3,4,5,6,7,8,9]
max_number = a[0]
for i in range(len(a)):
    if i > max_number:
        max_number = i
print(max_number)


# factorial number:

def find_factorial(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial(n-1)
print(find_factorial(5))

# find prime number:

a = int(input("Enter a Number:"))

if a >= 1 and a % 2 != 0 :
    print("This ia prime number:",a)
else:
    print("Not a prime number:")

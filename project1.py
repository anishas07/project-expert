#number1
def mul_(n,m):
    result = 0
    for _ in range(n):
        result +=m
    return result


#number2
def mul2(n,m):
    result = 0
    for i in range(n):
        for _ in range(1):
            result += m
    return result

#number3
n=5
m=3

print("multiply using one loop:", mul_(n,m))

print("Multiply using N loops:", mul_(n,m))

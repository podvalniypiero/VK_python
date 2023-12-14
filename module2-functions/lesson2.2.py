# def fibo(n):
#     if n == 1 or n==2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# n = int(input())
# print(fibo(n))

def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a
n = int(input())
print(fib(n))
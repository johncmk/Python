'''Dynamic programming example: memoized fib'''

'''Abstract characteristics of DP algorithms

* Small(linear) # of subproblems
* Can solve larger subproblems quickly based on the solutions of previously computed subproblems(Memoization)
* Solving all the subproblems makes it trivial to provide final solution'''

'''This is non memoized version, therefore it will be extremely slow 
if the compute number is approximately at most 50'''
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

'''This is memoized version, it's using d as global variable stores the result of the computation, therefore
the fib2 doesn't need to repeat'''
d = {}
def fib2(n):
    if n <= 1:
        d[n] = n
    if n not in d:
        d[n] = fib2(n-1) + fib2(n-2)
    return d[n]

'''This is another memoized version with using local cache instead of global dictionary variable, therefore 
the fib3's cache would not be conflict with other variable names'''
def fib3(n, cache = None):
    if cache is None:
        cache = {0:0,1:1}
    if n not in cache:
        cache[n] = fib3(n-1,cache)+fib3(n-2,cache)
    return cache[n]

'''fib bottom up'''
def bottom_up(n):
    fib = {}
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1]+ fib[i-2]
    return fib[n]

'''if the trial # is greater 20, let's say 50. Then while fib still computing the number, the fib2 and fib3 
will be done. This is Dynamic Programming'''
# print(fib(20))
# print(fib2(100))
print(fib3(200))

# print(bottom_up(100))


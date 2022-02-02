

def multiply(m,n):
    if(n==1):
        return m
    return m + multiply(m,n-1)


print(multiply(5,4))





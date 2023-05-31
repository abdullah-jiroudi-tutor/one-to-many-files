def insertion_sort(arry):
    if (n := len(arry)) <=1:
        return
    for i in range(1,n):
        key = arry[i]
        j=i-1
        while j>=0 and key<arry[j]:
            arry[j+1]=arry[j]
            j=j-1
        arry[j+1]=key
    return arry

arr=[8,2,4,9,3,6]
print(insertion_sort(arr))


def printt(n):
    if n==10:
        return
    else:
        print(n)
        return printt(n+1)

printt(0)

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

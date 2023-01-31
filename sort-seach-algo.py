#binary search
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n- 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(ar,to_find):
    lo=0
    hi=len(ar)
    while hi-lo>1:
        mid=(hi+lo)//2
        if ar[mid]<to_find:
            lo=mid+1
        else:
            hi=mid
    if ar[lo]==to_find:
        print(f"we found the number {to_find} at the index {lo}")
    elif ar[hi]==to_find:
        print(f"we found the number {to_find} at the index {hi}")
    else:
        print("Not found")

x=[2,5,8,12,16,23,38,56,72,91]
y=[8,2,5,0,1,6,7]
binary_search(x,16)
print(bubble_sort(y))
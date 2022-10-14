
def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2 ## divide

        merge_sort(arr, l, m) ## conquer
        merge_sort(arr, m+1, r)

        merge(arr, l, m, r)  ## combine

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    
    L[n1] = float("inf")
    R[n2] = float("inf")



    i = 0
    j = 0

    for k in range(l, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1




## Input and Output
n = int(input())

l = []
for i in range(n):
    a = int(input())
    l.append(a)

print(l)
merge_sort(l, 0, len(l)-1)
print(l)
## find_max_sub

def find_maximum_cross(A, low, mid, high):
    left_sum = float("-inf")
    temp_sum = 0

    for i in range(low, mid+1)[::-1]:
        temp_sum += A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left_index = i


    right_sum = float("-inf")
    temp_sum = 0

    for j in range(mid+1, high+1):
        temp_sum = temp_sum + A[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right_index = j
    
    return (max_left_index, max_right_index, left_sum + right_sum)



def find_maximum_subarr(A, low, high):
    if low == high:
        return (low, high, A[low])

    else:
        mid = (low + high) // 2
        
        left_low, left_high, left_sum = find_maximum_subarr(A, low, mid)
        right_low, right_high, right_sum = find_maximum_subarr(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_maximum_cross(A, low, mid, high)

        if (left_sum >= right_sum) and (left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum) and (right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


## Input and Ooutput
n = int(input())

l = []
for i in range(n):
    a = int(input())
    l.append(a)

for i in find_maximum_subarr(l,0, len(l)-1):
    print(i)


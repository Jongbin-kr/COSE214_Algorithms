## input
n = int(input())

p = [0] * (n+1)

for i in range(1, n+1):
    p[i] = int(input())



## define function
def extended_bottom_up_cut_rod(p, n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    # r[0] = 0
    for j in range(1, n+1):  ## i = 1~n
        q = float("-inf")
        for i in range(1, j+1):
            if q < p[i] + r[j-i]:
                q = p[i] + r[j-i]
                s[j] = i
        r[j] = q
    
    return r, s

def print_cut_rod_solution(p, n):
    r, s = extended_bottom_up_cut_rod(p, n)
    print(r[n])
    while n > 0:
        print(s[n])
        n = n -s[n]



## output
print_cut_rod_solution(p, n)

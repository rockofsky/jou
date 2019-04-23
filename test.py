def je_prastevilo(n):
    if n == 2 or n == 3:
        return True
    elif n == 1:
        return False
    else:
        for i in range(2, round(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
k = 0
for i in range(1, 200):
    if je_prastevilo(i) == True:
        print(i)
        k += 1

print("k je " + str(k))
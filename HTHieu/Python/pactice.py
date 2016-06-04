##############
#B1:
def UCLN(a, b):
    if a == 0 or b == 0:
        return a + b
    else:
        return UCLN(b, a % b)


def bcnn(a, b):
    return a * b / UCLN(a, b)


a = int(input("nhap a: "))
b = int(input("nhap b: "))
print "uoc chung lon nhat: ", UCLN(a, b)
print "boi chung nho nhat: ", bcnn(a, b)

#######

#B2:
def doiso(a, b):
    n = stack()
    while (a != 0):
        n.append(a % b)
        a = a / b
    while (len(n) > 0):
        print n.pop()


a = int(input("nhap a: "))
b = int(input("nhap b: "))
doiso(a, b)

##########
#B3
from inspect import stack


def tong(a):
    n = stack()
    arr = []
    b = 0
    i = 0
    while (a != 0):
        arr.append(a % 10)
        a = a / 10
        i = i + 1
    for j in range(len(arr)):
        b += arr[j]
    return b


print tong(99)


#########
#B4:
def phantich(n):
    i = 2
    arr = []
    while (i <= n):
        if n % i == 0:
            print i
            n /= i
        else:
            i = i + 1


phantich(20)

#########
#B5+6:
import math


def snt(n):
    i = 2
    a = True
    while (i <= math.sqrt(n)):
        if n % i == 0:
            a = False
            break
        else:
            i = i + 1
    return a


def timsnt(n):
    if n == 1:
        print "la snt"
    else:
        for i in range(n):
            if snt(i) == True:
                print i
            else:
                i += 1


timsnt(100)


##################
#B7
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print fibo(10)


#################



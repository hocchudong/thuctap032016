# ##############
# def UCLN(a, b):
#     if a == 0 or b == 0:
#         return a + b
#     else:
#         return UCLN(b, a % b)
#
#
# def bcnn(a, b):
#     return a * b / UCLN(a, b)
#
#
# a = int(input("nhap a: "))
# b = int(input("nhap b: "))
# print "uoc chung lon nhat: ", UCLN(a, b)
# print "boi chung nho nhat: ", bcnn(a, b)
#
# #######
#
#
# def doiso(a, b):
#     n = stack()
#     while (a != 0):
#         n.append(a % b)
#         a = a / b
#     while (len(n) > 0):
#         print n.pop()
#
#
# a = int(input("nhap a: "))
# b = int(input("nhap b: "))
# doiso(a, b)
#
# ##########
# from inspect import stack
#
#
# def tong(a):
#     n = stack()
#     arr = []
#     b = 0
#     i = 0
#     while (a != 0):
#         arr.append(a % 10)
#         a = a / 10
#         i = i + 1
#     for j in range(len(arr)):
#         b += arr[j]
#     return b
#
#
# print tong(99)
#
#
# #########
#
# def phantich(n):
#     i = 2
#     arr = []
#     while (i <= n):
#         if n % i == 0:
#             print i
#             n /= i
#         else:
#             i = i + 1
#
#
# phantich(20)
#
# #########
# import math
#
#
# def snt(n):
#     i = 2
#     a = True
#     while (i <= math.sqrt(n)):
#         if n % i == 0:
#             a = False
#             break
#         else:
#             i = i + 1
#     return a
#
#
# def timsnt(n):
#     if n == 1:
#         print "la snt"
#     else:
#         for i in range(n):
#             if snt(i) == True:
#                 print i
#             else:
#                 i += 1
#
#
# timsnt(100)
#
#
# ##################
#
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)
#
#
# print fibo(10)
#
#
# #################
# B8
# def sotn(n):
#     arr = []
#     b = []
#     while (n > 0):
#         arr.append(n % 10)
#         b.append(n % 10)
#         n /= 10
#     arr.reverse()
#     if arr == b:
#         return True
#     else:
#         return False
#
#
# i = 100000
# for i in range(999999):
#     if sotn(i) == True: print i


#######################
# B9
# def nextstr(n):
#     i = n
#     arr = []
#     sum = 0
#     for j in range(0, n):
#         arr.append(0)
#     while (i >= 0):
#         for j in range(n):
#             print arr[j]
#         print "\n"
#         i = n - 1
#         while (i >= 0) and (arr[i] == 1):
#             arr[i] = 0
#             i = i - 1
#         arr[i] = 1
#         for k in range(0, n):
#             sum += arr[k]
#
#
# n = int(input("nhap n: "))
# nextstr(n)
############
# B10

# def nextCombine():
#     stop = 0
#     while stop == 0:
#         for i in range(len(arr)):
#             print arr[i]
#         print "\n"
#         i = k - 1
#         while (i > 0 and arr[i] == n - k + i):
#             i = i - 1
#         if i > 0:
#             arr[i] = arr[i] + 1
#             for j in range(i + 1, k):
#                 arr[j] = arr[i] + j - i
#         else:
#             stop = 1
#
#
# if __name__ == '__main__':
#     n = int(input("nhap n: "))
#     k = int(input("nhap k: "))
#     arr = []
#     for i in range(0,k):
#         arr.append(i)
#     nextCombine()
# Chua chay on
##############################
# # B11
# def nextCombine():
#     i = n - 2
#     while i > 0:
#         print arr
#         while i > 0 and arr[i] > arr[i + 1]:
#             i -= 1
#         if i > 0:
#             k = n - 1
#             while arr[i] > arr[k]:
#                 k -= 1
#             (arr[i], arr[k]) = (arr[k], arr[i])
#             r = n - 2
#             s = i + 1
#             while r > s:
#                 (arr[r], arr[s]) = (arr[s], arr[r])
#                 r = r -1
#                 s = s + 1
#
#
# if __name__ == '__main__':
#     n = int(input("nhap n: "))
#     arr = []
#     for i in range(0, n):
#         arr.append(input("nhap "))
#     nextCombine()
####################
#B14
# import collections
# if __name__ == '__main__':
#     arr=[]
#    # n=int(input("nhap do dai: "))# dung distribution counting
#     s=raw_input("nhap xau: ")
#     print collections.Counter(s)
####################
#B15
import collections
if __name__ == '__main__':
    s="hoang trung hieu"
    freqs = {}
    for i in range(len(s)):
        freqs[s[i]]+=1
    print freqs
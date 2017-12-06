'''a program to calculate the statistical function for the project'''

import math
import statistics
#import turtle

def calc_uk(some_list,k):
    # calculates the statistics Mann-Whitney of the list given using indicator
    count = 0
    n_len = len(some_list)
    for i in range(0,k): #array starts at [0] so i need to give it the right pointer
        for j in range(k,n_len):
            if some_list[i]<=some_list[j]:
                count = count + 1
    return count


def calc_mk(some_list):
    # calculates the number MK using statistic Mann-Whitney for each k in the list
    n_len = len(some_list)
    mk = 0
    for i in range(1,n_len):
        u_kn = calc_uk(some_list, i) #array starts at [0] so i need to give it the right pointer
        mk = mk + (u_kn-(i*(n_len-i))/2)
    return mk


def calc_md(some_list):
    n_len = len(some_list)
    md = 0
    for i in range(1,n_len):
        u_kn = calc_uk(some_list,i) #array starts at [0] so i need to give it the right pointer
        upper = u_kn - i*(n_len-i)/2
        bottom = (i*(n_len-i)*(n_len+1))/12
        md = md + (upper/(math.sqrt(bottom)))
    return md


def s1_n(some_list):
    n_len = len(some_list)
    one = 0
    for i in range(1,n_len):
        one = one + i*(n_len-i)
    two = 0
    for j in range(1,n_len):
        for r in range(1,n_len-j+1): #array starts at [0] so i need to give it the right pointer (n-k is included here)
            two = two + j*(n_len-j-r)
    num = ((n_len+1)/12)*(one + 2*two)
    s1_n = math.sqrt(num)
    return s1_n


def s2_n(some_list):
    n_len = len(some_list)
    one = 0
    for i in range(1,n_len):
        for r in range(1,n_len-i+1): #array starts at [0] so i need to give it the right pointer (n-k is included here)
            sq = (i*(n_len-i-r))/((n_len-i)*(i+r))
            one = one + math.sqrt(sq)
    num = (n_len-1) + 2*one
    s2_n = math.sqrt(num)
    return s2_n


list_s = [18.35,19.54,19.5,19.62,21.52,21.48,20.38,21.15,20.29,19.98,19.71,19.81,20.77,20.84,21.09,
        19.74,21.13,19.43,19.77,19.81,20.81,21.35,18.79,19.43,22.12,21.43,19.73,21.34,20.15,20.79,
        21.42,20.56,22.23,21.05,22.07,22.31,20.73,21.93,20.73,23.97,21.62,21.67,21.95,23.78,20.87,21.76]

mk = calc_mk(list_s)
s1_n = s1_n(list_s)
print (mk)
print(s1_n)
print(mk/s1_n)

md = calc_md(list_s)
s2_n = s2_n(list_s)
print(md)
print(s2_n)
print (md/s2_n)

'''mu = statistics.mean(list_s)
stdv = statistics.stdev(list_s)
print(mu)
print(stdv)'''
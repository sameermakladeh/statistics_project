'''a program to calculate the statistical function for the project'''

import math
#import statistics
#import numpy as np
#import turtle
import pandas

# Import data from excel and show it (using pandas module)
df = pandas.read_excel('data.xlsx')
col_names = df.columns
col_data = df.values
#print (col_names[1])
#print (col_data[:,1])
#values = df['Year'].values
#FORMAT = ['Year','Mean','Min','Max']
#df_selected = df[FORMAT]


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
    s1_n = float(math.sqrt(num))
    return s1_n


def s2_n(some_list):
    n_len = len(some_list)
    one = 0
    for i in range(1,n_len):
        for r in range(1,n_len-i+1): #array starts at [0] so i need to give it the right pointer (n-k is included here)
            sq = (i*(n_len-i-r))/((n_len-i)*(i+r))
            one = one + math.sqrt(sq)
    num = (n_len-1) + 2*one
    s2_n = float(math.sqrt(num))
    return s2_n


def main(j):
    global col_data, col_names
    for i in range(1,j):
#calc for 1 (mk)
        t_list = col_data[:,i]
        mk_call = calc_mk(t_list)
        s1_n_call = s1_n(t_list)
        print("ratio_1 for ",col_names[i], " = ", mk_call/s1_n_call)
        #print("ratio_1 for mk", col_names[i], " = ", mk_call)
        #print("ratio_1 for s1", col_names[i], " = ", s1_n_call)
#calc for 2 (md)
        md_call = calc_md(t_list)
        s2_n_call = s2_n(t_list)
        print("ratio_2 for ",col_names[i], " = ", md_call/s2_n_call)
        #print("ratio_1 for mk", col_names[i], " = ", md_call)
        #print("ratio_1 for s1", col_names[i], " = ", s2_n_call)


main(4)



'''mu = statistics.mean(list_s)
stdv = statistics.stdev(list_s)
print(mu)
print(stdv)'''
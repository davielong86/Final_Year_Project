# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:30:22 2018

@author: david
"""


import random
 
f_to_split = "Merged_Data.csv"
 
ltotal = len(open(f_to_split, 'rb').read().split('\n'))
lim_75 = int(ltotal * .75)
if lim_75 < 1: lim_75=1
lim_25 = int(ltotal * .25)
if lim_25 < 1: lim_25=1
lim_75_count = 0
lim_25_count = 0
 
fin = open(f_to_split, 'rb')
f75out = open("data/trainingSet.txt", 'wb')
f25out = open("data/testingSet.txt", 'wb')
for line in fin:
    r = random.random()
    if r < 0.75 and lim_75_count < lim_75 or r >= 0.75 and lim_25_count > lim_25:
        lim_75_count += 1
        f75out.write(line)
    else:
        lim_25_count += 1
        f25out.write(line)
fin.close()
f75out.close()
f25out.close()
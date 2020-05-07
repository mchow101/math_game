# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:05:36 2020

@author: Mitali
"""
import time, random

upper_lim = 10
num_qs = 10
score = 0
start = 0
first = True

for i in range(num_qs):
    a = random.randint(0, upper_lim)
    b = random.randint(0, upper_lim)
    problem = (str(a) + " + " + str(b) + " = ")
    ans = int(input(problem))
    if first:
        start = time.time()
        first = False
    if ans == (a + b):
        print ("Correct!")
        score += 1
    else:
        print ("Incorrect. The correct answer is", a + b)
        score -= 1

elapsed = time.time() - start
print ("You scored", score, "points.")
print ("You took", elapsed, " seconds.")
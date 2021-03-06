# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:05:36 2020

@author: Mitali
"""
import time, random
import sqlite3

upper_lim = 10
num_qs = 1
score = 0
start = 0
first = True

for i in range(num_qs):
    a = random.randint(0, upper_lim)
    b = random.randint(0, upper_lim)
    problem = (str(a) + " * " + str(b) + " = ")
    ans = int(input(problem))
    if first:
        start = time.time()
        first = False
    if ans == (a * b):
        print ("Correct!")
        score += 1
    else:
        print ("Incorrect. The correct answer is", a * b)
        score -= 1

elapsed = time.time() - start
print ("You scored", score, "points.")
print ("You took", elapsed, "seconds.")

dbFile = 'data.db'
senConn = sqlite3.connect(dbFile)
senConn.row_factory = sqlite3.Row
senCur = senConn.cursor()

#senCur.execute("DROP table senTable")
#createStr  = "CREATE table senTable (date string, time real, score real, level string)"
#senCur.execute(createStr)

insertStr = "INSERT into senTable VALUES("
insertStr += "'" + time.asctime()[:10] + "', " + str(elapsed) + ', ' + str(score) + ", 'mult" + str(upper_lim) + "')"
senCur.execute(insertStr)
senCur.execute("SELECT *  FROM senTable WHERE date='" + time.asctime()[:10] + "';")
data = senCur.fetchall()
s = 0
t = 0
for x in data:
    t += x[1]
    s += x[2]
    
print ("Total score today:", int(s), "points")    
print ("Total time today:", t, "seconds")
senConn.commit()
senConn.close()
################################################
# Simple Monte Carlo Method for Calculating Pi #
################################################

import atexit
from time import clock, time
from datetime import timedelta
from random import *
from math import pow, sqrt, pi

#def secondsToStr(t):
#	return "%d:%02d:%02d.%03d" % \
#		reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
#			[(t*1000,),1000,60,60])

def secondsToStr(t):
	return str(timedelta(seconds=t))

line = "="*50
def log(s, elapsed=None):
	#print line
	#print secondsToStr(time()), '-', s
	#print s
	if elapsed:
		print "Running time:", elapsed
		print line
		print

def endlog():
	end = time()
	elapsed = end-start
	log("End Program", secondsToStr(elapsed))

def now():
	return secondsToStr(time())

start = time()
atexit.register(endlog)
log("Start Program")

###### Max number of iterations set below ######
hits=0.0
iterations=1000000

for i in range(0,iterations):
	x=random()
	y=random()
	
	distance = sqrt(pow(x,2) + pow(y, 2))
	
	if distance <= 1:
		currentPi = 4 * (hits / iterations)
		print currentPi
		#print 'Current estimation: %.10f' %currentPi
		hits = hits + 1
	
	#if sqrt(x*x+y*y)<=1:
	#	print 4*hits/n
	#	inside+=1

montePi= currentPi
print line
print "With %i points:\n" % iterations
print "Monte Carlo approximation for pi: %.10f \n" %montePi
print "Actual value for pi: %.10f \n" %pi


#import time
#start = time.time()
#start = clock()
#log("Start Program")
#print('Running Time: %.4f seconds' % (time.time() - start))
#print(time.time())

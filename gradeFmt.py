#!/usr/bin/env python

import sys

bars = 15

def isNum(word):
	try:
		int(word)
		return True
	except:
		return False

def remDot(fname):
	loc = fname.rfind('.')
	if loc == -1:
		return fname
	return fname[:loc]

def cnt(lst,a,b):
	total = 0
	for x in xrange(a,b+1):
		# print x, lst.count(x)
		total += lst.count(x)
	return total

def mean(seat):
	tote = 0 
	for memb in seat:
		tote += float(memb)
	return tote / float(len(seat))

def intPart(strng):
	ans = 0
	real = False
	for let in strng:
		if isNum(let):
			real = True
			ans*=10
			ans+=int(let)

	if not real:
		return -1
	return ans

def dispRange(a,b):
	if a==b:
		return str(a)
	return str(a)+'-'+str(b)

def main():
	if len(sys.argv) > 1:
		inname = sys.argv[1]
		outname = remDot(inname)+'.tab'
	else:
		quit('Please specify .csv file to process.')

	outFile = open(outname,'wb')
	inFile = open(inname,'rb')

	fileContents = inFile.read().splitlines()
	inFile.close()

	lines, students = 0,0
	scores = []

	for line in fileContents:
		lines+=1
		data = line.split(',')
		toCheck = []
		for datum in data:
			if isNum(datum) or (intPart(datum) != -1 and intPart(datum)>=999):	
				toCheck.append(intPart(datum))

		toCheck.sort()
		toCheck.reverse()

		if len(toCheck)>=2:
			students+=1
			uid, grade = toCheck[0],toCheck[1]
			# print uid, grade
			if grade > 0 and uid > 999:
				outFile.write(str(uid)+'\t\t'+str(grade)+'\t\n')
				scores.append(grade)

	outFile.close()

	minS,maxS = min(scores),max(scores)
	meanS = mean(scores)

	print '%d line read. %d students found.' % (lines, students)
	print 'Output written to '+outname

	print '\nStats:'
	print 'Min: %d\tMax: %d\tMean: %.2f\t' % (minS,maxS,meanS)
	print ''

	step = (maxS-minS)/bars
	step = max([step, 1])

	for x in xrange(minS,maxS+1,step):
		print dispRange(x,x+step-1)+'\t'+ '+'* cnt(scores,x,x+step-1)


main()

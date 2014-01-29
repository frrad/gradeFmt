#!/usr/bin/env python

import sys

bars = 15       # number of bars in summary histogram
minUID = 999    # value of smallest UID considered as int
UIDlength = 9   # number of digits to zero-pad UID
epsilon = .001  # Used for float-int comparison

def isNum(word):
    try:
        float(word)
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
    for pod in lst:
        if pod <= b+1 and pod >=a:
            total += 1
    return total

def mean(seat):
    tote = 0 
    for memb in seat:
        tote += float(memb)
    return tote / float(len(seat))

# remove extraneous markup from numbers (i.e. UIDs)
def sanitize(strang):
    ans = ""
    for let in strang:
        if isNum(let) or let == ".":
            ans =  ans + let
    # print "sanitized", strang, "to", ans #debug
    return ans

def numbify(str):
    f = float(str)
    i = int(f)
    if abs(f - i) < epsilon:
        return i
    return f

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
            clean = sanitize(datum)
            if isNum(clean):
                toCheck.append(numbify(clean))

        toCheck.sort()
        toCheck.reverse()

        if len(toCheck)>=2:
            uid, grade = toCheck[0],toCheck[1]
            if uid > minUID:
                students+=1
                UIDstr = str(uid).zfill(UIDlength)
                # print UIDstr, "\t", grade, "\t<=\t", line #debug
                if grade > 0:
                    outFile.write(UIDstr+'\t\t'+str(grade)+'\t\n')
                    scores.append(grade)

    outFile.close()

    minS,maxS = int(min(scores)),max(scores)
    meanS = mean(scores)

    print '%d line read. %d students found.' % (lines, students)
    print 'Output written to '+outname

    print '\nStats:'
    print 'Min: %d\tMax: %d\tMean: %.2f\t' % (minS,maxS,meanS)
    print ''

    minRound = int(minS)
    if abs(maxS - float(int( maxS)) )< epsilon:
        maxRound = int(maxS)
    else:
        maxRound = int(maxS)+1


    step = (maxRound-minRound)/bars
    step = max([step, 1])

    for x in xrange(minRound,maxRound+1,step):
        print dispRange(x,x+step-1)+'\t'+ '+'* cnt(scores,x,x+step-1)


main()

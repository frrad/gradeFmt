import sys

outname = 'proc.tab'

def isNum(word):
	try:
		int(word)
		return True
	except:
		return False

def main():
	inname = 'grades.csv'

	if len(sys.argv) > 1:
		inname = sys.argv[1]

	outFile = open(outname, 'wb')
	inFile = open(inname,"rb")

	fileContents = inFile.read().splitlines()
	inFile.close()

	lines, students = 0,0
	scores = []

	for line in fileContents:
		lines+=1
		data = line.split(",")
		toCheck = []
		for datum in data:
			if isNum(datum):	
				toCheck.append(int(datum))
		
		toCheck.sort()
		toCheck.reverse()

		if len(toCheck)>=2:
			students+=1
			uid, grade = toCheck[0],toCheck[1]
			# print uid, grade
			outFile.write(str(uid)+'\t\t'+str(grade)+'\t\n')
			scores.append(grade)

	outFile.close()

	print '%d line read. %d students found.' % (lines, students)
	print 'Output written to '+outname
	print scores

main()
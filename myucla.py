outname = 'proc.tab'
inname = 'grades.csv'

def isNum(word):
	try:
		int(word)
		return True
	except:
		return False


def main():
	
	outFile = open(outname, 'wb')
	inFile = open(inname,"rb")

	fileContents = inFile.read().splitlines()
	inFile.close()

	for line in fileContents:
		data = line.split(",")
		uid = -1
		grade = -1
		for datum in data:
			if isNum(datum):	
				dat = int(datum)
				if dat > 500:
					uid = dat	
				if dat < 500:
					grade = dat
		print uid, grade
		if uid > -1 and grade > -1:
			outFile.write(str(uid)+'\t\t'+str(grade)+'\t\n')

		
	outFile.close()



main()

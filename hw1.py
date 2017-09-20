## Kristina Kolibab
## Homework 1

#iPython let's you test out code, just a neat tip I didn't know

import numpy as np

# Correctly reads in the training set based on it's formatting
def readTrainingFile( file ):
	
	f = open(file, "r")
	trainList = []
	trueAnswer = []
	for line in f:
		trainList.append(line.split(' ')[0:-2]) # read in each point 
		trueAnswer.append(line.split(' ')[-2]) # read in each 'Y'/'N' answer
	f.close()
	trainList = np.array(trainList, dtype = float) # convert to numpy array
	trainList = trainList/np.linalg.norm(trainList)
	np.array(trueAnswer) 
	return trueAnswer, trainList

# Correctly reads in the training set based on it's formatting
def readTestFile( file ):
	
	f = open(file, "r")
	vecTesters = []
	for line in f:
		vecTesters.append(line.split(' ')[0:-1])
	f.close()
	vecTesters = np.array(vecTesters, dtype = float)
	vecTesters = vecTesters/np.linalg.norm(vecTesters)
	return vecTesters

# Converts my binary to ascii character
def bin_ascii( str ):
	int(str, 2)
	str = chr(int(str, 2))
	return str

# Classifier function to figure out my weight 'w' 
def classifier():
	
        # Initial stuff that does not get repeated
        trueAnswer, trainList = readTrainingFile("train.txt") # fetching vectors
        w = np.zeros(1024) # initially set weight to 0, w should only be of 1024, a LINE
	Error = True
        errorCounter = 0
	i = 0
        # Repeats until Error = false, meaning the training set effectively trained w
        while i != len(trainList) :
		Error = False
            	errorCounter += 1 
	   	for row in trainList: 
                	if np.dot(w, row) >= 0 and trueAnswer[i] != 'Y': # y = +1, guess value is 1
                		Error = True
				i = 0
				w = np.add(-1*row, w)
				break
                	elif np.dot(w, row) < 0 and trueAnswer[i] != 'N': # y = -1, guess value is 0
	            		Error = True			
				i = 0
				w = np.add(1*row, w)
				break
			else: 
				i += 1
				
	print "Iterations: ", errorCounter
        # Done training, time to test
	vecTesters = readTestFile("test.txt")		
	binaryS = ''
	for row in vecTesters:
		if np.dot(w, row) >= 0:
			binaryS = binaryS + '1'		
		elif np.dot(w, row) < 0:
			binaryS = binaryS + '0'
	print "Binary: ", binaryS
	print "ASCII Char: ", bin_ascii(binaryS)

# M A I N
def main():
	classifier()

if __name__ == "__main__":
    main()
    





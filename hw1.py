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
	return trueAnswer, trainList

# Correctly reads in the training set based on it's formatting
def readTestFile( file ):
	
	f = open(file, "r")
	vecTesters = []
	for line in f:
		vecTesters.append(line)
	return vecTesters

# Classifier function to figure out my weight 'w' 
def classifier():

        # Initial stuff that does not get repeated
        trueAnswer = []
        trainList = []
        trueAnswer, trainList = readTrainingFile("train.txt") # fetching vectors
#        print "trainList: ", trainList
        w = np.zeros((792, 1024)) # initially set weight to 0
#        print "w: ", w
        Error = True
        errorCounter = 0
        # Repeats until Error = false, meaning the training set effectively trained w
        while Error == True:
            print "-----------------TIME THROUGH: ", errorCounter
            errorCounter += 1
            Error = False
        
#            guess = np.zeros((792, 1024))
            guess = np.dot(w, trainList)
            # compare trueAnswer(yHat) with guess(value)  
            for (i, value) in enumerate(guess):
                yHat = trueAnswer[i] # only one answer per row i
                updateW = 0
                if value >= 0: # y = +1, guess value is 1
                    sign = 1
                    if yHat != 'Y': # guess not truly above the line 
                        updateW = 1
                elif value < 0: # y = -1, guess value is 0
                    sign = -1
                    if yHat != 'N': # guess not truly below the line
                        updateW = 0
              
                if updateW == 1:
                    print "Incorrect Guess"
                    print "w before: ", w
                    Error = True
                    np.add(np.dot(trainList, sign), w)
                    print "w after: ", w
                elif updateW == 0:
                    print "Correct Guess"

            # Done training, time to test
            print "Weight has been correctly trained, now to test!"
            vecTesters = []
            vecTesters = readTestFile("test.txt")
            ansVec = []
            ansVec = np.dot(w, vecTesters)

            for AnsValue in ansVec: 
                if AnsValue >= 0:
                    binary = 1
                    print "binary: ", binary
                elif AnsValue < 0:
                    binary = 0
                    print "binary: ", binary
                binaryVec.append(binary) # 8 total
        
        # print ansVec    
        # call a hex function, ascii char 

# M A I N
def main():

    classifier()

if __name__ == "__main__":
    main()
    





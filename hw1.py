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
	i = 0
	while i < len(vecTesters):
		print vecTesters[i]	
		i += 1
	return vecTesters

# Classifier function to figure out my weight 'w' 
def classifier():

        trueAnswer = []
        trainList = []
        trueAnswer, trainList = readTrainingFile("train.txt") # fetching vectors

        # readTestFile("test.txt")
        w = np.zeros((792, 1024)) # initially set weight to 0
        a = 0 
        
        for (i, row) in enumerate(w): # each row for w
            training_row = trainList[a] # each row for training 
            b = 0  
            yGuess = 0 
            for (j, value) in enumerate(row): # each value for w
                val = training_row[b] 
                b += 1
                yGuess += value*int(float(val)) # (j*val) + (j*val) + (j*val)...    
                      
            # compare trueAnswer with yGuess  
            yHat = trueAnswer[a]
            a += 1
            updateW = 0
            if yGuess >= 0: # y = +1
                sign = 1
                if yHat != 'Y': # guess not truly above the line 
                    updateW = 1
            elif yGuess < 0: # y = -1
                sign = -1
                if yHate != 'N': # guess not truly below the line
                    updateW = 1
            
            # iterate to update w if incorrect guess
            if updateW == 1:
                print "Incorrect Guess"
                a_ = 0
                x_ = 0
                fixedWeight = np.zeros((792,1024)) # taking w's place for now
                for (i_, row_) in enumerate(w):
                    training_r = trainList[a_]
                    fixed_row = fixedWeight[x_]
                    a_ += 1
                    b_ = 0
                    y_ = 0
                    for (j_, value_) in enumerate(row_):
                        val_ = training_r[b_]
                        b_ += 1
                        fixed_row[y_] += value_ + sign * int(float(val_)) 
                        y_ += 1
                    fixedWeight[x_] = fixed_row
                    x_ += 1
                # Update w
                w = fixedWeight
            elif updateW == 0:
                print "Correct Guess"

            # go through this forloop until you aren't guessing wrongly --> what does this mean though??
classifier()







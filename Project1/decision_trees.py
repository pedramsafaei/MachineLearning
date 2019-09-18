import numpy as np 
import math 
import operator

# BEGIN inputing first set of data 
X_Training1 = np.array( [ [0,1],
                          [0,0],
                          [1,0],
                          [0,0],
                          [1,1] ] )

Y_Training1 = np.array( [ [1],
                          [0],
                          [0],
                          [0],
                          [1] ] )

X_Validation1 = np.array( [ [0,0],
                            [0,1],
                            [1,0],
                            [1,1] ] )

Y_Validation1 = np.array( [ [0],
                            [1],
                            [0],
                            [1] ] )

X_Testing1 = np.array( [ [0,0],
                         [0,1],
                         [1,0],
                         [1,1] ] )

Y_Testing1 = np.array( [ [1],
                         [1],
                         [0],
                         [1] ] )
# END inputing first set of data 

# BEGIN inputing 2nd set of data 
X_Training2 = np.array( [ [0, 1, 0, 0],
                          [0, 0, 0, 1],
                          [1, 0, 0, 0], 
                          [0, 0, 1, 1], 
                          [1, 1, 0, 1],
                          [1, 1, 0, 0], 
                          [1, 0, 0, 1], 
                          [0, 1, 0, 1], 
                          [0, 1, 0, 0] ] )

Y_Training2 = np.array( [ [0], 
                          [1], 
                          [0], 
                          [0], 
                          [1], 
                          [0], 
                          [1], 
                          [1], 
                          [1] ] )


X_Validation2 = np.array( [ [1, 0, 0, 0], 
                            [0, 0, 1, 1], 
                            [1, 1, 0, 1],
                            [1, 1, 0, 0], 
                            [1, 0, 0, 1], 
                            [0, 1, 0, 0] ] )

Y_Validation2 = np.array( [ [0], 
                            [0], 
                            [1], 
                            [0], 
                            [1], 
                            [1] ] )


X_Testing2 = np.array( [ [0, 1, 0, 0], 
                         [0, 0, 0, 1], 
                         [1, 0, 0, 0], 
                         [0, 0, 1, 1], 
                         [1, 1, 0, 1],
                         [1, 1, 0, 0], 
                         [1, 0, 0, 1], 
                         [0, 1, 0, 1], 
                         [0, 1, 0, 0] ] )

Y_Testing2 = np.array( [ [1], 
                         [1], 
                         [0], 
                         [0], 
                         [1], 
                         [0], 
                         [1], 
                         [1], 
                         [1] ] )
# END inputing 2nd set of data 



# BEGIN Data for generating the decision tree (last part of the project)
X_real = np.array( [ [4.8, 3.4, 1.9, 0.2], 
                     [5.0, 3.0, 1.6, 1.2], 
                     [5.0, 3.4, 1.6, 0.2],
                     [5.2, 3.5, 1.5, 0.2], 
                     [5.2, 3.4, 1.4, 0.2], 
                     [4.7, 3.2, 1.6, 0.2],
                     [4.8, 3.1, 1.6, 0.2], 
                     [5.4, 3.4, 1.5, 0.4], 
                     [7.0, 3.2, 4.7, 1.4],
                     [6.4, 3.2, 4.7, 1.5], 
                     [6.9, 3.1, 4.9, 1.5], 
                     [5.5, 2.3, 4.0, 1.3],
                     [6.5, 2.8, 4.6, 1.5], 
                     [5.7, 2.8, 4.5, 1.3], 
                     [6.3, 3.3, 4.7, 1.6],
                     [4.9, 2.4, 3.3, 1.0] ] )

Y_real = np.array( [ [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1],
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0] ] )
# END Data for generating the decision tree (last part of the project)

"""
def DT_train_binary(X,Y,max_depth):
    currentDepth = 0
    if max_depth < 0 :
        max_depth = min (len(X[0]), len(X) - 1)
    featuresList = []
    decisionTree = findBestTree(X,Y,max_depth,featuresList,currentDepth)
    return decisionTree
"""
'''
def DT_test_binary(X,Y,DT):

def DT_train_binary_best(X_train, Y_train, X_val, Y_val):

def DT_train_real(X,Y,max_depth):

def DT_test_real(X,Y,DT):

def DT_train_real_best(X_train,Y_train,X_val,Y_val):
'''
"""
def entropy(Set):
    # count the number of yes or true
    Positive = np.sum(Set)
    # get the size of the training data 
    Size = np.size(Set)
    # number of negatives or no
    Negative = Size - Positive
    # calculate entropy of the set 
    Entropy = -(Negative/Size) * math.log2(Negative/Size) - (Positive/Size) * math.log2(Positive/Size)
    return Entropy

def informationGain(left, right, label):
    # find the entropy of the whole set 
    entireTrainingEntropy = entropy(label)
    entireSize = np.sign(label)
    # find the entropy of NO
    leftEntropy = entropy(left)
    leftSplitSize = np.size(left)
    #find the Entropy of YES
    rightEntropy = entropy(right)
    rightSplitSize = np.size(right)
    # find the information gain of that split
    infoGain = entireTrainingEntropy - (((leftSplitSize/entireSize)*(leftEntropy) ) + ((rightSplitSize/entireSize)*(rightEntropy)))
   
    return infoGain
"""

def splitData(X, direction, value):
    results = []
    for i in X:
        if i[direction] == value:
            split = i[:direction].tolist()
            split.extend(i[direction+1:])
            results.append(split)
    return results

def Entropy(dataSet):
	numEntires = len(dataSet)						
	labelCounts = {}								
	for featVec in dataSet:							
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():	
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1				
	entropy = 0.0								
	for key in labelCounts:							
		prob = float(labelCounts[key]) / numEntires	
		entropy -= prob * math.log(prob, 2)		
	return entropy	

def BestSplit(X):
	numFeatures = len(X[0]) - 1				
	baseEntropy = Entropy(X) 			
	bestInfoGain = 0.0  								
	bestFeature = -1								
	for i in range(numFeatures): 						
		featList = [example[i] for example in X]
		uniqueVals = set(featList)     				
		newEntropy = 0.0  								
		for value in uniqueVals: 						
			subDataSet = splitData(X, i, value) 		
			prob = len(subDataSet) / float(len(X))   		
			newEntropy += prob * Entropy(subDataSet) 	
		infoGain = baseEntropy - newEntropy 						
		if (infoGain > bestInfoGain): 							
			bestInfoGain = infoGain 							
			bestFeature = i 									
	return bestFeature 			

def numOccurrances(classList):
	classCount = {}
	for vote in classList:										
		if vote not in classCount.keys():classCount[vote] = 0	
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)		
	return sortedClassCount[0][0]							
		
# def findBestTree(X,Y,max_depth,featuresList,currentDepth):

def main():
	print(Entropy(X_Training1))
	print(BestSplit(X_Training2)) # returns index value of feature with largest IG
if __name__ == "__main__":
	main()


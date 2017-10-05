import numpy as np

def mapper(rowNo, value):
    result = {} #Creation of a dictionary to return values

    for columnNo in range(0, len(value)): #Go through the values
        k = columnNo #Create an integer taking the key of the value
        result[k] = {rowNo: value[columnNo]} #Add a string with "rowNumber: valueColumn" to the dictionnary at the index k
    return(result) #Return the dictionnary

def reducer(key, value):
    transposeValue = [] #Creation of a new array
    for x in range(0, len(value)): #Go through the different values of value
        for val in value[key]:  #Get the value for this key received as argument
            val = val.split(':')  #Split val to get the num of the line and the value separately
            transposeValue.append(val[1])  #Add the value to the new array

        newDict = {} #Create a new dictionnary
        newDict[key] = transposeValue  #Add the array to the dictionnary at the index of the key
    return newDict  #Return this dictionnary

#Main

tab = np.array([['a','z','y','x'],['b','c','d','e'],['f','g','h','i'],['j','k','l','m']]) #Creation of a 4x4 matrice
result_reducer = {}

#Mapper phase
for i in range(0, len(tab)): #Go through the matrice row by row
    result_mapper = mapper(i, tab[i,]) #Call of the mapper for each row

###################################
#Sort & Shuffle phase
###################################

#Reducer phase
tab_reduce0 = {0:[{0:'a'},{1:'b'},{2:'f'},{3:'j'}]}
tab_reduce1 = {1:[{0:'z'},{1:'c'},{2:'g'},{3:'k'}]}
tab_reduce2 = {2:[{0:'y'},{1:'d'},{2:'h'},{3:'l'}]}
tab_reduce3 = {3:[{0:'x'},{1:'e'},{2:'i'},{3:'m'}]}

#Calls of the reducer function
result_reducer0 = reducer(0, tab_reduce0[0])
result_reducer1 = reducer(1, tab_reduce1[1])
result_reducer2 = reducer(2, tab_reduce2[2])
result_reducer3 = reducer(3, tab_reduce3[3])


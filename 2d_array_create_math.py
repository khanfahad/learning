import numpy
arraySize = input("size of 2D array 'N M'").split()
N = int(arraySize[0])
M = int(arraySize[1])
myArray = []
for i in range(0,N):
    x = input("enter values separated by spaces: ").split()
    x = [int(i) for i in x]
    myArray.append(x)
my_array = numpy.array(myArray)

numpy.set_printoptions(legacy='1.13')
print("mean: ", numpy.mean(my_array, axis = 1))
print("variance: ", numpy.var(my_array, axis = 0))
print("standard deviation: ", numpy.std(my_array, axis = None))

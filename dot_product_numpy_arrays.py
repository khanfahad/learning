import numpy
arraySize = int(input())
a = numpy.array([input().split() for i in range(arraySize)],int)
b = numpy.array([input().split() for j in range(arraySize)],int)
m = numpy.dot(a,b)
print(m)

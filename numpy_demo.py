#NumPy stands for numerical python.
#It is a library in python used for working with arrays.
#It also has functions for working in domain of linear algebra, fourier transform, and matrices
'''
import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)
print(type(arr))
'''

'''
a=[1,2,3,4,5]
b=[5,6,7,8,9,10]

c=[]
for i in range(len(a)): #initial value will be considered as 0
    c.append(a[i]+b[i])
print(c)
print(type(c))
'''

'''
#wap to add 2 numpy arrays
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([5,6,7,8,9])   

c=a+b
print(c)
print(type(c))
'''

'''
wap to perform mathematical operations ny using numpy
import nuhmpy as np

arr=np.array([1,2,3,4])
print(arr+10)
print(arr*2)
'''

'''
wap a program to find the sum of all marks
import numpy as np

marks=np.array([69,24,39,49])
sum1=np.sum(marks)
print(sum1)
print(np.sum(marks))
print(np.mean(marks))

'''

'''
wap to find the maximum and minimum marks
import numpy as np
marks=np.array([69,24,39,49])
print(np.max(marks))
print(np.min(marks))
'''

'''
import numpy as np
marks=np.array([[80,90],
                [70,60],
                [50,40]])
print(marks)
'''

'''
import numpy as np
arr=np.zeros(5)
print(arr)
'''

'''
wap by using arrange function
import numpy as np
arr=np.arange(1,11) #start,stop,step
print(arr)
'''





import numpy as np;
a = np.array([5,8,3,4,6,2])
print(a[2:4])

l = [[1,2],[2,4]]
m = np.array(l)
print(m)

l = [[4,5,2],[2,4,6]]
m = np.array(l)
print(m)

a = [[1,2,4],[5,7,1]]
print(a)

l = np.array([[1,2],[2,4],[6,8]])
m = np.array([[6,3,9],[3.2,2]])
print(l.shape)
print(m.shape)

l = np.array([[2,4,6],[6,4,2]])
print(l.shape)

l = np.array([[7,7],[8,8],[9,4]])
print(l[1][0])

l = np.array([[1,0],[2,0],[3,0]])
print(l[2][0])

l = [[2,3],[6,3]]
b = np.array([[8,1],[2,9]])
print(l[0][0] == b[1,0])

#selecting and slicing Arrays

a = np.array([[2,3,],[4,3],[1,2]])
print(a[:,1])

a = np.array([[2,3,],[5,4]])
print(a[:,1])
#this can be used in selection columes a[0,:] this will  select all the colums from the first row
a = np.array([[8,7],[6,5],[4,3]])
print(a[1,:])

a =  np.array([[3,4,1,], [6,2,8,]])
print(a[1,:])

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[:,1])

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[:,:])

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[:,2])

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[1,:])

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[2,:])

#using  slicing you can get 2D array by  specifying the culums and the rows you  want E.g a[1:2, 1:3]

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:3 , 1:3])

a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a[1:2 , 2:3])

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[1:3,2:3]
print(b.shape)

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[2:3,1:3]
print(b.shape)

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[0:3,2:3]
print(b.shape)

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[0:3,3:3]
print(b.shape)

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[1:3,1:3]
print(b.shape)

a = np.array([[4,4,2],[4,3,3],[5,4,1]])
b = a[:,:]
print(b.shape)

a = np.array([[2,3,4],[4,5,6],[7,8,9]])
print(a[1:3,1:3])

#intro to numpy functions , in 1D numpy we can do element wise operation
a = np.array([[1,2],[3,4]])
b = a*2
print(b)

a = np.array([[8,7],[6,5]])
b = a*2
print(b)

a = np.array([[8,7],[6,5]])
b = a+3
print(b)

#using np.mean() to get the mean of a 1D array, the mean is the sum of all element div by the num of element
a = np.array([[8,7]])
print(np.mean(a))


a = np.array([[1,2],[3,4]])
print(np.mean(a))

a = np.array([[1,2,3]])
print(np.sum(a))

#using 2D arrays

a = np.array([[1,2,3],[1,2,3]])
print(np.sum(a))

a = np.array([4,1,6])
print(np.sort(a))

a = np.array([4,1,6])
a = np.sort(a)
print(a)

a = np.array([4,1,6])
b = np.sort(a)
print(b)
print(a)


a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.sum(a)
print(b + c)

a = np.array([1,2,3])
b = np.array([1,2,3])
c = np.mean(a) + np.mean(b)
print(c)

a = np.array([7,2,5])
np.sort(a)
print(a)

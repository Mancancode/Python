#SLICING IN PYTHON USING PYCHARM THE OUT WILL AUTHOMATICALLY PRINT
num = [[2,1,8],[10,11,12],[13,9]]
print(num[1][2])

num1 = [4,6,3,9]
print(num1[:])

num2 = [[7,6],[8,9],[10,11]]
print(num2[1][0])


num3 = [[2,3,3],[4,1,12],[6,2,12]]
print(num3[1][1] + num3[2][2])

numa = [[2,3,5],[4,1,12,13,6]]
print(numa[1][2:])

numa1 = [[2,1,9,4,2],[9,4,2,3,8]]
print(numa1[1] [-2])

numa2 = [5,6,4,2]
numa2[2] = 100
print(numa2)

numa3 =[2,4,6,8,10,12]
x = numa3[2:5]
print(x)

#DELETING IN PYTHON
rsu = [2,3,6,8,10]
del(rsu[3])
print(rsu)

RSU =   [5,2] + [2,1]
del(RSU[1])
print(RSU)


a = [1,9]
b= a
a[0] =9
print(a)
print(b)

a =  [2,4 , 3]
b = a
a[2] = 6
print(b)

a =  [1,2,4]
b = a
a[2] = 2
print(a)

a =  [1,3,6]
x = a[:]
x[2] = 5
print(a)

a =  [7,2,1]
x = a[:]
a[1]=200
print(x)

naz =[2,4,6,8]
yaz  = x[1:]
del(naz[0])
print(naz)

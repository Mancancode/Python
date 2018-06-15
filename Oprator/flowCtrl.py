#if elif else
'''mark=75
if(mark>94):
    print('Grade A')
elif(mark > 40) and (mark <= 80):
    print('Grade B ')
elif(mark > 70) and (mark <= 79):
    print('Grade C')
else:
    print('Grade D')
'''

    #While

num=int(input("Enter the Value of n="))
if (num<=0):
     print("Enter a valid value")
else:
      sum=0
      while(num>0):
          sum+=num
          sum-=1

      print(sum)

'''
# for loop Food
for amount in range(99,0,-1):
    if amount >1:
        print(amount,"Plates of jellof rice on the table, "  ,amount ," plates of jellof rice")
        if amount > 2 :
            suffix = str(amount)+"amount of plate on the table"
        else:
            suffix = " 1 plate of Jellof Rice"
    elif amount == 1:
        print("1 plate of jellof rice on the table", "1 plate of jellof rice")
        suffix="No more plate on the table"

    print("take one down and pass it around",suffix)
    print("---")

#for Break
count = 0
while True:
    print(count)
    count+=1
    if (count > 10):
        break

        #Continue
for x in range(20):
    if (x%2)==0:
        print(x)
'''








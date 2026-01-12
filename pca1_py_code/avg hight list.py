#program to calculate average hight from a list of hight
# without using sum() and len() only using for loop

tt= input("enter the nunbers")
list=tt.split()
#print(list)

count=0
for tt in list:
    count=count+1
#print(count) 

for i in range(count):
    list[i]=int(list[i])

sum=0
for pp in list:
    sum+=pp
    avg=round(sum/count)   
print (avg) 
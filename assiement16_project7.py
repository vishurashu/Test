
#Write a python program to Sort a tuple of tuples by the second item.
#tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
mytuple=(('a',21),('b',37)('c',11)('d',29))
print("original list=",str(mytuple))
for e in range(0,len(mytuple)):
    for j in range(len(mytuple),-i,-1):
        if mytuple[j][1]>mytuple[j+1][1]:
            temp=mytuple[j]
            mytuple=mytuple[j+1]
            mytuple[j+1]=temp
print(str(mytuple))            

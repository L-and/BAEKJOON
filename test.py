
myList=[]

a=[12,7,4,3,9,24]

for n in a:

    if n%2:

        number=a.index(n)

        myList.append(number)

print(myList)